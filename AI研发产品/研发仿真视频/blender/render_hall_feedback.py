# -*- coding: utf-8 -*-
"""FY301 Blender clip 04: Hall feedback gap + magnet motion + part photos."""
from __future__ import annotations

import math
import sys
from pathlib import Path

_BLEND_DIR = Path(__file__).resolve().parent
if str(_BLEND_DIR) not in sys.path:
    sys.path.insert(0, str(_BLEND_DIR))

from fy301_blend_utils import (  # noqa: E402
    add_camera,
    add_hud_image_plane,
    add_image_plane,
    add_root_to_syspath,
    import_mesh,
    make_material,
    parse_common_argv,
    reset_dark_scene,
)


def main() -> None:
    import bpy

    root = add_root_to_syspath(__file__)
    args = parse_common_argv(sys.argv)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    reset_dark_scene(args.res_x, args.res_y, args.fps, args.frames, out)

    mat_house = make_material("HallHousing", (0.55, 0.60, 0.68), metallic=0.7, roughness=0.35)
    mat_mag = make_material("Magnet", (0.75, 0.20, 0.18), metallic=0.2, roughness=0.45)
    mat_gap = make_material("GapHint", (0.31, 0.76, 0.97), metallic=0.0, roughness=0.5)

    housing = import_mesh(root, "hall_housing", name="HallHousing", location=(0.0, 0.0, 0.35), material=mat_house)
    if housing is None:
        bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0.0, 0.0, 0.35))
        housing = bpy.context.active_object
        housing.name = "HallHousing"
        housing.scale = (0.275, 0.175, 0.125)
        housing.data.materials.append(mat_house)

    magnet = import_mesh(root, "magnet_block", name="Magnet", location=(0.0, 0.0, -0.05), material=mat_mag)
    if magnet is None:
        bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0.0, 0.0, -0.05))
        magnet = bpy.context.active_object
        magnet.name = "Magnet"
        magnet.scale = (0.09, 0.06, 0.06)
        magnet.data.materials.append(mat_mag)

    # Animate magnet approaching housing: gap metaphor ~4mm -> ~2mm (scaled visually)
    magnet.location.z = -0.12
    magnet.keyframe_insert("location", frame=1)
    magnet.location.z = 0.02
    magnet.keyframe_insert("location", frame=args.frames)

    # Visible gap marker
    bpy.ops.mesh.primitive_cylinder_add(radius=0.015, depth=0.20, location=(0.22, 0.0, 0.12))
    gap = bpy.context.active_object
    gap.name = "GapMarker"
    gap.data.materials.append(mat_gap)
    gap.scale.z = 1.0
    gap.keyframe_insert("scale", frame=1)
    gap.scale.z = 0.55
    gap.keyframe_insert("scale", frame=args.frames)

    defaults = [
        root / "out/_excel_parts/44_r51_霍尔传感器.png",
        root / "out/_excel_parts/42_r49_传感器外壳.png",
    ]
    photos = [Path(p) for p in (args.photo_a, args.photo_b) if p] or defaults
    for i, photo in enumerate(photos[:2]):
        if photo.exists():
            add_image_plane(
                photo,
                name=f"Hall_Ref_{i+1}",
                location=(1.55, 1.4 - i * 1.3, 0.55),
                rotation_euler=(math.radians(90), 0.0, math.radians(-10)),
                width=1.15,
            )

    if args.hud:
        add_hud_image_plane(Path(args.hud), location=(-1.55, -0.15, 1.0), width=1.25)

    add_camera(location=(2.1, -2.0, 1.15), rotation_euler=(math.radians(62), 0, math.radians(48)))
    bpy.ops.render.render(animation=True)
    print(f"OK blender hall -> {out}")


if __name__ == "__main__":
    main()
