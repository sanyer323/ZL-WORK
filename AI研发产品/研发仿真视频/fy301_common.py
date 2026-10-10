# -*- coding: utf-8 -*-
"""Shared FY301 video pipeline helpers (paths, sim resolution, CJK fonts, ffprobe)."""
from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "out"
STORYBOARD_PATH = ROOT / "storyboard.json"
PARTS_INDEX = ROOT / "parts_index.json"
SKD_DIR = ROOT.parent / "SMAR SKD"

CJK_FONT_CANDIDATES = [
    Path(r"C:\Windows\Fonts\msyh.ttc"),
    Path(r"C:\Windows\Fonts\simhei.ttf"),
    Path("/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc"),
    Path("/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"),
    Path("/usr/share/fonts/truetype/wqy/wqy-microhei.ttc"),
    Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
]


def cjk_font_path() -> Path | None:
    for p in CJK_FONT_CANDIDATES:
        if p.exists():
            return p
    return None


def ffmpeg_fontfile_esc() -> str:
    p = cjk_font_path()
    if p is None:
        return r"C\:/Windows/Fonts/msyh.ttc"
    return str(p.resolve()).replace("\\", "/").replace(":", "\\:")


def subtitle_force_style(font_name: str = "Microsoft YaHei", font_size: int = 17) -> str:
  # Prefer installed CJK font name when we can resolve a file.
    p = cjk_font_path()
    if p and "wqy" in p.name.lower():
        font_name = "WenQuanYi Micro Hei"
    elif p and "noto" in p.name.lower():
        font_name = "Noto Sans CJK SC"
    return (
        f"FontName={font_name},FontSize={font_size},"
        "PrimaryColour=&H00FFFFFF&,OutlineColour=&H80000000&,Outline=2,Shadow=1,MarginV=26"
    )


def find_sim(name: str, *, prefer_blender: bool = True, out_dir: Path | None = None) -> Path:
    """Resolve simulation clip; prefer optional Blender enhancement when present."""
    out = out_dir or OUT
    blender_p = out / "blender" / name
    plain_p = out / name
    if prefer_blender and blender_p.exists() and blender_p.stat().st_size > 1000:
        print(f"sim prefer blender: {blender_p.name}", flush=True)
        return blender_p
    if plain_p.exists() and plain_p.stat().st_size > 1000:
        return plain_p
    cands = [p for p in out.glob(name[:2] + "*.mp4") if p.is_file()]
    blend_dir = out / "blender"
    blend_cands = [p for p in blend_dir.glob(name[:2] + "*.mp4") if p.is_file()] if blend_dir.exists() else []
    if prefer_blender and blend_cands:
        print(f"sim prefer blender: {blend_cands[0].name}", flush=True)
        return blend_cands[0]
    if not cands:
        raise FileNotFoundError(name)
    return cands[0]


def probe_duration(path: Path, ff: str | None = None) -> float:
    if not path.exists():
        return 0.0
    if ff is None:
        try:
            import imageio_ffmpeg

            ff = imageio_ffmpeg.get_ffmpeg_exe()
        except Exception:
            ff = "ffmpeg"
    r = subprocess.run([ff, "-i", str(path)], capture_output=True, text=True, encoding="utf-8", errors="replace")
    m = re.search(r"Duration:\s*(\d+):(\d+):(\d+\.\d+)", r.stderr or "")
    if not m:
        return 0.0
    return int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3))


def load_storyboard(path: Path | None = None) -> dict:
    p = path or STORYBOARD_PATH
    return json.loads(p.read_text(encoding="utf-8"))


def resolve_indexed_asset(name: str, index_path: Path | None = None) -> Path | None:
    """Resolve SKD / parts_index entry to an on-disk path (portable)."""
    idx_path = index_path or PARTS_INDEX
    if not idx_path.exists():
        return None
    data = json.loads(idx_path.read_text(encoding="utf-8"))
    for row in data.values():
        if not isinstance(row, dict):
            continue
        if row.get("name") != name and row.get("rel") != name:
            continue
        rel = row.get("rel") or name
        for cand in (
            SKD_DIR / rel,
            ROOT / rel,
            Path(str(row.get("path", ""))),
        ):
            if cand.exists():
                return cand.resolve()
    # fallback: scan SKD folder by basename
    if SKD_DIR.exists():
        hits = list(SKD_DIR.glob(f"**/{name}"))
        if hits:
            return hits[0].resolve()
    return None


def load_parts_index(index_path: Path | None = None) -> dict[str, Path]:
    """name -> resolved Path for all index entries that exist on disk."""
    idx_path = index_path or PARTS_INDEX
    out: dict[str, Path] = {}
    if not idx_path.exists():
        return out
    data = json.loads(idx_path.read_text(encoding="utf-8"))
    for row in data.values():
        if not isinstance(row, dict):
            continue
        name = str(row.get("name") or "")
        if not name:
            continue
        p = resolve_indexed_asset(name, idx_path)
        if p is not None:
            out[name] = p
    return out
