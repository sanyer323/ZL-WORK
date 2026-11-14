# -*- coding: utf-8 -*-
"""Rebuild parts_index.json with portable relative paths (no Windows absolute paths)."""
from __future__ import annotations

import json
from pathlib import Path

from fy301_common import PARTS_INDEX, ROOT, SKD_DIR

IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tif", ".tiff"}


def main() -> int:
    if not SKD_DIR.is_dir():
        print(f"FAIL: SKD folder missing: {SKD_DIR}")
        print("Place FY301 SKD photos at AI研发产品/SMAR SKD/ then rerun.")
        return 1

    rows: dict[str, dict] = {}
    i = 0
    for p in sorted(SKD_DIR.rglob("*")):
        if not p.is_file() or p.suffix.lower() not in IMAGE_EXTS:
            continue
        rel = p.relative_to(SKD_DIR).as_posix()
        rows[str(i)] = {
            "rel": rel,
            "name": p.name,
            "path": f"../SMAR SKD/{rel}",
        }
        i += 1

    PARTS_INDEX.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"OK: wrote {len(rows)} entries -> {PARTS_INDEX}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
