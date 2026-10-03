# -*- coding: utf-8 -*-
"""FY301 Blender clip 01: piezo disk bend + mesh import + FYCAL photos."""
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
    from mathutils import Vector

    root = add_root_to_syspath(__file__)
    args = parse_common_argv(sys.argv)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    reset_dark_scene(args.res_x, args.res_y, args.fps, args.frames, out)

    mat_metal = make_material("Metal", (0.55, 0.62, 0.70), metallic=0.85, roughness=0.32)
    mat_piezo = make_material("Piezo", (0.78, 0.55, 0.90), roughness=0.45)

    nozzle = import_mesh(root, "nozzle_body", name="Nozzle", location=(0.0, 0.0, 0.02), material=mat_metal)
    if nozzle is None:
        bpy.ops.mesh.primitive_cylinder_add(radius=0.11, depth=0.5, location=(0.0, 0.0, 0.02))
        nozzle = bpy.context.active_object
        nozzle.name = "Nozzle"
        nozzle.data.materials.append(mat_metal)

    disk = import_mesh(root, "piezo_disk", name="PiezoDisk", location=(0.0, 0.0, 0.40), material=mat_piezo)
    if disk is None:
        bpy.ops.mesh.primitive_cylinder_add(radius=0.55, depth=0.04, location=(0.0, 0.0, 0.40))
        disk = bpy.context.active_object
        disk.name = "PiezoDisk"
        disk.data.materials.append(mat_piezo)
    bpy.ops.object.shade_smooth()

    # Bend shape key on whatever mesh we have
    sk_basis = disk.shape_key_add(name="Basis", from_mix=False)
    sk_bend = disk.shape_key_add(name="Bend", from_mix=False)
    # Estimate radius from bounds
    xs = [v.co.x for v in disk.data.vertices]
    ys = [v.co.y for v in disk.data.vertices]
    radius = max(0.05, max(max(abs(min(xs)), abs(max(xs))), max(abs(min(ys)), abs(max(ys)))))
    for i, _v in enumerate(disk.data.vertices):
        co = sk_basis.data[i].co
        r = math.hypot(co.x, co.y)
        w = max(0.0, 1.0 - (r / radius) ** 2)
        sk_bend.data[i].co = co + Vector((0.0, 0.0, -0.17 * w))
    sk_bend.value = 0.0
    sk_bend.keyframe_insert("value", frame=1)
    sk_bend.value = 1.0
    sk_bend.keyframe_insert("value", frame=args.frames)

    defaults = [
        root / "out/_fycal_figs/_named/fig16_cleaning_piezo.png",
        root / "out/_fycal_figs/_named/fig18_exploded_piezo.png",
    ]
    photos = [Path(p) for p in (args.photo_a, args.photo_b) if p] or defaults
    for i, photo in enumerate(photos[:2]):
        if photo.exists():
            add_image_plane(
                photo,
                name=f"FYCAL_Ref_{i+1}",
                location=(1.55, 1.55 - i * 1.35, 0.55),
                rotation_euler=(math.radians(90), 0.0, math.radians(-12)),
                width=1.25,
            )

    if args.hud:
        add_hud_image_plane(Path(args.hud), location=(-1.55, -0.2, 1.05), width=1.2)

    add_camera(location=(2.15, -2.05, 1.25), rotation_euler=(math.radians(64), 0, math.radians(50)))
    bpy.ops.render.render(animation=True)
    print(f"OK blender piezo -> {out}")


if __name__ == "__main__":
    main()
