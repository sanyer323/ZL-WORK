# -*- coding: utf-8 -*-
"""
Render optional Blender enhancement clips for FY301 principle edition.

Default targets (P3 first slice):
  - segment 01 piezo bend  -> out/blender/01_压电陶瓷原理.mp4
  - segment 03 spool valve -> out/blender/03_膜片放大与滑阀.mp4

Usage:
  python render_blender_clips.py
  python render_blender_clips.py --blender "C:\\Program Files\\Blender Foundation\\Blender 4.2\\blender.exe"
  python render_blender_clips.py --only 01
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT_BLEND = ROOT / "out" / "blender"
SCRIPTS = {
    "01": {
        "script": ROOT / "blender" / "render_piezo_bend.py",
        "out": OUT_BLEND / "01_压电陶瓷原理.mp4",
    },
    "03": {
        "script": ROOT / "blender" / "render_spool_valve.py",
        "out": OUT_BLEND / "03_膜片放大与滑阀.mp4",
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


def run_one(blender: Path, key: str, frames: int, fps: int) -> None:
    item = SCRIPTS[key]
    script = item["script"]
    out = item["out"]
    if not script.exists():
        raise SystemExit(f"missing script: {script}")
    out.parent.mkdir(parents=True, exist_ok=True)
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
    ]
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
    ap.add_argument("--dry-run", action="store_true", help="Only locate Blender + scripts")
    args = ap.parse_args()

    blender = find_blender(args.blender)
    print(f"blender: {blender}", flush=True)
    keys = [args.only] if args.only else list(SCRIPTS)
    for k in keys:
        print(f"script[{k}]: {SCRIPTS[k]['script']}", flush=True)
        print(f"out[{k}]: {SCRIPTS[k]['out']}", flush=True)
    if args.dry_run:
        print("DONE (dry-run)")
        return 0
    for k in keys:
        run_one(blender, k, args.frames, args.fps)
    print("ALL BLENDER CLIPS DONE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
