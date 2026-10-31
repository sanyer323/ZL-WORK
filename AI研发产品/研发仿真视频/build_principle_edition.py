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
    weak_side: list[str] = []

    if FYCAL_MANIFEST_PATH.exists():
        raw = json.loads(FYCAL_MANIFEST_PATH.read_text(encoding="utf-8"))
        for row in raw:
            f = str(row.get("file", ""))
            if Path(f).is_absolute() or ":\\" in f or f.startswith("\\\\"):
                abs_in_manifest.append(f)

    for seg in SEGMENTS:
        for lab in seg.get("parts") or []:
            try:
                p = part(lab)
            except KeyError:
                missing_files.append(f"unknown part label: {lab}")
                continue
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
        side = side_images(seg)
        if len(side) < 2:
            weak_side.append(seg["id"])
        else:
            print(
                f"side panel ok: {seg['id']} x{len(side)} "
                f"hud={len(seg.get('hud') or [])}",
                flush=True,
            )
        if not (seg.get("hud") or []):
            print(f"warn: segment {seg['id']} has empty hud badges", flush=True)

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
    if weak_side:
        raise SystemExit(
            "Segments need >=2 side-panel images (FYCAL or parts):\n  "
            + ", ".join(weak_side)
        )

STORYBOARD_PATH = ROOT / "storyboard.json"


def normalize_segment(seg: dict) -> dict:
    """JSON storyboard → runtime segment (fycal_imgs as list[tuple])."""
    out = dict(seg)
    imgs = []
    for item in out.get("fycal_imgs") or []:
        if isinstance(item, dict):
            imgs.append((item["file"], item.get("caption") or item["file"]))
        elif isinstance(item, (list, tuple)) and len(item) >= 2:
            imgs.append((str(item[0]), str(item[1])))
        else:
            raise ValueError(f"bad fycal_imgs item in segment {out.get('id')}: {item!r}")
    out["fycal_imgs"] = imgs
    out["parts"] = list(out.get("parts") or [])
    out["hud"] = list(out.get("hud") or [])
    out["photo_beats"] = list(out.get("photo_beats") or [])
    return out


def load_segments(path: Path | None = None) -> list[dict]:
    p = path or STORYBOARD_PATH
    if not p.exists():
        raise FileNotFoundError(f"storyboard missing: {p}")
    data = json.loads(p.read_text(encoding="utf-8"))
    segs = data["segments"] if isinstance(data, dict) else data
    if not isinstance(segs, list) or not segs:
        raise ValueError(f"storyboard has no segments: {p}")
    return [normalize_segment(s) for s in segs]


SEGMENTS = load_segments()


def font(size: int):
    candidates = [
        Path(r"C:\Windows\Fonts\msyh.ttc"),
        Path(r"C:\Windows\Fonts\simhei.ttf"),
        Path("/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc"),
        Path("/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"),
        Path("/usr/share/fonts/truetype/wqy/wqy-microhei.ttc"),
        Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
    ]
    for p in candidates:
        if p.exists():
            try:
                return ImageFont.truetype(str(p), size)
            except OSError:
                continue
    return ImageFont.load_default()


def part_meta(label: str) -> dict:
    m = BY_LABEL.get(label)
    if not m:
        for k, v in BY_LABEL.items():
            if label in k or k in label:
                m = v
                break
    if not m:
        raise KeyError(label)
    return m


def part(label: str) -> Path:
    return PARTS / part_meta(label)["file"]


def side_images(seg: dict) -> list[tuple[Path, str]]:
    """Right-rail images: prefer FYCAL handbook photos, else Excel part photos."""
    items: list[tuple[Path, str]] = []
    for fname, cap in seg.get("fycal_imgs") or []:
        items.append((fycal_path(fname), cap))
    if items:
        return items
    for lab in seg.get("parts") or []:
        meta = part_meta(lab)
        no = meta.get("part_no")
        prefix = f"#{no} " if no not in (None, "") else ""
        items.append((part(lab), f"{prefix}{lab}"))
    return items


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


