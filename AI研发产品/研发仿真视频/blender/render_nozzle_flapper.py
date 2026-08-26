# -*- coding: utf-8 -*-
"""FY301 Blender clip 02: nozzle-flapper pilot stage + FYCAL calibration photos."""
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

    mat_metal = make_material("Metal", (0.52, 0.58, 0.66), metallic=0.85, roughness=0.3)
    mat_air = make_material("AirHint", (1.0, 0.72, 0.30), metallic=0.0, roughness=0.55)
    mat_flapper = make_material("Flapper", (0.78, 0.55, 0.90), roughness=0.4)

    bpy.ops.mesh.primitive_cylinder_add(radius=0.09, depth=0.7, location=(-0.55, 0.0, 0.0))
    restriction = bpy.context.active_object
    restriction.name = "Restriction"
    restriction.rotation_euler[1] = math.radians(90)
    restriction.data.materials.append(mat_metal)

    bpy.ops.mesh.primitive_cone_add(radius1=0.16, radius2=0.045, depth=0.35, location=(0.0, 0.0, 0.0))
    nozzle = bpy.context.active_object
    nozzle.name = "Nozzle"
    nozzle.rotation_euler[1] = math.radians(90)
    nozzle.data.materials.append(mat_metal)

    bpy.ops.mesh.primitive_cylinder_add(radius=0.28, depth=0.03, location=(0.42, 0.0, 0.0))
    flapper = bpy.context.active_object
    flapper.name = "PiezoFlapper"
    flapper.rotation_euler[1] = math.radians(90)
    flapper.data.materials.append(mat_flapper)
    flapper.location.x = 0.55
    flapper.keyframe_insert("location", frame=1)
    flapper.location.x = 0.28
    flapper.keyframe_insert("location", frame=args.frames)

    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.18, location=(-0.15, 0.35, 0.35))
    pilot = bpy.context.active_object
    pilot.name = "PilotPressureHint"
    pilot.data.materials.append(mat_air)
    pilot.scale = (0.55, 0.55, 0.55)
    pilot.keyframe_insert("scale", frame=1)
    pilot.scale = (1.25, 1.25, 1.25)
    pilot.keyframe_insert("scale", frame=args.frames)

    defaults = [
        root / "out/_fycal_figs/_named/fig12_cal_on_block.png",
        root / "out/_fycal_figs/_named/fig10_supply_piezo.png",
    ]
    photos = [Path(p) for p in (args.photo_a, args.photo_b) if p] or defaults
    for i, photo in enumerate(photos[:2]):
        if photo.exists():
            add_image_plane(
                photo,
                name=f"FYCAL_Pilot_{i+1}",
                location=(1.6, 1.5 - i * 1.35, 0.55),
                rotation_euler=(math.radians(90), 0.0, math.radians(-10)),
                width=1.25,
            )

    if args.hud:
        add_hud_image_plane(Path(args.hud), location=(-1.6, -0.15, 1.05), width=1.25)

    add_camera(location=(2.3, -2.1, 1.2), rotation_euler=(math.radians(63), 0, math.radians(48)))
    bpy.ops.render.render(animation=True)
    print(f"OK blender nozzle-flapper -> {out}")


if __name__ == "__main__":
    main()
