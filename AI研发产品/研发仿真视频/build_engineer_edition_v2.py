# -*- coding: utf-8 -*-
"""
FY301 工程师培训版 v2
- 指认图：来自 FY300定位器拆解图.xlsx「零件实物图」
- 旁白说完为止：先合成语音，再把原理动画拉长对齐，绝不截断旁白
"""
from __future__ import annotations

import json
import re
import subprocess
import textwrap
from pathlib import Path

import imageio_ffmpeg
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "out"
BUILD = OUT / "_eng_build_v2"
PARTS = OUT / "_excel_parts"
FF = imageio_ffmpeg.get_ffmpeg_exe()
BUILD.mkdir(parents=True, exist_ok=True)

W, H = 1280, 720
FPS = 20
CALL_DUR = 3.0
CONCL_PAD = 0.4  # after conclusion speech
MANIFEST = json.loads((PARTS / "manifest.json").read_text(encoding="utf-8"))
BY_LABEL = {m["label"]: m for m in MANIFEST}


def part(label: str) -> Path:
    m = BY_LABEL.get(label)
    if not m:
        # fuzzy
        for k, v in BY_LABEL.items():
            if label in k or k in label:
                m = v
                break
    if not m:
        raise KeyError(f"part not found: {label} / keys={list(BY_LABEL)[:8]}...")
    return PARTS / m["file"]


# 每段用 Excel 零件图（可多张）
SEGMENTS = [
    {
        "id": "01",
        "sim": "01_压电陶瓷原理.mp4",
        "title": "指认：气动组件（压电挡板装在这里）",
        "parts": ["气动组件外壳", "排线外壳"],
        "part_note": "Excel 零件：气动组件外壳 / 排线外壳（压电盘与排线在气动组件顶部）",
        "narration": (
            "先认零件。打开拆解图里的气动组件外壳，顶部排线连的就是压电盘，它当挡板用。"
            "电压升高，盘会弯一点去靠近喷嘴；电压降低就离开。"
            "现场用手操器看压电电压，正常大概三十到七十伏。"
            "它几乎不费电，所以整机能靠回路供电工作。"
        ),
        "conclusion": "现场结论：压电电压异常，先查驱动板和气动组件顶部压电件，不要先怪气源。",
    },
    {
        "id": "02",
        "sim": "02_喷嘴挡板先导级.mp4",
        "title": "指认：过滤元件 + 气动组件（先导气路）",
        "parts": ["过滤元件", "气动组件外壳"],
        "part_note": "Excel 零件：过滤元件、气动组件外壳（内部含节流孔、喷嘴、先导室）",
        "narration": (
            "气源进气动组件前，先过过滤元件。组件里面有节流孔，一直往喷嘴送一小股气。"
            "压电挡板靠近，气排不出去，先导室压力升高；离开，压力降低。"
            "标定参考：供气二十磅时，零伏大约两磅，五十伏大约六磅，一百伏大约十二到十三磅。"
            "先导气很准，但力气小，还要后面放大。"
        ),
        "conclusion": "现场结论：先导压不对，查过滤元件堵塞、节流孔脏、喷嘴脏，或挡板不到位。",
    },
    {
        "id": "03",
        "sim": "03_膜片放大与滑阀.mp4",
        "title": "指认：膜片 + 滑阀",
        "parts": ["膜片", "滑阀"],
        "part_note": "Excel 零件：膜片（编号27）、滑阀（编号29）；旁边还有滑阀套筒、阀座、弹簧",
        "narration": (
            "先导压力推膜片，膜片再带动滑阀。滑阀才是真正给执行器供气排气的大通道。"
            "滑阀往一边，OUT1 进气；往另一边，OUT2 进气。双作用时两边方向相反。"
            "失电时记住：OUT1 掉到零，OUT2 到供气压力，阀门回安全位。"
        ),
        "conclusion": "现场结论：有先导压但阀不动，查滑阀是否卡滞、过滤器、OUT1 OUT2 是否接反。",
    },
    {
        "id": "04",
        "sim": "04_霍尔反馈与闭环.mp4",
        "title": "指认：霍尔传感器",
        "parts": ["霍尔传感器", "传感器外壳"],
        "part_note": "Excel 零件：霍尔传感器（编号35）、传感器外壳",
        "narration": (
            "阀杆上有磁铁，定位器用霍尔传感器非接触读位置，不用机械杠杆。"
            "安装时磁铁面到传感器大约二到四毫米，太远会报 HALL，或位置乱跳。"
            "设定开度和实际开度有偏差时，定位器会自动改压电电压，把阀推回目标。"
        ),
        "conclusion": "现场结论：Auto Setup 报 HALL 或 MGNT，先查磁铁间距和安装方向。",
    },
    {
        "id": "05",
        "sim": "05_全系统闭环信号流.mp4",
        "title": "指认：线路板 + 气动组件 + 霍尔",
        "parts": ["线路板", "气动组件外壳", "霍尔传感器"],
        "part_note": "Excel 零件：线路板（电）、气动组件外壳（气）、霍尔传感器（反馈）",
        "narration": (
            "串起来就一句话：电流设定进线路板，板子算出目标，压电调先导气，"
            "膜片滑阀把气送到 OUT1 OUT2，霍尔看阀位再往回改。"
            "调不好时，按这个顺序查：信号供电，压电电压，先导压，OUT 压力，磁铁反馈。"
        ),
        "conclusion": "现场结论：按电、压电、先导、OUT、反馈五步排查，比盲目换件快。",
    },
]