def find_sim(name: str, prefer_blender: bool = True) -> Path:
    """Resolve simulation clip; prefer optional Blender enhancement when present."""
    blender_p = OUT / "blender" / name
    plain_p = OUT / name
    if prefer_blender and blender_p.exists() and blender_p.stat().st_size > 1000:
        print(f"sim prefer blender: {blender_p.name}", flush=True)
        return blender_p
    if plain_p.exists() and plain_p.stat().st_size > 1000:
        return plain_p
    cands = [p for p in OUT.glob(name[:2] + "*.mp4") if p.is_file()]
    blend_cands = [p for p in (OUT / "blender").glob(name[:2] + "*.mp4") if p.is_file()] if (OUT / "blender").exists() else []
    if prefer_blender and blend_cands:
        print(f"sim prefer blender: {blend_cands[0].name}", flush=True)
        return blend_cands[0]
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
    images: list[tuple[Path, str]],
    duration: float,
    out_mp4: Path,
    beats: list[float] | None = None,
    panel_title: str = "实物图（全程）",
) -> None:
    """右侧照片栏视频：多张全程可见，按旁白节拍高亮并 Ken Burns。"""
    n_frames = max(2, int(duration * FPS))
    imgs = []
    caps = []
    for path, cap in images:
        imgs.append(Image.open(path).convert("RGB"))
        caps.append(cap)
    n = len(imgs)
    panel_h = H
    panel_w = STRIP_W
    gap = 8
    cell_h = (panel_h - 50 - gap * (n + 1)) // max(n, 1)

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
        draw.text((10, 10), panel_title, font=font(14), fill=(148, 163, 184))

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


def make_hud_overlay_png(badges: list[str], path: Path) -> None:
    """Top-left key-number chips burned onto principle shots."""
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    x, y = 18, 18
    for text in badges:
        f = font(18)
        bbox = draw.textbbox((0, 0), text, font=f)
        tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
        pad_x, pad_y = 12, 7
        box = [x, y, x + tw + pad_x * 2, y + th + pad_y * 2]
        try:
            draw.rounded_rectangle(box, radius=8, fill=(15, 23, 42, 210), outline=(79, 195, 247, 255), width=2)
        except AttributeError:
            draw.rectangle(box, fill=(15, 23, 42, 210), outline=(79, 195, 247, 255), width=2)
        draw.text((x + pad_x, y + pad_y - 1), text, font=f, fill=(232, 238, 247, 255))
        y = box[3] + 8
    img.save(path)


def burn_hud(src_mp4: Path, dst_mp4: Path, badges: list[str], duration: float) -> None:
    if not badges:
        if src_mp4.resolve() != dst_mp4.resolve():
            run([FF, "-y", "-i", str(src_mp4), "-c", "copy", str(dst_mp4)])
        return
    overlay = BUILD / (dst_mp4.stem + "_hud.png")
    make_hud_overlay_png(badges, overlay)
    run(
        [
            FF, "-y",
            "-i", str(src_mp4),
            "-i", str(overlay),
            "-filter_complex", "overlay=0:0",
            "-t", f"{duration:.3f}",
            "-c:v", "libx264", "-pix_fmt", "yuv420p", "-preset", "fast",
            str(dst_mp4),
        ]
    )


def compose_sim_with_photos(
    sim_mp4: Path,
    images: list[tuple[Path, str]],
    duration: float,
    out_mp4: Path,
    beats: list[float] | None = None,
    panel_title: str = "实物图（全程）",
    badges: list[str] | None = None,
) -> None:
    """左侧原理动画 + 右侧全程可见、会动的实物照片栏 + 关键数角标。"""
    panel = BUILD / (out_mp4.stem + "_panel.mp4")
    stacked = BUILD / (out_mp4.stem + "_stacked.mp4")
    print(f"  photo panel {duration:.1f}s ...", flush=True)
    make_animated_photo_panel(images, duration, panel, beats=beats, panel_title=panel_title)
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
            str(stacked),
        ]
    )
    burn_hud(stacked, out_mp4, badges or [], duration)


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
        side = side_images(seg)
        badges = list(seg.get("hud") or [])
        has_side = len(side) >= 2
        if has_side:
            # 讲解全程：左原理 + 右实物栏（FYCAL 或 Excel 零件）+ 关键数角标
            compose_sim_with_photos(
                sim_raw,
                side,
                narr_use,
                sim_mp4,
                beats=seg.get("photo_beats"),
                panel_title=seg.get("panel_title") or "实物图（全程）",
                badges=badges,
            )
            # 开场用同一套图短指认（可选，缩短以免重复感）
            make_callout_png(seg, call_png)
            png_to_video(call_png, call_mp4, 2.5)
            call_dur_i = 2.5
        else:
            make_callout_png(seg, call_png)
            png_to_video(call_png, call_mp4, CALL_DUR)
            full = BUILD / f"simfull_{i}.mp4"
            run([FF, "-y", "-i", str(sim_raw), "-c", "copy", str(full)])
            burn_hud(full, sim_mp4, badges, narr_use)
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
        print(
            f"  narr={narr_dur:.1f}s take={take_dur:.1f}s "
            f"side_panel={has_side} hud={len(badges)}",
            flush=True,
        )

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
