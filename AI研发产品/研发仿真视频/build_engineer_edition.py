# -*- coding: utf-8 -*-
"""
FY301 工程师培训版成片
结构（每段）：实物指认 2.5s → 原理动作 → 现场结论 2s
语言面向仪表/调试工程师，少公式。
不使用失败的半透明叠加动画。
"""
from __future__ import annotations

import asyncio
import re
import subprocess
import textwrap
from pathlib import Path

import imageio_ffmpeg
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "out"
BUILD = OUT / "_eng_build"
SKD_PHOTO = Path(r"C:\Users\sanye\Desktop\SMAR\AI研发产品\SMAR SKD\FY301 SKD Parts.jpeg")
FF = imageio_ffmpeg.get_ffmpeg_exe()
BUILD.mkdir(parents=True, exist_ok=True)

W, H = 1280, 720
FPS = 20
CALL_DUR = 2.8
CONCL_DUR = 2.2

# 指认框：相对 SKD 照片归一化 (l,t,r,b)
SEGMENTS = [
    {
        "id": "01",
        "sim": "01_压电陶瓷原理.mp4",
        "sim_dur": 16,
        "title": "这是哪？压电驱动端",
        "callout": (0.02, 0.02, 0.36, 0.35),
        "callout_note": "气动块顶部：排线接到压电盘（挡板）",
        "narration": (
            "先认零件。气动块顶部那根排线，连的是压电盘，它当挡板用。"
            "电压升高，盘会弯一点，去靠近喷嘴；电压降低，就离开。"
            "现场可用手操器看压电电压，正常大概在三十到七十伏。"
            "它几乎不费电，所以整机能靠回路供电工作。"
        ),
        "conclusion": "现场结论：压电电压异常 → 先查驱动板与压电组件，不要先怪气源。",
    },
    {
        "id": "02",
        "sim": "02_喷嘴挡板先导级.mp4",
        "sim_dur": 16,
        "title": "这是哪？气动块（先导气路）",
        "callout": (0.02, 0.08, 0.38, 0.72),
        "callout_note": "气动块本体：里面是节流孔、喷嘴、先导室",
        "narration": (
            "气源先进气动块。里面有个很小的节流孔，一直往喷嘴送气。"
            "压电挡板靠近，气排不出去，先导室压力就升高；离开，压力就降低。"
            "标定参考：供气二十磅时，零伏大约两磅，五十伏大约六磅，一百伏大约十二磅。"
            "先导气很准，但力气小，还要后面放大。"
        ),
        "conclusion": "现场结论：先导压不对 → 查节流孔堵塞、喷嘴脏、挡板是否到位。",
    },
    {
        "id": "03",
        "sim": "03_膜片放大与滑阀.mp4",
        "sim_dur": 16,
        "title": "这是哪？OUT1 / OUT2",
        "callout": (0.02, 0.25, 0.38, 0.78),
        "callout_note": "气动块侧面接口：IN 供气，OUT1 / OUT2 去执行器",
        "narration": (
            "先导压力推大膜片，再带动滑阀。滑阀才是真正给执行器供气排气的大通道。"
            "滑阀往一边，OUT1 进气；往另一边，OUT2 进气。双作用时两边方向相反。"
            "记住失电安全：OUT1 掉到零，OUT2 到供气压力，阀门回安全位。"
        ),
        "conclusion": "现场结论：有先导压但阀不动 → 查滑阀卡滞、过滤器、OUT 接管是否接反。",
    },
    {
        "id": "04",
        "sim": "04_霍尔反馈与闭环.mp4",
        "sim_dur": 14,
        "title": "这是哪？位置反馈端",
        "callout": (0.00, 0.75, 0.20, 1.00),
        "callout_note": "黑色底座附近：霍尔传感器对着阀杆磁铁",
        "narration": (
            "阀杆上有磁铁，定位器里用霍尔非接触读位置，不用杠杆。"
            "安装时磁铁面到传感器大概二到四毫米，太远会报 HALL 或位置乱跳。"
            "设定开度和实际开度有偏差时，定位器会自动改压电电压，把阀推回目标。"
        ),
        "conclusion": "现场结论：Auto Setup 报 HALL / MGNT → 先查磁铁间距与安装方向。",
    },
    {
        "id": "05",
        "sim": "05_全系统闭环信号流.mp4",
        "sim_dur": 14,
        "title": "整机怎么串起来",
        "callout": (0.05, 0.05, 0.95, 0.95),
        "callout_note": "左气动执行 · 中壳体电路 · 右端盖显示",
        "narration": (
            "串起来就一句话：电流设定进来，板子算出目标，压电调先导气，"
            "膜片滑阀把气送到 OUT1 OUT2，霍尔看阀位再往回改。"
            "调不好时，按这个顺序查：信号和供电 → 压电电压 → 先导压 → OUT 压力 → 磁铁反馈。"
        ),
        "conclusion": "现场结论：按 电→压电→先导→OUT→反馈 五步排查，比盲目换件快。",
    },
]