def font(size: int):
    for p in (r"C:\Windows\Fonts\msyh.ttc", r"C:\Windows\Fonts\simhei.ttf"):
        if Path(p).exists():
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def run(cmd: list[str]) -> None:
    print("+", " ".join(str(c) for c in cmd[:8]), "...", flush=True)
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode != 0:
        raise RuntimeError((r.stderr or r.stdout)[-2000:])


def probe_duration(path: Path) -> float:
    r = subprocess.run([FF, "-i", str(path)], capture_output=True, text=True, encoding="utf-8", errors="replace")
    m = re.search(r"Duration:\s*(\d+):(\d+):(\d+\.\d+)", r.stderr or "")
    if not m:
        return 0.0
    return int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3))


def find_sim(name: str) -> Path:
    p = OUT / name
    if p.exists():
        return p
    cands = list(OUT.glob(name[:2] + "*.mp4"))
    if not cands:
        raise FileNotFoundError(name)
    return cands[0]


def make_callout_png(seg: dict, path: Path) -> None:
    canvas = Image.new("RGB", (W, H), (11, 18, 32))
    draw = ImageDraw.Draw(canvas)
    draw.rectangle([0, 0, W, 64], fill=(15, 23, 42))
    draw.text((28, 14), seg["title"], font=font(26), fill=(232, 238, 247))

    labels = seg["parts"]
    n = len(labels)
    gap = 24
    usable_w = W - 60
    usable_h = H - 150
    cell_w = (usable_w - gap * (n - 1)) // n
    cell_h = usable_h

    for i, lab in enumerate(labels):
        img = Image.open(part(lab)).convert("RGB")
        # fit in cell
        img.thumbnail((cell_w - 20, cell_h - 70), Image.Resampling.LANCZOS)
        x0 = 30 + i * (cell_w + gap)
        y0 = 80
        # card
        draw.rectangle([x0, y0, x0 + cell_w, y0 + cell_h], outline=(79, 195, 247), width=2)
        px = x0 + (cell_w - img.width) // 2
        py = y0 + 20
        canvas.paste(img, (px, py))
        # caption
        m = BY_LABEL[lab]
        cap = f"#{m.get('part_no') or '-'}  {lab}"
        # wrap
        tw = font(18)
        draw.text((x0 + 12, y0 + cell_h - 48), cap, font=tw, fill=(255, 183, 77))

    draw.rectangle([20, H - 58, W - 20, H - 16], fill=(15, 23, 42))
    draw.text((36, H - 48), seg["part_note"], font=font(16), fill=(148, 163, 184))
    canvas.save(path, quality=92)


