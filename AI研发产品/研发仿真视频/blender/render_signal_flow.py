# -*- coding: utf-8 -*-
"""FY301 Blender clip 05: full-loop signal flow (电→气→机→电) with pulse animation."""
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


def _node_at(location, *, name: str, material, scale=(0.35, 0.22, 0.12)):
    import bpy

    bpy.ops.mesh.primitive_cube_add(size=1.0, location=location)
    obj = bpy.context.active_object
    obj.name = name
    obj.scale = scale
    obj.data.materials.append(material)
    return obj


def main() -> None:
    import bpy

    root = add_root_to_syspath(__file__)
    args = parse_common_argv(sys.argv)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    reset_dark_scene(args.res_x, args.res_y, args.fps, args.frames, out)

    mat_pcb = make_material("PCB", (0.12, 0.42, 0.28), metallic=0.15, roughness=0.45)
    mat_piezo = make_material("Piezo", (0.85, 0.78, 0.35), metallic=0.35, roughness=0.35)
    mat_air = make_material("AirBlock", (0.45, 0.55, 0.65), metallic=0.7, roughness=0.3)
    mat_act = make_material("Actuator", (0.55, 0.35, 0.25), metallic=0.4, roughness=0.4)
    mat_hall = make_material("Hall", (0.55, 0.60, 0.68), metallic=0.65, roughness=0.35)
    mat_pulse = make_material("Pulse", (0.31, 0.76, 0.97), metallic=0.0, roughness=0.2)
    mat_link = make_material("Link", (0.25, 0.35, 0.48), metallic=0.2, roughness=0.55)

    # Chain positions (left → right), then Hall loops visually back
    stations = [
        ("Loop_mA", (-2.4, 0.0, 0.2), mat_pcb, "pcb_board", (0.55, 0.08, 0.35)),
        ("Piezo", (-1.2, 0.0, 0.25), mat_piezo, "piezo_disk", (0.55, 0.55, 0.08)),
        ("Pilot", (0.0, 0.0, 0.2), mat_air, "nozzle_body", (0.35, 0.35, 0.45)),
        ("Spool", (1.2, 0.0, 0.15), mat_air, "pneumatic_block", (0.55, 0.35, 0.28)),
        ("Actuator", (2.4, 0.0, 0.2), mat_act, "actuator_hint", (0.28, 0.28, 0.55)),
        ("Hall", (1.8, -1.1, 0.15), mat_hall, "hall_housing", (0.35, 0.22, 0.18)),
    ]

    objs = []
    for name, loc, mat, stem, scale in stations:
        imported = import_mesh(root, stem, name=name, location=loc, scale=scale, material=mat)
        if imported is None:
            imported = _node_at(loc, name=name, material=mat, scale=scale)
        objs.append(imported)

    # Link bars between consecutive stations (including Hall back toward PCB)
    link_pairs = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0)]
    for a, b in link_pairs:
        pa = stations[a][1]
        pb = stations[b][1]
        mid = ((pa[0] + pb[0]) / 2, (pa[1] + pb[1]) / 2, (pa[2] + pb[2]) / 2 + 0.05)
        dx, dy, dz = pb[0] - pa[0], pb[1] - pa[1], pb[2] - pa[2]
        length = max(math.sqrt(dx * dx + dy * dy + dz * dz), 0.01)
        bpy.ops.mesh.primitive_cylinder_add(radius=0.025, depth=length, location=mid)
        bar = bpy.context.active_object
        bar.name = f"Link_{a}_{b}"
        bar.data.materials.append(mat_link)
        # orient cylinder Z toward target
        bar.rotation_euler = (
            math.atan2(math.sqrt(dx * dx + dy * dy), dz) if abs(dz) > 1e-6 else math.radians(90),
            0.0,
            math.atan2(dy, dx),
        )

    # Traveling pulse along the polyline (closed loop)
    path = [s[1] for s in stations] + [stations[0][1]]
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.09, location=path[0])
    pulse = bpy.context.active_object
    pulse.name = "SignalPulse"
    pulse.data.materials.append(mat_pulse)

    frames = max(int(args.frames), 2)
    segs_n = len(path) - 1
    for fi in range(1, frames + 1):
        t = (fi - 1) / (frames - 1)
        # one full loop
        u = t * segs_n
        i = min(int(u), segs_n - 1)
        local = u - i
        a, b = path[i], path[i + 1]
        pulse.location = (
            a[0] + (b[0] - a[0]) * local,
            a[1] + (b[1] - a[1]) * local,
            a[2] + (b[2] - a[2]) * local + 0.12,
        )
        pulse.keyframe_insert("location", frame=fi)

    defaults = [
        root / "out/_excel_parts/03_r6_线路板.png",
        root / "out/_excel_parts/40_r47_气动组件外壳.png",
    ]
    photos = [Path(p) for p in (args.photo_a, args.photo_b) if p] or defaults
    for i, photo in enumerate(photos[:2]):
        if photo.exists():
            add_image_plane(
                photo,
                name=f"Loop_Ref_{i+1}",
                location=(i * 1.4 - 0.7, 1.55, 0.7),
                rotation_euler=(math.radians(90), 0.0, math.radians(8 if i == 0 else -8)),
                width=1.15,
            )

    if args.hud:
        add_hud_image_plane(Path(args.hud), location=(-2.3, -1.35, 1.05), width=1.3)

    add_camera(location=(0.3, -4.2, 2.4), rotation_euler=(math.radians(62), 0, math.radians(5)))
    bpy.ops.render.render(animation=True)
    print(f"OK blender signal flow -> {out}")


if __name__ == "__main__":
    main()