def font(size: int) -> ImageFont.FreeTypeFont:
    for p in (
        r"C:\Windows\Fonts\msyh.ttc",
        r"C:\Windows\Fonts\msyhbd.ttc",
        r"C:\Windows\Fonts\simhei.ttf",
    ):
        if Path(p).exists():
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def run(cmd: list[str]) -> None:
    print("+", " ".join(str(c) for c in cmd[:7]), "...", flush=True)
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode != 0:
        raise RuntimeError((r.stderr or r.stdout)[-1800:])


def find_sim(name: str) -> Path:
    p = OUT / name
    if p.exists():
        return p
    cands = list(OUT.glob(name[:2] + "*.mp4"))
    if not cands:
        raise FileNotFoundError(name)
    return cands[0]


def make_callout_png(seg: dict, path: Path) -> None:
    photo = Image.open(SKD_PHOTO).convert("RGB")
    # fit photo on dark canvas
    canvas = Image.new("RGB", (W, H), (11, 18, 32))
    img = photo.copy()
    img.thumbnail((W - 80, H - 160), Image.Resampling.LANCZOS)
    ox = (W - img.width) // 2
    oy = 70
    canvas.paste(img, (ox, oy))
    draw = ImageDraw.Draw(canvas, "RGBA")

    l, t, r, b = seg["callout"]
    box = [
        ox + int(l * img.width),
        oy + int(t * img.height),
        ox + int(r * img.width),
        oy + int(b * img.height),
    ]
    # dim outside
    overlay = Image.new("RGBA", (W, H), (11, 18, 32, 0))
    od = ImageDraw.Draw(overlay)
    od.rectangle([0, 0, W, H], fill=(11, 18, 32, 140))
    od.rectangle(box, fill=(0, 0, 0, 0))
    # punch hole: composite cleverly — draw dim then clear box by pasting original region
    canvas_rgba = canvas.convert("RGBA")
    canvas_rgba = Image.alpha_composite(canvas_rgba, overlay)
    # restore sharp callout region
    region = img.crop(
        (
            int(l * img.width),
            int(t * img.height),
            int(r * img.width),
            int(b * img.height),
        )
    )
    canvas_rgba.paste(region, (box[0], box[1]))
    draw = ImageDraw.Draw(canvas_rgba)
    draw.rectangle(box, outline=(79, 195, 247, 255), width=4)

    # title bar
    draw.rectangle([0, 0, W, 58], fill=(15, 23, 42, 230))
    draw.text((28, 12), seg["title"], font=font(28), fill=(232, 238, 247, 255))
    # note
    note = seg["callout_note"]
    tw = font(20)
    draw.rectangle([20, H - 78, W - 20, H - 20], fill=(15, 23, 42, 220))
    draw.text((36, H - 68), "指认：" + note, font=tw, fill=(255, 183, 77, 255))
    canvas_rgba.convert("RGB").save(path, quality=92)


