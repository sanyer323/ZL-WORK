# -*- coding: utf-8 -*-
"""Shared helpers for FY301 Blender enhancement clips (bpy runtime)."""
from __future__ import annotations

import math
from pathlib import Path


def add_root_to_syspath(script_file: str) -> Path:
    import sys

    root = Path(script_file).resolve().parents[1]
    blender_dir = Path(script_file).resolve().parent
    for p in (str(blender_dir), str(root)):
        if p not in sys.path:
            sys.path.insert(0, p)
    return root


def choose_eevee(scene) -> None:
    import bpy

    engine_ids = {e.identifier for e in bpy.types.RenderSettings.bl_rna.properties["engine"].enum_items}
    if "BLENDER_EEVEE_NEXT" in engine_ids:
        scene.render.engine = "BLENDER_EEVEE_NEXT"
    elif "BLENDER_EEVEE" in engine_ids:
        scene.render.engine = "BLENDER_EEVEE"
    else:
        scene.render.engine = "CYCLES"


def reset_dark_scene(res_x: int, res_y: int, fps: int, frames: int, out: Path):
    import bpy

    bpy.ops.wm.read_factory_settings(use_empty=True)
    scene = bpy.context.scene
    choose_eevee(scene)
    scene.render.resolution_x = res_x
    scene.render.resolution_y = res_y
    scene.render.fps = fps
    scene.frame_start = 1
    scene.frame_end = frames
    scene.render.filepath = str(out)
    scene.render.image_settings.file_format = "FFMPEG"
    scene.render.ffmpeg.format = "MPEG4"
    scene.render.ffmpeg.codec = "H264"
    scene.render.ffmpeg.constant_rate_factor = "MEDIUM"
    scene.render.film_transparent = False

    world = bpy.data.worlds.new("FY301World")
    scene.world = world
    world.use_nodes = True
    bg = world.node_tree.nodes["Background"]
    bg.inputs[0].default_value = (0.043, 0.071, 0.125, 1)
    bg.inputs[1].default_value = 1.0
    return scene


def make_material(name: str, color, metallic: float = 0.0, roughness: float = 0.4):
    import bpy

    m = bpy.data.materials.new(name)
    m.use_nodes = True
    n = m.node_tree.nodes["Principled BSDF"]
    n.inputs["Base Color"].default_value = (*color, 1.0)
    n.inputs["Metallic"].default_value = metallic
    n.inputs["Roughness"].default_value = roughness
    return m


def add_image_plane(
    image_path: Path,
    *,
    name: str,
    location=(0.0, 0.0, 0.0),
    rotation_euler=(math.radians(90), 0.0, 0.0),
    width: float = 1.2,
):
    """Create a textured plane from a PNG/JPG (FYCAL or Excel part photo)."""
    import bpy

    image_path = Path(image_path)
    if not image_path.exists():
        raise FileNotFoundError(image_path)

    img = bpy.data.images.load(str(image_path))
    aspect = img.size[0] / max(img.size[1], 1)
    height = width / aspect

    bpy.ops.mesh.primitive_plane_add(size=1.0, location=location)
    obj = bpy.context.active_object
    obj.name = name
    obj.rotation_euler = rotation_euler
    obj.scale = (width / 2.0, height / 2.0, 1.0)

    mat = bpy.data.materials.new(f"Mat_{name}")
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    nodes.clear()
    out = nodes.new("ShaderNodeOutputMaterial")
    bsdf = nodes.new("ShaderNodeBsdfPrincipled")
    tex = nodes.new("ShaderNodeTexImage")
    tex.image = img
    links.new(tex.outputs["Color"], bsdf.inputs["Base Color"])
    links.new(bsdf.outputs["BSDF"], out.inputs["Surface"])
    obj.data.materials.append(mat)
    return obj


