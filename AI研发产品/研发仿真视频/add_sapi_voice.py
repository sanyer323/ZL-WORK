# -*- coding: utf-8 -*-
"""用 Windows SAPI 为成片生成中文旁白并混音。"""
from __future__ import annotations

import re
import subprocess
import time
from pathlib import Path

import imageio_ffmpeg

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "out"
BUILD = OUT / "_build"
FF = imageio_ffmpeg.get_ffmpeg_exe()

SEGMENTS = [
    (
        22.0,
        "理解 FY301 气动核心，先看压电陶瓷。"
        "逆压电效应使陶瓷在电场下发生形变：电压升高，压电盘弯曲，充当喷嘴前方的挡板。"
        "运行监控电压大约三十到七十伏。"
        "电气上它近似电容，只有充放电瞬间有电流，稳态近乎零功耗，因此整机可在三点八毫安两线回路下工作。",
    ),
    (
        20.0,
        "气源经节流孔向喷嘴供恒定小气流，压电盘作挡板调制间隙。"
        "电压升高，挡板靠近喷嘴，排气受阻，先导室压力升高；电压降低则先导压力下降。"
        "手册 FYCAL 参考：供气二十磅时，零伏约两磅，五十伏约六磅，一百伏约十二到十三磅。"
        "先导压力精确但流量小，必须进入下一级放大。",
    ),
    (
        20.0,
        "先导压力作用在大膜片上，经连杆与小膜片力平衡，把微小压力变化放大为滑阀位移。"
        "滑阀上移时，供气进入 OUT1；下移时 OUT1 排气，双作用时 OUT2 方向相反。"
        "失电故障安全：OUT1 到零，OUT2 到供气压力，执行机构回到安全位。",
    ),
    (
        18.0,
        "阀杆磁铁与霍尔传感器非接触测位，安装间隙目标二到四毫米。"
        "设定值与实际位置比较，经比例积分修正压电驱动电压，偏差逐步收敛。"
        "无杠杆磨损，适合高精度长期运行。",
    ),
    (
        18.0,
        "完整链路：四到二十毫安经模数转换进入 CPU，数模与隔离驱动压电盘，"
        "调制先导压力，膜片放大推动滑阀，OUT1 OUT2 驱动执行器，霍尔回馈位置。"
        "电气蓝路径与气动橙路径并行，形成智能定位闭环。这就是 FY301 的工作原理。",
    ),
]

TITLE_DUR = 2.5


def sapi_wav(text: str, wav: Path) -> None:
    txt = BUILD / "_tts_text.txt"
    txt.write_text(text, encoding="utf-8")
    ps = f"""
$OutputEncoding = [Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()
Add-Type -AssemblyName System.Speech
$s = New-Object System.Speech.Synthesis.SpeechSynthesizer
$voices = $s.GetInstalledVoices() | ForEach-Object {{ $_.VoiceInfo }}
$zh = $voices | Where-Object {{ $_.Culture.Name -like 'zh*' }} | Select-Object -First 1
if ($zh) {{ $s.SelectVoice($zh.Name) }}
$s.Rate = -1
$text = [System.IO.File]::ReadAllText('{str(txt).replace("'", "''")}', [System.Text.Encoding]::UTF8)
$s.SetOutputToWaveFile('{str(wav).replace("'", "''")}')
$s.Speak($text)
$s.Dispose()
"""
    script = BUILD / "_tts.ps1"
    script.write_text(ps, encoding="utf-8-sig")  # BOM helps Windows PowerShell
    r = subprocess.run(
        ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", str(script)],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    if r.returncode != 0 or not wav.exists() or wav.stat().st_size < 1000:
        raise RuntimeError(f"SAPI failed: {r.stderr or r.stdout}")


def run(cmd):
    print("+", " ".join(cmd[:6]), "...", flush=True)
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode != 0:
        raise RuntimeError(r.stderr[-1500:])


def main():
    BUILD.mkdir(exist_ok=True)
    silent = BUILD / "silent_master.mp4"
    if not silent.exists():
        raise SystemExit("missing silent_master.mp4 — run build_master.py first")

    audio_parts = []
    for i, (dur, text) in enumerate(SEGMENTS):
        sil = BUILD / f"sapi_sil_{i}.wav"
        # generate silence via ffmpeg
        run([FF, "-y", "-f", "lavfi", "-i", "anullsrc=r=16000:cl=mono", "-t", str(TITLE_DUR), str(sil)])
        wav = BUILD / f"sapi_narr_{i}.wav"
        print(f"TTS segment {i+1}/5 ...", flush=True)
        sapi_wav(text, wav)
        pad = BUILD / f"sapi_pad_{i}.wav"
        run(
            [
                FF,
                "-y",
                "-i",
                str(wav),
                "-af",
                f"apad=whole_dur={dur}",
                "-t",
                str(dur),
                str(pad),
            ]
        )
        audio_parts.extend([sil, pad])

    # concat wavs — re-encode to same format first
    normed = []
    for i, p in enumerate(audio_parts):
        n = BUILD / f"anorm_{i}.wav"
        run([FF, "-y", "-i", str(p), "-ar", "16000", "-ac", "1", str(n)])
        normed.append(n)

    lst = BUILD / "sapi_concat.txt"
    lst.write_text(
        "\n".join(f"file '{p.resolve().as_posix()}'" for p in normed),
        encoding="utf-8",
    )
    voice = BUILD / "sapi_voice_all.wav"
    run([FF, "-y", "-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy", str(voice)])

    srt = OUT / "FY301_研发原理讲解.srt"
    srt_esc = str(srt.resolve()).replace("\\", "/").replace(":", "\\:")
    final = OUT / "FY301_研发原理讲解_完整版.mp4"
    soft = OUT / "FY301_研发原理讲解_软字幕.mp4"

    run(
        [
            FF,
            "-y",
            "-i",
            str(silent),
            "-i",
            str(voice),
            "-vf",
            f"subtitles='{srt_esc}':force_style='FontName=Microsoft YaHei,FontSize=18,PrimaryColour=&H00FFFFFF&,OutlineColour=&H80000000&,Outline=2,Shadow=1,MarginV=28'",
            "-c:v",
            "libx264",
            "-pix_fmt",
            "yuv420p",
            "-c:a",
            "aac",
            "-b:a",
            "128k",
            "-shortest",
            str(final),
        ]
    )
    run(
        [
            FF,
            "-y",
            "-i",
            str(silent),
            "-i",
            str(voice),
            "-i",
            str(srt),
            "-map",
            "0:v",
            "-map",
            "1:a",
            "-map",
            "2",
            "-c:v",
            "copy",
            "-c:a",
            "aac",
            "-c:s",
            "mov_text",
            "-metadata:s:s:0",
            "language=zho",
            "-shortest",
            str(soft),
        ]
    )
    print("DONE", final, flush=True)
    print("SOFT", soft, flush=True)


if __name__ == "__main__":
    main()
