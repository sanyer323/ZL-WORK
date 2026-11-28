# -*- coding: utf-8 -*-
"""FY301 Blender clip 03: spool stroke with mesh import + part photos."""
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

    mat_sleeve = make_material("Sleeve", (0.45, 0.52, 0.60), metallic=0.8, roughness=0.3)
    mat_spool = make_material("Spool", (0.85, 0.75, 0.35), metallic=0.7, roughness=0.25)
    mat_diaph = make_material("Diaphragm", (0.75, 0.35, 0.28), metallic=0.05, roughness=0.55)

    sleeve = import_mesh(root, "sleeve", name="Sleeve", material=mat_sleeve)
    if sleeve is None:
        bpy.ops.mesh.primitive_cylinder_add(radius=0.28, depth=1.4, location=(0.0, 0.0, 0.0))
        sleeve = bpy.context.active_object
        sleeve.name = "Sleeve"
        sleeve.data.materials.append(mat_sleeve)

    spool = import_mesh(root, "spool", name="Spool", location=(0.0, 0.0, -0.18), material=mat_spool)
    if spool is None:
        bpy.ops.mesh.primitive_cylinder_add(radius=0.18, depth=0.95, location=(0.0, 0.0, -0.18))
        spool = bpy.context.active_object
        spool.name = "Spool"
        spool.data.materials.append(mat_spool)

    d_large = import_mesh(
        root,
        "diaphragm_large",
        name="DiaphragmLarge",
        location=(-0.95, 0.0, 0.35),
        rotation_euler=(0.0, math.radians(90), 0.0),
        material=mat_diaph,
    )
    if d_large is None:
        bpy.ops.mesh.primitive_cylinder_add(radius=0.62, depth=0.04, location=(-0.95, 0.0, 0.35))
        d_large = bpy.context.active_object
        d_large.name = "DiaphragmLarge"
        d_large.rotation_euler[1] = math.radians(90)
        d_large.data.materials.append(mat_diaph)

    d_small = import_mesh(
        root,
        "diaphragm_small",
        name="DiaphragmSmall",
        location=(-0.95, 0.0, -0.25),
        rotation_euler=(0.0, math.radians(90), 0.0),
        material=mat_diaph,
    )
    if d_small is None:
        bpy.ops.mesh.primitive_cylinder_add(radius=0.38, depth=0.04, location=(-0.95, 0.0, -0.25))
        d_small = bpy.context.active_object
        d_small.name = "DiaphragmSmall"
        d_small.rotation_euler[1] = math.radians(90)
        d_small.data.materials.append(mat_diaph)

    spool.location.z = -0.18
    spool.keyframe_insert("location", frame=1)
    d_large.scale = (1, 1, 1)
    d_large.keyframe_insert("scale", frame=1)
    spool.location.z = 0.22
    spool.keyframe_insert("location", frame=args.frames)
    d_large.scale = (1.06, 1.06, 0.85)
    d_large.keyframe_insert("scale", frame=args.frames)

    defaults = [
        root / "out/_excel_parts/33_r40_膜片.png",
        root / "out/_excel_parts/36_r43_滑阀.png",
    ]
    photos = [Path(p) for p in (args.photo_a, args.photo_b) if p] or defaults
    for i, photo in enumerate(photos[:2]):
        if photo.exists():
            add_image_plane(
                photo,
                name=f"Part_Ref_{i+1}",
                location=(1.65, 1.45 - i * 1.35, 0.55),
                rotation_euler=(math.radians(90), 0.0, math.radians(-10)),
                width=1.15,
            )

    if args.hud:
        add_hud_image_plane(Path(args.hud), location=(-1.55, -0.2, 1.05), width=1.2)

    add_camera(location=(2.35, -2.05, 1.2), rotation_euler=(math.radians(62), 0, math.radians(50)))
    bpy.ops.render.render(animation=True)
    print(f"OK blender spool -> {out}")


if __name__ == "__main__":
    main()