def make_conclusion_png(seg: dict, path: Path) -> None:
    img = Image.new("RGB", (W, H), (11, 18, 32))
    draw = ImageDraw.Draw(img)
    draw.rectangle([60, H // 2 - 90, W - 60, H // 2 + 90], outline=(129, 199, 132), width=3)
    draw.text((W // 2, H // 2 - 55), "现场结论", font=font(26), fill=(129, 199, 132), anchor="mm")
    # wrap conclusion
    lines = textwrap.wrap(seg["conclusion"], width=28)
    y = H // 2 - 10
    for line in lines:
        draw.text((W // 2, y), line, font=font(24), fill=(232, 238, 247), anchor="mm")
        y += 36
    img.save(path, quality=92)


def png_to_video(png: Path, mp4: Path, seconds: float) -> None:
    run(
        [
            FF,
            "-y",
            "-loop",
            "1",
            "-i",
            str(png),
            "-t",
            str(seconds),
            "-r",
            str(FPS),
            "-vf",
            f"scale={W}:{H}:force_original_aspect_ratio=decrease,pad={W}:{H}:(ow-iw)/2:(oh-ih)/2",
            "-c:v",
            "libx264",
            "-pix_fmt",
            "yuv420p",
            "-preset",
            "fast",
            str(mp4),
        ]
    )


def stretch_sim(src: Path, dst: Path, target: float) -> None:
    probe = subprocess.run([FF, "-i", str(src)], capture_output=True, text=True, encoding="utf-8", errors="replace")
    m = re.search(r"Duration:\s*(\d+):(\d+):(\d+\.\d+)", probe.stderr or "")
    src_dur = 5.0
    if m:
        src_dur = int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3))
    factor = target / max(src_dur, 0.1)
    run(
        [
            FF,
            "-y",
            "-stream_loop",
            "3",
            "-i",
            str(src),
            "-filter:v",
            f"setpts={factor}*PTS,fps={FPS},scale={W}:{H}",
            "-an",
            "-t",
            str(target),
            "-c:v",
            "libx264",
            "-pix_fmt",
            "yuv420p",
            "-preset",
            "fast",
            str(dst),
        ]
    )


def srt_ts(sec: float) -> str:
    ms = int(round(sec * 1000))
    h, ms = divmod(ms, 3600000)
    m, ms = divmod(ms, 60000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def split_cues(text: str, t0: float, t1: float):
    parts = []
    buf = ""
    for ch in text:
        buf += ch
        if ch in "。！？；":
            parts.append(buf.strip())
            buf = ""
    if buf.strip():
        parts.append(buf.strip())
    parts = [p for p in parts if p]
    total = sum(len(p) for p in parts) or 1
    span = t1 - t0
    t = t0
    cues = []
    for p in parts:
        d = max(1.5, span * len(p) / total)
        cues.append((t, min(t + d, t1), p))
        t += d
    if cues:
        cues[-1] = (cues[-1][0], t1, cues[-1][2])
    return cues


def sapi_wav(text: str, wav: Path) -> None:
    txt = BUILD / "_tts.txt"
    txt.write_text(text, encoding="utf-8")
    ps = f"""
$OutputEncoding = [Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()
Add-Type -AssemblyName System.Speech
$s = New-Object System.Speech.Synthesis.SpeechSynthesizer
$zh = $s.GetInstalledVoices() | ForEach-Object {{ $_.VoiceInfo }} | Where-Object {{ $_.Culture.Name -like 'zh*' }} | Select-Object -First 1
if ($zh) {{ $s.SelectVoice($zh.Name) }}
$s.Rate = -1
$text = [System.IO.File]::ReadAllText('{str(txt).replace("'", "''")}', [System.Text.Encoding]::UTF8)
$s.SetOutputToWaveFile('{str(wav).replace("'", "''")}')
$s.Speak($text)
$s.Dispose()
"""
    script = BUILD / "_tts.ps1"
    script.write_text(ps, encoding="utf-8-sig")
    r = subprocess.run(
        ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", str(script)],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    if r.returncode != 0 or not wav.exists() or wav.stat().st_size < 800:
        raise RuntimeError(r.stderr or r.stdout or "sapi fail")


def main():
    narr_path = ROOT / "旁白文案_工程师培训版.txt"
    narr_blocks = []
    timeline = []
    t_cursor = 0.0
    video_parts = []

    for i, seg in enumerate(SEGMENTS):
        call_png = BUILD / f"call_{i}.png"
        concl_png = BUILD / f"concl_{i}.png"
        call_mp4 = BUILD / f"call_{i}.mp4"
        concl_mp4 = BUILD / f"concl_{i}.mp4"
        sim_mp4 = BUILD / f"sim_{i}.mp4"

        make_callout_png(seg, call_png)
        make_conclusion_png(seg, concl_png)
        png_to_video(call_png, call_mp4, CALL_DUR)
        png_to_video(concl_png, concl_mp4, CONCL_DUR)
        stretch_sim(find_sim(seg["sim"]), sim_mp4, seg["sim_dur"])

        t0 = t_cursor
        t_call1 = t0 + CALL_DUR
        t_sim1 = t_call1 + seg["sim_dur"]
        t_end = t_sim1 + CONCL_DUR
        timeline.append({**seg, "t0": t0, "t_call1": t_call1, "t_sim1": t_sim1, "t_end": t_end})
        narr_blocks.append(
            f"[{srt_ts(t_call1)} - {srt_ts(t_sim1)}] {seg['title']}\n"
            f"{seg['narration']}\n{seg['conclusion']}\n"
        )
        video_parts.extend([call_mp4, sim_mp4, concl_mp4])
        t_cursor = t_end

    narr_path.write_text("\n".join(narr_blocks), encoding="utf-8")

    # SRT
    srt_lines = []
    idx = 1
    for item in timeline:
        srt_lines += [str(idx), f"{srt_ts(item['t0'])} --> {srt_ts(item['t_call1'])}", item["title"] + "\n" + item["callout_note"], ""]
        idx += 1
        for a, b, text in split_cues(item["narration"], item["t_call1"], item["t_sim1"]):
            wrapped = "\n".join(textwrap.wrap(text, 28))
            srt_lines += [str(idx), f"{srt_ts(a)} --> {srt_ts(b)}", wrapped, ""]
            idx += 1
        srt_lines += [str(idx), f"{srt_ts(item['t_sim1'])} --> {srt_ts(item['t_end'])}", item["conclusion"], ""]
        idx += 1
    srt_path = OUT / "FY301_工程师培训版.srt"
    srt_path.write_text("\n".join(srt_lines), encoding="utf-8")

    # concat silent
    lst = BUILD / "concat.txt"
    lst.write_text("\n".join(f"file '{p.resolve().as_posix()}'" for p in video_parts), encoding="utf-8")
    silent = BUILD / "silent.mp4"
    run([FF, "-y", "-f", "concat", "-safe", "0", "-i", str(lst), "-c:v", "libx264", "-pix_fmt", "yuv420p", "-r", str(FPS), str(silent)])

    # TTS per segment: silence during callout+conclusion short, voice on sim
    # Better: voice covers narration during sim; short voice for conclusion
    audio_parts = []
    for i, item in enumerate(timeline):
        sil1 = BUILD / f"sil_call_{i}.wav"
        run([FF, "-y", "-f", "lavfi", "-i", "anullsrc=r=16000:cl=mono", "-t", str(CALL_DUR), str(sil1)])
        narr_wav = BUILD / f"narr_{i}.wav"
        print(f"TTS {i+1}/{len(timeline)}", flush=True)
        sapi_wav(item["narration"], narr_wav)
        narr_pad = BUILD / f"narrpad_{i}.wav"
        run([FF, "-y", "-i", str(narr_wav), "-af", f"apad=whole_dur={item['sim_dur']}", "-t", str(item["sim_dur"]), str(narr_pad)])
        concl_wav = BUILD / f"concl_{i}.wav"
        sapi_wav(item["conclusion"], concl_wav)
        concl_pad = BUILD / f"conclpad_{i}.wav"
        run([FF, "-y", "-i", str(concl_wav), "-af", f"apad=whole_dur={CONCL_DUR}", "-t", str(CONCL_DUR), str(concl_pad)])
        audio_parts.extend([sil1, narr_pad, concl_pad])

    normed = []
    for i, p in enumerate(audio_parts):
        n = BUILD / f"an_{i}.wav"
        run([FF, "-y", "-i", str(p), "-ar", "16000", "-ac", "1", str(n)])
        normed.append(n)
    alist = BUILD / "acodet.txt"
    alist.write_text("\n".join(f"file '{p.resolve().as_posix()}'" for p in normed), encoding="utf-8")
    voice = BUILD / "voice.wav"
    run([FF, "-y", "-f", "concat", "-safe", "0", "-i", str(alist), "-c", "copy", str(voice)])

    srt_esc = str(srt_path.resolve()).replace("\\", "/").replace(":", "\\:")
    final = OUT / "FY301_工程师培训版.mp4"
    run(
        [
            FF,
            "-y",
            "-i",
            str(silent),
            "-i",
            str(voice),
            "-vf",
            f"subtitles='{srt_esc}':force_style='FontName=Microsoft YaHei,FontSize=17,PrimaryColour=&H00FFFFFF&,OutlineColour=&H80000000&,Outline=2,Shadow=1,MarginV=26'",
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
    print("DONE", final, flush=True)
    print("SRT", srt_path, flush=True)
    print("NARR", narr_path, flush=True)


if __name__ == "__main__":
    main()