def add_camera(location, rotation_euler, energy: float = 280.0):
    import bpy

    bpy.ops.object.camera_add(location=location, rotation=rotation_euler)
    cam = bpy.context.active_object
    bpy.context.scene.camera = cam
    bpy.ops.object.light_add(type="AREA", location=(location[0] * 0.4, location[1] * 0.2, location[2] + 1.0))
    light = bpy.context.active_object
    light.data.energy = energy
    light.data.size = 3.0
    bpy.ops.object.light_add(type="AREA", location=(-1.2, 1.0, 1.6))
    fill = bpy.context.active_object
    fill.data.energy = energy * 0.35
    fill.data.size = 2.5
    return cam


def add_hud_image_plane(hud_png: Path, location=(0.0, -1.55, 1.05), width: float = 1.35):
    """Optional pre-baked HUD/key-number card in-frame."""
    if not hud_png or not Path(hud_png).exists():
        return None
    return add_image_plane(
        Path(hud_png),
        name="HUD",
        location=location,
        rotation_euler=(math.radians(78), 0.0, 0.0),
        width=width,
    )


def meshes_dir(root: Path) -> Path:
    return root / "blender" / "meshes"


def import_mesh(
    root: Path,
    stem: str,
    *,
    name: str,
    location=(0.0, 0.0, 0.0),
    rotation_euler=(0.0, 0.0, 0.0),
    scale=(1.0, 1.0, 1.0),
    material=None,
):
    """
    Import mesh from blender/meshes/<stem>.{obj,stl,fbx,glb,gltf,ply}.
    Returns the active object, or None if no mesh file exists.
    """
    import bpy

    base = meshes_dir(root)
    candidates = []
    for ext in (".obj", ".stl", ".fbx", ".glb", ".gltf", ".ply"):
        candidates.append(base / f"{stem}{ext}")
    path = next((p for p in candidates if p.exists()), None)
    if path is None:
        return None

    before = set(bpy.data.objects.keys())
    ext = path.suffix.lower()
    if ext == ".obj":
        if hasattr(bpy.ops.wm, "obj_import"):
            bpy.ops.wm.obj_import(filepath=str(path))
        else:
            bpy.ops.import_scene.obj(filepath=str(path))
    elif ext == ".stl":
        if hasattr(bpy.ops.wm, "stl_import"):
            bpy.ops.wm.stl_import(filepath=str(path))
        else:
            bpy.ops.import_mesh.stl(filepath=str(path))
    elif ext == ".fbx":
        bpy.ops.import_scene.fbx(filepath=str(path))
    elif ext in {".glb", ".gltf"}:
        bpy.ops.import_scene.gltf(filepath=str(path))
    elif ext == ".ply":
        bpy.ops.wm.ply_import(filepath=str(path)) if hasattr(bpy.ops.wm, "ply_import") else bpy.ops.import_mesh.ply(filepath=str(path))
    else:
        return None

    after = [bpy.data.objects[k] for k in bpy.data.objects.keys() if k not in before]
    if not after:
        return None
    obj = after[0]
    if len(after) > 1:
        bpy.ops.object.select_all(action="DESELECT")
        for o in after:
            o.select_set(True)
        bpy.context.view_layer.objects.active = after[0]
        bpy.ops.object.join()
        obj = bpy.context.active_object
    obj.name = name
    obj.location = location
    obj.rotation_euler = rotation_euler
    obj.scale = scale
    if material is not None:
        if obj.data.materials:
            obj.data.materials[0] = material
        else:
            obj.data.materials.append(material)
    print(f"imported mesh: {path.name} -> {name}", flush=True)
    return obj


def mesh_or_primitive(root: Path, stem: str, primitive_fn, **kwargs):
    """Try import_mesh(stem); if missing, call primitive_fn() which must return an object."""
    obj = import_mesh(root, stem, name=kwargs.get("name", stem), **{k: v for k, v in kwargs.items() if k != "name"})
    if obj is not None:
        return obj
    return primitive_fn()


def parse_common_argv(argv: list[str]):
    import argparse
    import sys

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
    ap.add_argument("--hud", default="", help="Optional HUD overlay PNG")
    ap.add_argument("--photo-a", default="", help="Optional reference photo A")
    ap.add_argument("--photo-b", default="", help="Optional reference photo B")
    return ap.parse_args(argv if argv else sys.argv[1:])