def make_conclusion_png(seg: dict, path: Path) -> None:
    img = Image.new("RGB", (W, H), (11, 18, 32))
    draw = ImageDraw.Draw(img)
    draw.rectangle([50, H // 2 - 100, W - 50, H // 2 + 100], outline=(129, 199, 132), width=3)
    draw.text((W // 2, H // 2 - 60), "现场结论", font=font(26), fill=(129, 199, 132), anchor="mm")
    y = H // 2 - 15
    for line in textwrap.wrap(seg["conclusion"], width=26):
        draw.text((W // 2, y), line, font=font(24), fill=(232, 238, 247), anchor="mm")
        y += 36
    img.save(path, quality=92)


def png_to_video(png: Path, mp4: Path, seconds: float) -> None:
    run(
        [
            FF, "-y", "-loop", "1", "-i", str(png),
            "-t", f"{seconds:.3f}", "-r", str(FPS),
            "-vf", f"scale={W}:{H}:force_original_aspect_ratio=decrease,pad={W}:{H}:(ow-iw)/2:(oh-ih)/2",
            "-c:v", "libx264", "-pix_fmt", "yuv420p", "-preset", "fast", str(mp4),
        ]
    )


def stretch_sim(src: Path, dst: Path, target: float) -> None:
    src_dur = max(probe_duration(src), 0.1)
    factor = target / src_dur
    run(
        [
            FF, "-y", "-stream_loop", "8", "-i", str(src),
            "-filter:v", f"setpts={factor}*PTS,fps={FPS},scale={W}:{H}",
            "-an", "-t", f"{target:.3f}",
            "-c:v", "libx264", "-pix_fmt", "yuv420p", "-preset", "fast", str(dst),
        ]
    )


def sapi_wav(text: str, wav: Path, rate: int = -2) -> float:
    """Generate TTS; return duration seconds."""
    txt = BUILD / "_tts.txt"
    txt.write_text(text, encoding="utf-8")
    ps = f"""
$OutputEncoding = [Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()
Add-Type -AssemblyName System.Speech
$s = New-Object System.Speech.Synthesis.SpeechSynthesizer
$zh = $s.GetInstalledVoices() | ForEach-Object {{ $_.VoiceInfo }} | Where-Object {{ $_.Culture.Name -like 'zh*' }} | Select-Object -First 1
if ($zh) {{ $s.SelectVoice($zh.Name) }}
$s.Rate = {rate}
$text = [System.IO.File]::ReadAllText('{str(txt).replace("'", "''")}', [System.Text.Encoding]::UTF8)
$s.SetOutputToWaveFile('{str(wav).replace("'", "''")}')
$s.Speak($text)
$s.Dispose()
"""
    script = BUILD / "_tts.ps1"
    script.write_text(ps, encoding="utf-8-sig")
    r = subprocess.run(
        ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", str(script)],
        capture_output=True, text=True, encoding="utf-8", errors="replace",
    )
    if r.returncode != 0 or not wav.exists() or wav.stat().st_size < 800:
        raise RuntimeError(r.stderr or r.stdout or "sapi fail")
    # re-encode to known format and probe
    norm = wav.with_name(wav.stem + "_n.wav")
    run([FF, "-y", "-i", str(wav), "-ar", "16000", "-ac", "1", str(norm)])
    wav.write_bytes(norm.read_bytes())
    return probe_duration(wav)


def silence_wav(path: Path, seconds: float) -> None:
    run([FF, "-y", "-f", "lavfi", "-i", "anullsrc=r=16000:cl=mono", "-t", f"{seconds:.3f}", str(path)])


def srt_ts(sec: float) -> str:
    ms = int(round(sec * 1000))
    h, ms = divmod(ms, 3600000)
    m, ms = divmod(ms, 60000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def split_cues(text: str, t0: float, t1: float):
    parts, buf = [], ""
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
    t, cues = t0, []
    for p in parts:
        d = max(1.8, span * len(p) / total)
        cues.append((t, min(t + d, t1), p))
        t += d
    if cues:
        cues[-1] = (cues[-1][0], t1, cues[-1][2])
    return cues


def main():
    # verify excel parts exist
    for seg in SEGMENTS:
        for lab in seg["parts"]:
            p = part(lab)
            print("part ok:", lab, "->", p.name, flush=True)

    video_parts = []
    audio_parts = []
    timeline = []
    t_cursor = 0.0
    narr_blocks = []

    for i, seg in enumerate(SEGMENTS):
        print(f"\n=== segment {i+1}/{len(SEGMENTS)} {seg['id']} ===", flush=True)
        call_png = BUILD / f"call_{i}.png"
        concl_png = BUILD / f"concl_{i}.png"
        make_callout_png(seg, call_png)
        make_conclusion_png(seg, concl_png)

        # TTS first — durations drive video length
        narr_wav = BUILD / f"narr_{i}.wav"
        concl_wav = BUILD / f"concl_{i}.wav"
        narr_dur = sapi_wav(seg["narration"], narr_wav, rate=-2)
        concl_dur = sapi_wav(seg["conclusion"], concl_wav, rate=-1)
        # add small tail so last syllable isn't abrupt
        narr_dur_use = narr_dur + 0.6
        concl_dur_use = concl_dur + CONCL_PAD

        call_mp4 = BUILD / f"call_{i}.mp4"
        sim_mp4 = BUILD / f"sim_{i}.mp4"
        concl_mp4 = BUILD / f"concl_{i}.mp4"
        png_to_video(call_png, call_mp4, CALL_DUR)
        stretch_sim(find_sim(seg["sim"]), sim_mp4, narr_dur_use)
        png_to_video(concl_png, concl_mp4, concl_dur_use)

        # audio: silence during callout, full narr (padded), full concl (padded)
        sil = BUILD / f"sil_{i}.wav"
        silence_wav(sil, CALL_DUR)
        narr_pad = BUILD / f"narrpad_{i}.wav"
        run([FF, "-y", "-i", str(narr_wav), "-af", f"apad=whole_dur={narr_dur_use:.3f}", "-t", f"{narr_dur_use:.3f}", str(narr_pad)])
        concl_pad = BUILD / f"conclpad_{i}.wav"
        run([FF, "-y", "-i", str(concl_wav), "-af", f"apad=whole_dur={concl_dur_use:.3f}", "-t", f"{concl_dur_use:.3f}", str(concl_pad)])

        video_parts.extend([call_mp4, sim_mp4, concl_mp4])
        audio_parts.extend([sil, narr_pad, concl_pad])

        t0 = t_cursor
        t_call1 = t0 + CALL_DUR
        t_sim1 = t_call1 + narr_dur_use
        t_end = t_sim1 + concl_dur_use
        timeline.append({**seg, "t0": t0, "t_call1": t_call1, "t_sim1": t_sim1, "t_end": t_end, "narr_dur": narr_dur})
        narr_blocks.append(
            f"[{srt_ts(t_call1)} - {srt_ts(t_sim1)}] {seg['title']} (旁白{narr_dur:.1f}s)\n"
            f"{seg['narration']}\n{seg['conclusion']}\n"
        )
        t_cursor = t_end
        print(f"  narr={narr_dur:.2f}s -> video={narr_dur_use:.2f}s; concl={concl_dur:.2f}s", flush=True)

    narr_path = ROOT / "旁白文案_工程师培训版.txt"
    narr_path.write_text("\n".join(narr_blocks), encoding="utf-8")

    # SRT
    srt_lines, idx = [], 1
    for item in timeline:
        srt_lines += [str(idx), f"{srt_ts(item['t0'])} --> {srt_ts(item['t_call1'])}", item["title"] + "\n" + item["part_note"], ""]
        idx += 1
        for a, b, text in split_cues(item["narration"], item["t_call1"], item["t_sim1"]):
            srt_lines += [str(idx), f"{srt_ts(a)} --> {srt_ts(b)}", "\n".join(textwrap.wrap(text, 28)), ""]
            idx += 1
        srt_lines += [str(idx), f"{srt_ts(item['t_sim1'])} --> {srt_ts(item['t_end'])}", item["conclusion"], ""]
        idx += 1
    srt_path = OUT / "FY301_工程师培训版.srt"
    srt_path.write_text("\n".join(srt_lines), encoding="utf-8")

    # concat video
    vlist = BUILD / "vconcat.txt"
    vlist.write_text("\n".join(f"file '{p.resolve().as_posix()}'" for p in video_parts), encoding="utf-8")
    silent = BUILD / "silent.mp4"
    run([FF, "-y", "-f", "concat", "-safe", "0", "-i", str(vlist), "-c:v", "libx264", "-pix_fmt", "yuv420p", "-r", str(FPS), str(silent)])

    # concat audio (normalize first)
    normed = []
    for j, p in enumerate(audio_parts):
        n = BUILD / f"a_{j}.wav"
        run([FF, "-y", "-i", str(p), "-ar", "16000", "-ac", "1", str(n)])
        normed.append(n)
    alist = BUILD / "aconcat.txt"
    alist.write_text("\n".join(f"file '{p.resolve().as_posix()}'" for p in normed), encoding="utf-8")
    voice = BUILD / "voice.wav"
    run([FF, "-y", "-f", "concat", "-safe", "0", "-i", str(alist), "-c", "copy", str(voice)])

    srt_esc = str(srt_path.resolve()).replace("\\", "/").replace(":", "\\:")
    final = OUT / "FY301_工程师培训版.mp4"
    # Do NOT use -shortest in a way that cuts audio: pad video if needed
    run(
        [
            FF, "-y",
            "-i", str(silent),
            "-i", str(voice),
            "-vf", f"subtitles='{srt_esc}':force_style='FontName=Microsoft YaHei,FontSize=17,PrimaryColour=&H00FFFFFF&,OutlineColour=&H80000000&,Outline=2,Shadow=1,MarginV=26'",
            "-c:v", "libx264", "-pix_fmt", "yuv420p",
            "-c:a", "aac", "-b:a", "128k",
            "-shortest",
            str(final),
        ]
    )
    # verify durations
    vd = probe_duration(final)
    print("DONE", final, f"duration={vd:.1f}s", flush=True)
    print("SRT", srt_path, flush=True)


if __name__ == "__main__":
    main()
