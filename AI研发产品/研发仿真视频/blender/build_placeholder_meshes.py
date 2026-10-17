# -*- coding: utf-8 -*-
"""Generate replaceable placeholder OBJ meshes for FY301 Blender clips (no Blender needed)."""
from __future__ import annotations

import json
import math
from pathlib import Path

OUT = Path(__file__).resolve().parent / "meshes"
OUT.mkdir(parents=True, exist_ok=True)


def write_obj(path: Path, verts: list[tuple[float, float, float]], faces: list[list[int]], name: str) -> None:
    lines = [f"# FY301 placeholder mesh: {name}", f"o {name}"]
    for x, y, z in verts:
        lines.append(f"v {x:.6f} {y:.6f} {z:.6f}")
    for f in faces:
        lines.append("f " + " ".join(str(i) for i in f))
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"OK: {path.name}  v={len(verts)} f={len(faces)}")


def cylinder(radius: float, depth: float, segments: int = 32, z0: float = 0.0):
    """Return (verts, faces) with 1-based face indices."""
    verts: list[tuple[float, float, float]] = []
    faces: list[list[int]] = []
    z_bot, z_top = z0 - depth / 2, z0 + depth / 2
    verts.append((0.0, 0.0, z_bot))  # 1
    verts.append((0.0, 0.0, z_top))  # 2
    for i in range(segments):
        a = 2 * math.pi * i / segments
        x, y = radius * math.cos(a), radius * math.sin(a)
        verts.append((x, y, z_bot))  # 3 + 2*i
        verts.append((x, y, z_top))  # 4 + 2*i
    for i in range(segments):
        b0 = 3 + 2 * i
        t0 = 4 + 2 * i
        b1 = 3 + 2 * ((i + 1) % segments)
        t1 = 4 + 2 * ((i + 1) % segments)
        faces.append([1, b0, b1])
        faces.append([2, t1, t0])
        faces.append([b0, t0, t1, b1])
    return verts, faces


def cone(r1: float, r2: float, depth: float, segments: int = 32):
    verts: list[tuple[float, float, float]] = []
    faces: list[list[int]] = []
    z0, z1 = -depth / 2, depth / 2
    verts.append((0.0, 0.0, z0))
    verts.append((0.0, 0.0, z1))
    for i in range(segments):
        a = 2 * math.pi * i / segments
        c, s = math.cos(a), math.sin(a)
        verts.append((r1 * c, r1 * s, z0))
        verts.append((r2 * c, r2 * s, z1))
    for i in range(segments):
        b0 = 3 + 2 * i
        t0 = 4 + 2 * i
        b1 = 3 + 2 * ((i + 1) % segments)
        t1 = 4 + 2 * ((i + 1) % segments)
        faces.append([1, b0, b1])
        faces.append([2, t1, t0])
        faces.append([b0, t0, t1, b1])
    return verts, faces


def box(w: float, d: float, h: float):
    x, y, z = w / 2, d / 2, h / 2
    verts = [
        (-x, -y, -z),
        (x, -y, -z),
        (x, y, -z),
        (-x, y, -z),
        (-x, -y, z),
        (x, -y, z),
        (x, y, z),
        (-x, y, z),
    ]
    faces = [
        [1, 2, 3, 4],
        [5, 8, 7, 6],
        [1, 5, 6, 2],
        [2, 6, 7, 3],
        [3, 7, 8, 4],
        [4, 8, 5, 1],
    ]
    return verts, faces


def main() -> None:
    catalog = {
        "piezo_disk.obj": cylinder(0.55, 0.045, 64),
        "nozzle_body.obj": cone(0.16, 0.045, 0.35, 32),
        "restriction_tube.obj": cylinder(0.09, 0.7, 32),
        "flapper_disk.obj": cylinder(0.28, 0.03, 48),
        "sleeve.obj": cylinder(0.28, 1.4, 48),
        "spool.obj": cylinder(0.18, 0.95, 48),
        "diaphragm_large.obj": cylinder(0.62, 0.04, 48),
        "diaphragm_small.obj": cylinder(0.38, 0.04, 48),
        "hall_housing.obj": box(0.55, 0.35, 0.25),
        "magnet_block.obj": box(0.18, 0.12, 0.12),
        # segment 05 signal-flow nodes (replace with real CAD exports)
        "pcb_board.obj": box(1.1, 0.08, 0.7),
        "pneumatic_block.obj": box(0.9, 0.55, 0.45),
        "actuator_hint.obj": cylinder(0.22, 0.9, 32),
    }
    manifest = []
    for name, (verts, faces) in catalog.items():
        write_obj(OUT / name, verts, faces, Path(name).stem)
        manifest.append(
            {
                "file": name,
                "replace_with": "Export real CAD mesh to this same filename (OBJ/STL/FBX supported by importer).",
            }
        )
    (OUT / "manifest.json").write_text(
        json.dumps(
            {
                "note": "Replace any file with a real CAD export using the same stem; Blender clips auto-import when present.",
                "meshes": manifest,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print(f"DONE -> {OUT}")


if __name__ == "__main__":
    main()
