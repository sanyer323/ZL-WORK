# -*- coding: utf-8 -*-
"""Rebuild out/_fycal_figs/_named/manifest.json with relative filenames only."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
NAMED = ROOT / "out" / "_fycal_figs" / "_named"
OUT = NAMED / "manifest.json"

# Keep known handbook source tags when regenerating.
SRC_HINTS = {
    "fig10_supply_piezo.png": "p10_00_xref54.png",
    "fig12_cal_on_block.png": "p12_01_xref71.png",
    "fig13_fycal_panel.png": "p14_00_xref80.png",
    "fig14_piezo_on_fycal.png": "p14_01_xref81.png",
    "fig15_helmet_a.png": "p15_00_xref85.png",
    "fig16_cleaning_piezo.png": "p16_00_xref94.png",
    "fig16_cleaning_piezo_b.png": "p16_01_xref95.png",
    "fig17_reassemble_a.png": "p17_00_xref99.png",
    "fig17_reassemble_b.png": "p17_02_xref101.png",
    "fig17_reassemble_c.png": "p17_03_xref102.png",
    "fig18_exploded_piezo.png": "p17_01_xref100.png",
}


def main() -> None:
    rows = []
    for png in sorted(NAMED.glob("*.png")):
        rows.append(
            {
                "id": png.stem,
                "file": png.name,
                "src": SRC_HINTS.get(png.name, png.name),
            }
        )
    OUT.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"OK: {OUT} ({len(rows)} entries, relative paths only)")


if __name__ == "__main__":
    main()
