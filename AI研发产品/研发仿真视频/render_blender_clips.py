# -*- coding: utf-8 -*-
"""
Render optional Blender enhancement clips for FY301 principle edition.

P3 clips:
  01 piezo bend
  02 nozzle-flapper pilot
  03 spool valve

Usage:
  python render_blender_clips.py
  python render_blender_clips.py --only 02
  python render_blender_clips.py --blender "C:\\Program Files\\Blender Foundation\\Blender 4.2\\blender.exe"
"""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT_BLEND = ROOT / "out" / "blender"
HUD_DIR = OUT_BLEND / "_hud"
STORYBOARD = ROOT / "storyboard.json"

SCRIPTS = {
    "01": {
        "script": ROOT / "blender" / "render_piezo_bend.py",
        "out": OUT_BLEND / "01_压电陶瓷原理.mp4",
        "photos": [
            ROOT / "out/_fycal_figs/_named/fig16_cleaning_piezo.png",
            ROOT / "out/_fycal_figs/_named/fig18_exploded_piezo.png",
        ],
        "hud_fallback": ["0-100 V", "target ~50 V", "normal 30-70 V"],
    },
    "03": {
        "script": ROOT / "blender" / "render_spool_valve.py",
        "out": OUT_BLEND / "03_膜片放大与滑阀.mp4",
        "photos": [
            ROOT / "out/_excel_parts/33_r40_膜片.png",
            ROOT / "out/_excel_parts/36_r43_滑阀.png",
        ],
        "hud_fallback": ["force balance", "OUT1 / OUT2", "fail-safe"],
    },
    "02": {
        "script": ROOT / "blender" / "render_nozzle_flapper.py",
        "out": OUT_BLEND / "02_喷嘴挡板先导级.mp4",
        "photos": [
            ROOT / "out/_fycal_figs/_named/fig12_cal_on_block.png",
            ROOT / "out/_fycal_figs/_named/fig10_supply_piezo.png",
        ],
        "hud_fallback": ["FYCAL @20 psi", "0V <= 2", "50V ~ 6", "100V ~ 12-13"],
    },
}


def find_blender(explicit: str | None) -> Path:
    if explicit:
        p = Path(explicit)
        if not p.exists():
            raise SystemExit(f"Blender not found: {p}")
        return p
    which = shutil.which("blender")
    if which:
        return Path(which)
    candidates = [
        Path(r"C:\Program Files\Blender Foundation\Blender 4.4\blender.exe"),
        Path(r"C:\Program Files\Blender Foundation\Blender 4.3\blender.exe"),
        Path(r"C:\Program Files\Blender Foundation\Blender 4.2\blender.exe"),
        Path(r"C:\Program Files\Blender Foundation\Blender 4.1\blender.exe"),
        Path(r"C:\Program Files\Blender Foundation\Blender 4.0\blender.exe"),
        Path(r"C:\Program Files\Blender Foundation\Blender 3.6\blender.exe"),
        Path("/usr/bin/blender"),
        Path("/snap/bin/blender"),
    ]
    for p in candidates:
        if p.exists():
            return p
    raise SystemExit(
        "Blender executable not found. Install Blender 3.6+ and either add it to PATH "
        "or pass --blender \"C:\\Program Files\\Blender Foundation\\Blender 4.2\\blender.exe\""
    )


def hud_lines_for(seg_id: str) -> list[str]:
    if STORYBOARD.exists():
        data = json.loads(STORYBOARD.read_text(encoding="utf-8"))
        for seg in data.get("segments") or []:
            if seg.get("id") == seg_id:
                hud = list(seg.get("hud") or [])
                if hud:
                    return hud
    return list(SCRIPTS[seg_id]["hud_fallback"])


