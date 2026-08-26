# -*- coding: utf-8 -*-
"""
FY301 原理讲解版（工程师能看懂，但不是排故障）
结构：Excel 零件指认 → 原理动作 → 本段要点（机理，非排查）
旁白说完再切镜头。
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
BUILD = OUT / "_principle_build"
PARTS = OUT / "_excel_parts"
FYCAL_FIGS = OUT / "_fycal_figs" / "_named"
FF = imageio_ffmpeg.get_ffmpeg_exe()
BUILD.mkdir(parents=True, exist_ok=True)

W, H = 1280, 720
FPS = 20
CALL_DUR = 3.5  # Excel 零件指认时长；FYCAL 段改为全程分屏，不再单独切走
TAIL = 0.5
STRIP_W = 420  # 右侧照片栏宽度
MANIFEST = json.loads((PARTS / "manifest.json").read_text(encoding="utf-8"))
BY_LABEL = {m["label"]: m for m in MANIFEST}
FYCAL_MANIFEST_PATH = FYCAL_FIGS / "manifest.json"


def fycal_path(fname: str) -> Path:
    """Resolve FYCAL handbook images by relative filename only (no absolute host paths)."""
    name = Path(fname).name
    return FYCAL_FIGS / name


def load_fycal_manifest() -> dict[str, dict]:
    if not FYCAL_MANIFEST_PATH.exists():
        return {}
    rows = json.loads(FYCAL_MANIFEST_PATH.read_text(encoding="utf-8"))
    out = {}
    for row in rows:
        rel = Path(str(row.get("file", ""))).name
        if not rel:
            continue
        out[rel] = {**row, "file": rel}
    return out


def preflight_assets() -> None:
    """Fail early if segment images or FYCAL manifest entries are missing/inconsistent."""
    fycal_man = load_fycal_manifest()
    missing_files: list[str] = []
    missing_manifest: list[str] = []
    abs_in_manifest: list[str] = []

    if FYCAL_MANIFEST_PATH.exists():
        raw = json.loads(FYCAL_MANIFEST_PATH.read_text(encoding="utf-8"))
        for row in raw:
            f = str(row.get("file", ""))
            if Path(f).is_absolute() or ":\\" in f or f.startswith("\\\\"):
                abs_in_manifest.append(f)

    for seg in SEGMENTS:
        for lab in seg.get("parts") or []:
            p = part(lab)
            if not p.exists():
                missing_files.append(str(p))
            else:
                print("part ok:", lab, "->", p.name, flush=True)
        for fname, _ in seg.get("fycal_imgs") or []:
            p = fycal_path(fname)
            if not p.exists():
                missing_files.append(str(p))
            else:
                print("fycal ok:", p.name, flush=True)
            if p.name not in fycal_man:
                missing_manifest.append(p.name)

    if abs_in_manifest:
        raise SystemExit(
            "FYCAL manifest still contains absolute paths; "
            "rebuild with relative filenames only:\n  "
            + "\n  ".join(abs_in_manifest[:5])
        )
    if missing_files:
        raise SystemExit("Missing asset files:\n  " + "\n  ".join(missing_files))
    if missing_manifest:
        raise SystemExit(
            "FYCAL images used by SEGMENTS but missing from manifest.json:\n  "
            + "\n  ".join(missing_manifest)
        )

SEGMENTS = [
    {
        "id": "01",
        "sim": "01_压电陶瓷原理.mp4",
        "title": "压电陶瓷挡板：电 → 微小位移",
        "parts": [],
        "fycal_imgs": [
            ("fig16_cleaning_piezo.png", "Fig.16 清洁中的压电陶瓷片"),
            ("fig18_exploded_piezo.png", "Fig.18 压电底座爆炸图"),
            ("fig14_piezo_base_labeled.png", "Fig.14 压电底座在 FYCAL 上"),
        ],
        # 旁白节拍：陶瓷片 → 爆炸叠装 → FYCAL 底座（相对时间 0~1）
        "photo_beats": [0.0, 0.30, 0.58],
        "part_note": "fycalme 实物图 + FY301ME §2.1：Piezo Vane = 喷嘴挡板",
        "narration": (
            "按 FY301 手册：先导级的挡板，就是这块压电陶瓷圆片。"
            "控制电路加上电压，圆片弯曲，挡住喷嘴前方那一股小气流。"
            "中间爆炸图是盔帽、垫圈、弹簧的叠装；旋转盔帽改变高度 h，用来标定工作点。"
            "右图把底座接到 FYCAL，可离线加零到一百伏，单独看陶瓷动作。"
            "电气上它像电容，稳态几乎不耗环路电流；工作电压希望靠近五十伏，正常约三十到七十伏。"
            "这一步只做一件事：把电，变成挡板的微小机械位移。"
        ),
        "takeaway": "本段要点：压电片=喷嘴挡板（Piezo Vane）；调 h 定工作点；驱动约 0–100 V。",
    },
    {
        "id": "02",
        "sim": "02_喷嘴挡板先导级.mp4",
        "title": "节流孔 + 喷嘴：先导室压力",
        "parts": [],
        "fycal_imgs": [
            ("fig12_cal_on_block.png", "Fig.12 压电底座接 FYCAL 供电与气路"),
            ("fig16_cleaning_piezo.png", "Fig.16 压电片、底座腔、O圈、垫圈"),
        ],
        "photo_beats": [0.0, 0.48],
        "part_note": "FY301ME：restriction+nozzle 分压；FYCAL @20 psi → ≤2 / 5.8–6.2 / 12–13 psi",
        "narration": (
            "气先经过节流孔，再到喷嘴。节流孔和喷嘴组成分压回路，先导室压力就在这里形成。"
            "挡板靠近喷嘴，先导压升高；挡板离开，先导压降低。电压升高，通常对应先导压升高。"
            "手册用 FYCAL 单独标定底座：供气二十磅。"
            "先零伏、一百伏、再回零伏，减小迟滞；再固定五十伏，把先导压调到五点八到六点二磅。"
            "核对：零伏不高于两磅；一百伏约十二到十三磅。"
            "先导压很准，但流量很小，所以必须交给下一级伺服放大。"
        ),
        "takeaway": "本段要点：节流孔+喷嘴+挡板 → 先导压；FYCAL 判据按 FY301ME。",
    },
    {
        "id": "03",
        "sim": "03_膜片放大与滑阀.mp4",
        "title": "伺服级：膜片力平衡 → 滑阀",
        "parts": ["膜片", "滑阀"],
        "fycal_imgs": [],
        "part_note": "FY301ME §2.1：大膜片先导室 / 小膜片滑阀室力平衡；滑阀提供更大气流",
        "narration": (
            "先导室有一块较大的膜片，滑阀室有一块较小的膜片。"
            "稳态时：先导气压推大膜片的力，等于滑阀侧推小膜片的力，两力平衡。"
            "先导压一变，平衡被打破，滑阀在套筒里上下移动，直到到达新的平衡位置。"
            "滑阀一动，就打开大通道：把供气送到 OUT1 或 OUT2，或从排气口放掉。"
            "直观表现是：驱动电压升高，往往一侧气室出气；电压降低，另一侧气室出气。"
            "滑阀的作用，是把节流孔那点小流量，放大成能推动执行器的大气流。"
            "失电安全逻辑通常是：OUT1 到零，OUT2 到供气压力，执行器回预定安全位。"
        ),
        "takeaway": "本段要点：先导压变化 → 膜片力再平衡 → 滑阀移位 → OUT1/OUT2。",
    },
    {
        "id": "04",
        "sim": "04_霍尔反馈与闭环.mp4",
        "title": "霍尔反馈：实际阀位回控制回路",
        "parts": ["霍尔传感器", "传感器外壳"],
        "fycal_imgs": [],
        "part_note": "FY301ME §2.2：Control 同时吃 CPU 设定与 Hall 反馈",
        "narration": (
            "阀门一动，磁铁跟着动。霍尔传感器装在外壳里，不接触磁铁，只读磁场，得到实际开度。"
            "安装间隙大约二到四毫米，读数才稳。"
            "控制电路一边接收来自 CPU 的设定开度，一边接收霍尔反馈的实际开度。"
            "两者一比较，就去增减压电电压，阀门继续被修正，直到落到目标位置。"
            "这就是位置闭环：不是开环给一个电压就算完。"
        ),
        "takeaway": "本段要点：Hall 反馈实际开度；与设定比较后回改压电电压。",
    },
    {
        "id": "05",
        "sim": "05_全系统闭环信号流.mp4",
        "title": "全链路：电 → 气 → 机 → 再回电",
        "parts": ["线路板", "气动组件外壳", "霍尔传感器"],
        "fycal_imgs": [],
        "part_note": "FY301ME 图2.2：A/D→CPU→Control/压电隔离；环路约 3.8 mA 供电定位器电路",
        "narration": (
            "整机按手册方框图这样走："
            "四到二十毫安经模数转换进 CPU，CPU 给出目标开度；"
            "控制电路结合霍尔反馈，经隔离后驱动压电挡板。"
            "定位器电路从环路取电，正常工作约三点八毫安量级，所以稳态压电几乎不额外耗电。"
            "气路上：节流孔喷嘴形成先导压，膜片滑阀放大到 OUT1 OUT2，推动执行器。"
            "阀位再经霍尔回到控制电路。整条链是：电，到陶瓷位移，到先导压，到大气流，到阀位，再回电。"
            "这就是 FY301 的工作原理。"
        ),
        "takeaway": "本段要点：4–20 mA→CPU→压电→先导→滑阀→阀位Hall→再校正。",
    },
]


def font(size: int):
    for p in (r"C:\Windows\Fonts\msyh.ttc", r"C:\Windows\Fonts\simhei.ttf"):
        if Path(p).exists():
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def part(label: str) -> Path:
    m = BY_LABEL.get(label)
    if not m:
        for k, v in BY_LABEL.items():
            if label in k or k in label:
                m = v
                break
    if not m:
        raise KeyError(label)
    return PARTS / m["file"]


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

    # Prefer FYCAL handbook photos when provided
    items = []
    for fname, cap in seg.get("fycal_imgs") or []:
        p = fycal_path(fname)
        if not p.exists():
            raise FileNotFoundError(p)
        items.append((p, cap))
    if not items:
        for lab in seg.get("parts") or []:
            m = BY_LABEL[lab]
            items.append((part(lab), f"#{m.get('part_no') or '-'}  {lab}"))

    n = len(items)
    if n == 0:
        raise ValueError(f"no images for segment {seg['id']}")
    gap = 18
    usable_w = W - 60
    usable_h = H - 150
    cell_w = (usable_w - gap * (n - 1)) // n

    for i, (img_path, cap) in enumerate(items):
        img = Image.open(img_path).convert("RGB")
        img.thumbnail((cell_w - 16, usable_h - 78), Image.Resampling.LANCZOS)
        x0 = 30 + i * (cell_w + gap)
        y0 = 80
        draw.rectangle([x0, y0, x0 + cell_w, y0 + usable_h], outline=(79, 195, 247), width=2)
        px = x0 + (cell_w - img.width) // 2
        py = y0 + 16
        canvas.paste(img, (px, py))
        # wrap caption
        lines = textwrap.wrap(cap, width=max(10, cell_w // 14))
        ty = y0 + usable_h - 18 - 20 * (len(lines) - 1)
        for line in lines:
            draw.text((x0 + 10, ty), line, font=font(15), fill=(255, 183, 77))
            ty += 20

    draw.rectangle([20, H - 58, W - 20, H - 16], fill=(15, 23, 42))
    draw.text((36, H - 48), seg["part_note"], font=font(15), fill=(148, 163, 184))
    canvas.save(path, quality=92)


def make_takeaway_png(seg: dict, path: Path) -> None:
    img = Image.new("RGB", (W, H), (11, 18, 32))
    draw = ImageDraw.Draw(img)
    draw.rectangle([50, H // 2 - 100, W - 50, H // 2 + 100], outline=(79, 195, 247), width=3)
    draw.text((W // 2, H // 2 - 60), "本段要点", font=font(26), fill=(79, 195, 247), anchor="mm")
    y = H // 2 - 15
    for line in textwrap.wrap(seg["takeaway"], width=26):
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


def active_photo_index(t: float, n: int, beats: list[float] | None) -> tuple[int, float]:
    """根据旁白节拍返回 (当前图索引, 段内进度 0~1)。"""
    if n <= 0:
        return 0, 0.0
    if not beats or len(beats) < n:
        slot = 1.0 / n
        active = min(n - 1, int(t * n))
        local = (t - active * slot) / slot if slot > 0 else 0.0
        return active, max(0.0, min(1.0, local))
    ends = list(beats[1:]) + [1.0]
    active = 0
    for i, b in enumerate(beats[:n]):
        if t >= b:
            active = i
    start = beats[active]
    end = ends[active] if active < len(ends) else 1.0
    span = max(end - start, 1e-6)
    local = (t - start) / span
    return active, max(0.0, min(1.0, local))


def make_animated_photo_panel(
    fycal_imgs: list,
    duration: float,
    out_mp4: Path,
    beats: list[float] | None = None,
) -> None:
    """右侧照片栏视频：三张全程可见，按旁白节拍高亮并 Ken Burns。"""
    n_frames = max(2, int(duration * FPS))
    imgs = []
    caps = []
    for fname, cap in fycal_imgs:
        im = Image.open(fycal_path(fname)).convert("RGB")
        imgs.append(im)
        caps.append(cap)
    n = len(imgs)
    panel_h = H
    panel_w = STRIP_W
    gap = 8
    cell_h = (panel_h - 50 - gap * (n + 1)) // n

    cmd = [
        FF, "-y",
        "-f", "rawvideo", "-pix_fmt", "rgb24",
        "-s", f"{panel_w}x{panel_h}", "-r", str(FPS),
        "-i", "-",
        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-preset", "ultrafast",
        str(out_mp4),
    ]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stderr=subprocess.PIPE)

    for fi in range(n_frames):
        t = fi / max(n_frames - 1, 1)
        active, local = active_photo_index(t, n, beats)
        zoom = 1.0 + 0.12 * local

        canvas = Image.new("RGB", (panel_w, panel_h), (15, 23, 42))
        draw = ImageDraw.Draw(canvas)
        draw.text((10, 10), "FYCAL 实物图（全程）", font=font(14), fill=(148, 163, 184))

        for i, im in enumerate(imgs):
            y0 = 40 + gap + i * (cell_h + gap)
            box = [6, y0, panel_w - 6, y0 + cell_h]
            src = im
            if i == active:
                w, h = src.size
                cw, ch = max(8, int(w / zoom)), max(8, int(h / zoom))
                ox = int((w - cw) * (0.2 + 0.6 * local))
                oy = int((h - ch) * (0.3 + 0.4 * (1 - local)))
                ox = max(0, min(ox, w - cw))
                oy = max(0, min(oy, h - ch))
                src = src.crop((ox, oy, ox + cw, oy + ch))
            thumb = src.copy()
            thumb.thumbnail((panel_w - 20, cell_h - 36), Image.Resampling.LANCZOS)
            px = 6 + (panel_w - 12 - thumb.width) // 2
            py = y0 + 4
            fill = (30, 58, 80) if i == active else (22, 30, 46)
            draw.rectangle(box, fill=fill, outline=(79, 195, 247) if i == active else (51, 65, 85), width=3 if i == active else 1)
            canvas.paste(thumb, (px, py))
            cap = caps[i]
            short = textwrap.wrap(cap, width=22)[:2]
            ty = y0 + cell_h - 18 - 14 * (len(short) - 1)
            for line in short:
                draw.text((12, ty), line, font=font(12), fill=(255, 183, 77) if i == active else (148, 163, 184))
                ty += 14
            if i == active:
                draw.text((panel_w - 70, y0 + 6), "讲解中", font=font(12), fill=(129, 199, 132))

        proc.stdin.write(canvas.tobytes())

    proc.stdin.close()
    err = proc.stderr.read().decode("utf-8", errors="replace")
    code = proc.wait()
    if code != 0:
        raise RuntimeError(err[-1500:])


def compose_sim_with_photos(
    sim_mp4: Path,
    fycal_imgs: list,
    duration: float,
    out_mp4: Path,
    beats: list[float] | None = None,
) -> None:
    """左侧原理动画 + 右侧全程可见、会动的 FYCAL 照片栏。"""
    panel = BUILD / (out_mp4.stem + "_panel.mp4")
    print(f"  photo panel {duration:.1f}s ...", flush=True)
    make_animated_photo_panel(fycal_imgs, duration, panel, beats=beats)
    main_w = W - STRIP_W
    run(
        [
            FF, "-y",
            "-i", str(sim_mp4),
            "-i", str(panel),
            "-filter_complex",
            f"[0:v]scale={main_w}:{H}:force_original_aspect_ratio=decrease,"
            f"pad={main_w}:{H}:(ow-iw)/2:(oh-ih)/2:color=0x0b1220,setsar=1[left];"
            f"[1:v]scale={STRIP_W}:{H},setsar=1[right];"
            f"[left][right]hstack=inputs=2[v]",
            "-map", "[v]",
            "-t", f"{duration:.3f}",
            "-c:v", "libx264", "-pix_fmt", "yuv420p", "-preset", "fast",
            str(out_mp4),
        ]
    )


def sapi_wav(text: str, wav: Path, rate: int = -2) -> float:
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
    (BUILD / "_tts.ps1").write_text(ps, encoding="utf-8-sig")
    r = subprocess.run(
        ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", str(BUILD / "_tts.ps1")],
        capture_output=True, text=True, encoding="utf-8", errors="replace",
    )
    if r.returncode != 0 or not wav.exists() or wav.stat().st_size < 800:
        raise RuntimeError(r.stderr or r.stdout or "sapi fail")
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
    preflight_assets()

    video_parts, audio_parts, timeline, narr_blocks = [], [], [], []
    t_cursor = 0.0

    for i, seg in enumerate(SEGMENTS):
        print(f"\n=== {seg['id']} ===", flush=True)
        call_png = BUILD / f"call_{i}.png"
        take_png = BUILD / f"take_{i}.png"
        make_callout_png(seg, call_png)
        make_takeaway_png(seg, take_png)

        narr_wav = BUILD / f"narr_{i}.wav"
        take_wav = BUILD / f"take_{i}.wav"
        narr_dur = sapi_wav(seg["narration"], narr_wav, rate=-2)
        take_dur = sapi_wav(seg["takeaway"], take_wav, rate=-1)
        narr_use = narr_dur + TAIL
        take_use = take_dur + 0.35

        call_mp4 = BUILD / f"call_{i}.mp4"
        sim_raw = BUILD / f"simraw_{i}.mp4"
        sim_mp4 = BUILD / f"sim_{i}.mp4"
        take_mp4 = BUILD / f"take_{i}.mp4"

        stretch_sim(find_sim(seg["sim"]), sim_raw, narr_use)
        has_fycal = bool(seg.get("fycal_imgs"))
        if has_fycal:
            # 讲解全程：左原理 + 右三张会动的实物图（不再切走）
            compose_sim_with_photos(
                sim_raw,
                seg["fycal_imgs"],
                narr_use,
                sim_mp4,
                beats=seg.get("photo_beats"),
            )
            # 开场用同一套图短指认（可选，缩短以免重复感）
            make_callout_png(seg, call_png)
            png_to_video(call_png, call_mp4, 2.5)
            call_dur_i = 2.5
        else:
            make_callout_png(seg, call_png)
            png_to_video(call_png, call_mp4, CALL_DUR)
            # copy stretched sim to full width
            run([FF, "-y", "-i", str(sim_raw), "-c", "copy", str(sim_mp4)])
            call_dur_i = CALL_DUR

        png_to_video(take_png, take_mp4, take_use)

        sil = BUILD / f"sil_{i}.wav"
        silence_wav(sil, call_dur_i)
        narr_pad = BUILD / f"narrpad_{i}.wav"
        take_pad = BUILD / f"takepad_{i}.wav"
        run([FF, "-y", "-i", str(narr_wav), "-af", f"apad=whole_dur={narr_use:.3f}", "-t", f"{narr_use:.3f}", str(narr_pad)])
        run([FF, "-y", "-i", str(take_wav), "-af", f"apad=whole_dur={take_use:.3f}", "-t", f"{take_use:.3f}", str(take_pad)])

        video_parts.extend([call_mp4, sim_mp4, take_mp4])
        audio_parts.extend([sil, narr_pad, take_pad])

        t0 = t_cursor
        t_call1 = t0 + call_dur_i
        t_sim1 = t_call1 + narr_use
        t_end = t_sim1 + take_use
        timeline.append({**seg, "t0": t0, "t_call1": t_call1, "t_sim1": t_sim1, "t_end": t_end})
        narr_blocks.append(
            f"[{srt_ts(t_call1)} - {srt_ts(t_sim1)}] {seg['title']}\n{seg['narration']}\n{seg['takeaway']}\n"
        )
        t_cursor = t_end
        print(f"  narr={narr_dur:.1f}s take={take_dur:.1f}s fycal_pip={has_fycal}", flush=True)

    narr_path = ROOT / "旁白文案_原理讲解版.txt"
    narr_path.write_text("\n".join(narr_blocks), encoding="utf-8")

    srt_lines, idx = [], 1
    for item in timeline:
        srt_lines += [str(idx), f"{srt_ts(item['t0'])} --> {srt_ts(item['t_call1'])}", item["title"] + "\n" + item["part_note"], ""]
        idx += 1
        for a, b, text in split_cues(item["narration"], item["t_call1"], item["t_sim1"]):
            srt_lines += [str(idx), f"{srt_ts(a)} --> {srt_ts(b)}", "\n".join(textwrap.wrap(text, 28)), ""]
            idx += 1
        srt_lines += [str(idx), f"{srt_ts(item['t_sim1'])} --> {srt_ts(item['t_end'])}", item["takeaway"], ""]
        idx += 1
    srt_path = OUT / "FY301_原理讲解版.srt"
    srt_path.write_text("\n".join(srt_lines), encoding="utf-8")

    vlist = BUILD / "vconcat.txt"
    vlist.write_text("\n".join(f"file '{p.resolve().as_posix()}'" for p in video_parts), encoding="utf-8")
    silent = BUILD / "silent.mp4"
    run([FF, "-y", "-f", "concat", "-safe", "0", "-i", str(vlist), "-c:v", "libx264", "-pix_fmt", "yuv420p", "-r", str(FPS), str(silent)])

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
    final = OUT / "FY301_原理讲解版.mp4"
    run(
        [
            FF, "-y", "-i", str(silent), "-i", str(voice),
            "-vf", f"subtitles='{srt_esc}':force_style='FontName=Microsoft YaHei,FontSize=17,PrimaryColour=&H00FFFFFF&,OutlineColour=&H80000000&,Outline=2,Shadow=1,MarginV=26'",
            "-c:v", "libx264", "-pix_fmt", "yuv420p",
            "-c:a", "aac", "-b:a", "128k", "-shortest", str(final),
        ]
    )
    print("DONE", final, f"duration={probe_duration(final):.1f}s", flush=True)


if __name__ == "__main__":
    main()
