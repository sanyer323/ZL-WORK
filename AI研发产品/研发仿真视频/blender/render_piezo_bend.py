# -*- coding: utf-8 -*-
"""
FY301 Blender clip: piezo disk bends under rising voltage (segment 01).

Run (Windows example):
  blender --background --python blender/render_piezo_bend.py -- --out out/blender/01_压电陶瓷原理.mp4

This script is intentionally procedural (no external CAD mesh required).
Keep the FY301 skill causal story: V↑ → disk bends → flapper displacement.
"""
from __future__ import annotations

import argparse
import math
import sys
from pathlib import Path


def _parse_args(argv: list[str]) -> argparse.Namespace:
    if "--" in argv:
        argv = argv[argv.index("--") + 1 :]
    else:
        argv = []
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True, help="Output mp4 path")
    ap.add_argument("--frames", type=int, default=120)
    ap.add_argument("--fps", type=int, default=20)
    ap.add_argument("--res-x", type=int, default=1280)
    ap.add_argument("--res-y", type=int, default=720)
    return ap.parse_args(argv)


def main() -> None:
    import bpy
    from mathutils import Vector

    args = _parse_args(sys.argv)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)

    # Reset scene
    bpy.ops.wm.read_factory_settings(use_empty=True)
    scene = bpy.context.scene
    # EEVEE name differs across Blender 3.x / 4.x
    engine_ids = {e.identifier for e in bpy.types.RenderSettings.bl_rna.properties["engine"].enum_items}
    if "BLENDER_EEVEE_NEXT" in engine_ids:
        scene.render.engine = "BLENDER_EEVEE_NEXT"
    elif "BLENDER_EEVEE" in engine_ids:
        scene.render.engine = "BLENDER_EEVEE"
    else:
        scene.render.engine = "CYCLES"
    scene.render.resolution_x = args.res_x
    scene.render.resolution_y = args.res_y
    scene.render.fps = args.fps
    scene.frame_start = 1
    scene.frame_end = args.frames
    scene.render.filepath = str(out)
    scene.render.image_settings.file_format = "FFMPEG"
    scene.render.ffmpeg.format = "MPEG4"
    scene.render.ffmpeg.codec = "H264"
    scene.render.ffmpeg.constant_rate_factor = "MEDIUM"
    scene.render.film_transparent = False

    # World
    world = bpy.data.worlds.new("FY301World")
    scene.world = world
    world.use_nodes = True
    bg = world.node_tree.nodes["Background"]
    bg.inputs[0].default_value = (0.043, 0.071, 0.125, 1)  # #0b1220
    bg.inputs[1].default_value = 1.0

    # Nozzle body (static)
    bpy.ops.mesh.primitive_cylinder_add(radius=0.12, depth=0.55, location=(0.0, 0.0, 0.05))
    nozzle = bpy.context.active_object
    nozzle.name = "Nozzle"
    mat_metal = bpy.data.materials.new("Metal")
    mat_metal.use_nodes = True
    nt = mat_metal.node_tree.nodes["Principled BSDF"]
    nt.inputs["Base Color"].default_value = (0.55, 0.62, 0.70, 1)
    nt.inputs["Metallic"].default_value = 0.85
    nt.inputs["Roughness"].default_value = 0.35
    nozzle.data.materials.append(mat_metal)

    # Piezo disk
    bpy.ops.mesh.primitive_cylinder_add(radius=0.55, depth=0.045, location=(0.0, 0.0, 0.42))
    disk = bpy.context.active_object
    disk.name = "PiezoDisk"
    bpy.ops.object.shade_smooth()
    mat_piezo = bpy.data.materials.new("Piezo")
    mat_piezo.use_nodes = True
    pb = mat_piezo.node_tree.nodes["Principled BSDF"]
    pb.inputs["Base Color"].default_value = (0.78, 0.55, 0.90, 1)
    pb.inputs["Roughness"].default_value = 0.45
    disk.data.materials.append(mat_piezo)

    # Shape key: center rises (bend toward nozzle gap metaphor)
    sk_basis = disk.shape_key_add(name="Basis", from_mix=False)
    sk_bend = disk.shape_key_add(name="Bend", from_mix=False)
    mesh = disk.data
    # Local radius in object space; cylinder is along Z.
    for i, v in enumerate(mesh.vertices):
        # Use undeformed coordinates from basis
        co = sk_basis.data[i].co
        r = math.hypot(co.x, co.y)
        # Edge constrained, center deflects downward toward nozzle
        w = max(0.0, 1.0 - (r / 0.55) ** 2)
        sk_bend.data[i].co = co + Vector((0.0, 0.0, -0.16 * w))

    # Animate voltage 0→100 mapped to bend 0→1
    sk_bend.value = 0.0
    sk_bend.keyframe_insert("value", frame=1)
    sk_bend.value = 1.0
    sk_bend.keyframe_insert("value", frame=args.frames)

    # Camera + light
    bpy.ops.object.camera_add(location=(1.8, -1.6, 1.15), rotation=(math.radians(65), 0, math.radians(48)))
    cam = bpy.context.active_object
    scene.camera = cam
    bpy.ops.object.light_add(type="AREA", location=(1.2, -0.2, 2.2))
    light = bpy.context.active_object
    light.data.energy = 250
    light.data.size = 2.5

    # HUD-like empties are not needed; keep geometry clean for later compositing in principle edition.

    bpy.ops.render.render(animation=True)
    print(f"OK blender piezo -> {out}")


if __name__ == "__main__":
    main()
