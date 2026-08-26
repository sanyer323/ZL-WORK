# -*- coding: utf-8 -*-
"""Verify FY301 principle-edition assets without rendering/TTS."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "out"
PARTS = OUT / "_excel_parts"
FYCAL_FIGS = OUT / "_fycal_figs" / "_named"
FYCAL_MANIFEST_PATH = FYCAL_FIGS / "manifest.json"
BUILD_SCRIPT = ROOT / "build_principle_edition.py"


def parse_segments_fycal_and_parts(src: str) -> list[dict]:
    """Lightweight parse of SEGMENTS image refs without importing build deps."""
    # Extract fycal_imgs tuples and parts lists from SEGMENTS block.
    block_m = re.search(r"SEGMENTS\s*=\s*\[(.*?)\n\]\n", src, re.S)
    if not block_m:
        raise RuntimeError("SEGMENTS not found in build_principle_edition.py")
    block = block_m.group(1)
    segs = []
    for seg_m in re.finditer(r"\{\s*\"id\":\s*\"(.*?)\"(.*?)(?=\n\s*\{\s*\"id\":|\Z)", block, re.S):
        sid = seg_m.group(1)
        body = seg_m.group(2)
        parts = re.findall(r"\"parts\":\s*\[(.*?)\]", body, re.S)
        part_labels = []
        if parts:
            part_labels = re.findall(r"\"([^\"]+)\"", parts[0])
        fycal = re.findall(r"\(\s*\"([^\"]+\.png)\"\s*,\s*\"[^\"]*\"\s*\)", body)
        segs.append({"id": sid, "parts": part_labels, "fycal": fycal})
    return segs


def main() -> int:
    errors: list[str] = []
    src = BUILD_SCRIPT.read_text(encoding="utf-8")
    segs = parse_segments_fycal_and_parts(src)

    parts_man = []
    if PARTS.joinpath("manifest.json").exists():
        parts_man = json.loads((PARTS / "manifest.json").read_text(encoding="utf-8"))
    by_label = {m["label"]: m for m in parts_man}

    fycal_man: dict[str, dict] = {}
    if not FYCAL_MANIFEST_PATH.exists():
        errors.append(f"missing {FYCAL_MANIFEST_PATH}")
    else:
        raw = json.loads(FYCAL_MANIFEST_PATH.read_text(encoding="utf-8"))
        for row in raw:
            f = str(row.get("file", ""))
            if Path(f).is_absolute() or ":\\" in f or f.startswith("\\\\") or re.match(r"^[A-Za-z]:/", f):
                errors.append(f"absolute path in FYCAL manifest: {f}")
            rel = Path(f).name
            if not rel:
                continue
            fycal_man[rel] = row
            if not (FYCAL_FIGS / rel).exists():
                errors.append(f"manifest file missing on disk: {rel}")

    if "fig14_piezo_base_labeled.png" not in fycal_man:
        errors.append("manifest missing fig14_piezo_base_labeled.png")
    if not (FYCAL_FIGS / "fig14_piezo_base_labeled.png").exists():
        errors.append("disk missing fig14_piezo_base_labeled.png")

    for seg in segs:
        for lab in seg["parts"]:
            m = by_label.get(lab)
            if not m:
                errors.append(f"segment {seg['id']} unknown part label: {lab}")
                continue
            p = PARTS / m["file"]
            if not p.exists():
                errors.append(f"segment {seg['id']} missing part image: {p.name}")
        for fname in seg["fycal"]:
            p = FYCAL_FIGS / Path(fname).name
            if not p.exists():
                errors.append(f"segment {seg['id']} missing FYCAL image: {p.name}")
            elif p.name not in fycal_man:
                errors.append(f"segment {seg['id']} FYCAL image not in manifest: {p.name}")

    if errors:
        print("FAIL")
        for e in errors:
            print(" -", e)
        return 1

    print(
        "OK: FY301 principle assets consistent "
        f"({len(segs)} segments, {len(fycal_man)} FYCAL manifest entries, relative paths)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
