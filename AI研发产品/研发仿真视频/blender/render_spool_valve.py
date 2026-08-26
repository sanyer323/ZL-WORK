# -*- coding: utf-8 -*-
"""
FY301 Blender clip: diaphragm force balance drives spool stroke (segment 03).

Run:
  blender --background --python blender/render_spool_valve.py -- --out out/blender/03_膜片放大与滑阀.mp4
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
    ap.add_argument("--out", required=True)
    ap.add_argument("--frames", type=int, default=120)
    ap.add_argument("--fps", type=int, default=20)
    ap.add_argument("--res-x", type=int, default=1280)
    ap.add_argument("--res-y", type=int, default=720)
    return ap.parse_args(argv)


def _mat(name: str, color, metallic=0.0, roughness=0.4):
    import bpy

    m = bpy.data.materials.new(name)
    m.use_nodes = True
    n = m.node_tree.nodes["Principled BSDF"]
    n.inputs["Base Color"].default_value = (*color, 1.0)
    n.inputs["Metallic"].default_value = metallic
    n.inputs["Roughness"].default_value = roughness
    return m


def main() -> None:
    import bpy

    args = _parse_args(sys.argv)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)

    bpy.ops.wm.read_factory_settings(use_empty=True)
    scene = bpy.context.scene
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

    world = bpy.data.worlds.new("FY301World")
    scene.world = world
    world.use_nodes = True
    world.node_tree.nodes["Background"].inputs[0].default_value = (0.043, 0.071, 0.125, 1)

    mat_sleeve = _mat("Sleeve", (0.45, 0.52, 0.60), metallic=0.8, roughness=0.3)
    mat_spool = _mat("Spool", (0.85, 0.75, 0.35), metallic=0.7, roughness=0.25)
    mat_diaph = _mat("Diaphragm", (0.75, 0.35, 0.28), metallic=0.05, roughness=0.55)

    # Sleeve
    bpy.ops.mesh.primitive_cylinder_add(radius=0.28, depth=1.4, location=(0.0, 0.0, 0.0))
    sleeve = bpy.context.active_object
    sleeve.name = "Sleeve"
    sleeve.data.materials.append(mat_sleeve)
    # Hollow look: scale inner by boolean is heavy; keep solid semi-transparent sleeve wall via wireframe feel
    sleeve.display_type = "SOLID"

    # Spool (lands)
    bpy.ops.mesh.primitive_cylinder_add(radius=0.18, depth=0.95, location=(0.0, 0.0, -0.18))
    spool = bpy.context.active_object
    spool.name = "Spool"
    spool.data.materials.append(mat_spool)

    # Two diaphragm disks (large pilot / small spool side metaphor)
    bpy.ops.mesh.primitive_cylinder_add(radius=0.62, depth=0.04, location=(-0.95, 0.0, 0.35))
    d_large = bpy.context.active_object
    d_large.name = "DiaphragmLarge"
    d_large.rotation_euler[1] = math.radians(90)
    d_large.data.materials.append(mat_diaph)

    bpy.ops.mesh.primitive_cylinder_add(radius=0.38, depth=0.04, location=(-0.95, 0.0, -0.25))
    d_small = bpy.context.active_object
    d_small.name = "DiaphragmSmall"
    d_small.rotation_euler[1] = math.radians(90)
    d_small.data.materials.append(mat_diaph)

    # Animate spool stroke + diaphragms hinting force change
    spool.location.z = -0.18
    spool.keyframe_insert("location", frame=1)
    d_large.scale = (1, 1, 1)
    d_large.keyframe_insert("scale", frame=1)
    spool.location.z = 0.22
    spool.keyframe_insert("location", frame=args.frames)
    d_large.scale = (1.06, 1.06, 0.85)
    d_large.keyframe_insert("scale", frame=args.frames)

    bpy.ops.object.camera_add(location=(2.3, -2.0, 1.2), rotation=(math.radians(62), 0, math.radians(50)))
    scene.camera = bpy.context.active_object
    bpy.ops.object.light_add(type="AREA", location=(1.4, 0.3, 2.4))
    light = bpy.context.active_object
    light.data.energy = 280
    light.data.size = 3.0

    bpy.ops.render.render(animation=True)
    print(f"OK blender spool -> {out}")


if __name__ == "__main__":
    main()