def bake_hud_png(seg_id: str) -> Path:
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ImportError as e:
        raise SystemExit("Pillow required to bake Blender HUD cards: pip install pillow") from e

    HUD_DIR.mkdir(parents=True, exist_ok=True)
    path = HUD_DIR / f"hud_{seg_id}.png"
    lines = hud_lines_for(seg_id)
    w, h = 720, 280
    img = Image.new("RGBA", (w, h), (15, 23, 42, 230))
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    for cand in (
        Path(r"C:\Windows\Fonts\msyh.ttc"),
        Path("/usr/share/fonts/truetype/wqy/wqy-microhei.ttc"),
        Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
    ):
        if cand.exists():
            try:
                font = ImageFont.truetype(str(cand), 28)
                break
            except OSError:
                pass
    y = 24
    draw.text((24, y), f"FY301 / seg {seg_id}", font=font, fill=(148, 163, 184, 255))
    y += 44
    for text in lines:
        bbox = draw.textbbox((0, 0), text, font=font)
        tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
        box = [24, y, 24 + tw + 28, y + th + 16]
        try:
            draw.rounded_rectangle(box, radius=10, fill=(30, 41, 59, 255), outline=(79, 195, 247, 255), width=2)
        except AttributeError:
            draw.rectangle(box, fill=(30, 41, 59, 255), outline=(79, 195, 247, 255), width=2)
        draw.text((38, y + 6), text, font=font, fill=(232, 238, 247, 255))
        y = box[3] + 12
    img.save(path)
    return path


def run_one(blender: Path, key: str, frames: int, fps: int) -> None:
    item = SCRIPTS[key]
    script = item["script"]
    out = item["out"]
    if not script.exists():
        raise SystemExit(f"missing script: {script}")
    out.parent.mkdir(parents=True, exist_ok=True)
    hud = bake_hud_png(key)
    photos = [p for p in item["photos"] if Path(p).exists()]
    cmd = [
        str(blender),
        "--background",
        "--python",
        str(script),
        "--",
        "--out",
        str(out),
        "--frames",
        str(frames),
        "--fps",
        str(fps),
        "--hud",
        str(hud),
    ]
    if len(photos) >= 1:
        cmd += ["--photo-a", str(photos[0])]
    if len(photos) >= 2:
        cmd += ["--photo-b", str(photos[1])]
    print("+", " ".join(cmd), flush=True)
    r = subprocess.run(cmd, cwd=str(ROOT))
    if r.returncode != 0:
        raise SystemExit(f"Blender render failed for segment {key} (exit {r.returncode})")
    if not out.exists() or out.stat().st_size < 1000:
        raise SystemExit(f"Blender output missing/too small: {out}")
    print(f"OK: {out} ({out.stat().st_size} bytes)", flush=True)


def main() -> int:
    ap = argparse.ArgumentParser(description="Render FY301 Blender enhancement clips")
    ap.add_argument("--blender", default=None, help="Path to blender executable")
    ap.add_argument("--only", choices=sorted(SCRIPTS), help="Render only one segment id")
    ap.add_argument("--frames", type=int, default=120)
    ap.add_argument("--fps", type=int, default=20)
    ap.add_argument("--dry-run", action="store_true", help="Locate scripts, bake HUD; Blender optional")
    args = ap.parse_args()

    keys = [args.only] if args.only else sorted(SCRIPTS)
    blender = None
    try:
        blender = find_blender(args.blender)
        print(f"blender: {blender}", flush=True)
    except SystemExit as e:
        if not args.dry_run:
            raise
        print(f"warn: {e}", flush=True)

    for k in keys:
        print(f"script[{k}]: {SCRIPTS[k]['script']}", flush=True)
        print(f"out[{k}]: {SCRIPTS[k]['out']}", flush=True)
        hud = bake_hud_png(k)
        print(f"hud[{k}]: {hud}", flush=True)
        for photo in SCRIPTS[k]["photos"]:
            print(
                f"photo[{k}]: {photo.name} ({'ok' if Path(photo).exists() else 'MISSING'})",
                flush=True,
            )
    if args.dry_run:
        print("DONE (dry-run)")
        return 0
    assert blender is not None
    for k in keys:
        run_one(blender, k, args.frames, args.fps)
    print("ALL BLENDER CLIPS DONE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
