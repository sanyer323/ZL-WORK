# -*- coding: utf-8 -*-
"""Gate: default FY301 deliverable must be principle edition, not troubleshooting edition."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
STORYBOARD = ROOT / "storyboard.json"
README = ROOT / "README.md"


def main() -> int:
    errors: list[str] = []
    data = json.loads(STORYBOARD.read_text(encoding="utf-8"))
    out = data.get("output") or {}
    principle = str(out.get("principle_mp4") or "")
    if "原理讲解版" not in principle:
        errors.append(f"storyboard output.principle_mp4 must be principle edition, got: {principle!r}")
    if "工程师" in principle or "培训" in principle and "原理" not in principle:
        errors.append(f"default deliverable looks like engineer/troubleshooting edition: {principle!r}")

    readme = README.read_text(encoding="utf-8") if README.exists() else ""
    if "原理讲解版" not in readme:
        errors.append("README missing principle-edition guidance")
    if "工程师培训版" in readme and "原理讲解版" in readme:
        # ok if both mentioned; ensure principle is recommended
        if "推荐" not in readme and "默认" not in readme:
            errors.append("README should mark principle edition as recommended/default")

    # Blender mesh pack presence (placeholders or real CAD replacements)
    mesh_dir = ROOT / "blender" / "meshes"
    required = [
        "piezo_disk.obj",
        "spool.obj",
        "hall_housing.obj",
        "pcb_board.obj",
        "pneumatic_block.obj",
        "actuator_hint.obj",
        "manifest.json",
    ]
    for name in required:
        if not (mesh_dir / name).exists():
            errors.append(f"missing mesh pack file: blender/meshes/{name} (run build_placeholder_meshes.py)")

    if errors:
        print("FAIL")
        for e in errors:
            print(" -", e)
        return 1
    print("OK: default deliverable is principle edition; mesh pack present")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
