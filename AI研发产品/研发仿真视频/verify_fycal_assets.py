# -*- coding: utf-8 -*-
"""Verify FY301 principle-edition assets / storyboard without rendering/TTS."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "out"
PARTS = OUT / "_excel_parts"
FYCAL_FIGS = OUT / "_fycal_figs" / "_named"
FYCAL_MANIFEST_PATH = FYCAL_FIGS / "manifest.json"
STORYBOARD_PATH = ROOT / "storyboard.json"
BUILD_SCRIPT = ROOT / "build_principle_edition.py"


def load_segments() -> list[dict]:
    if not STORYBOARD_PATH.exists():
        raise FileNotFoundError(f"missing {STORYBOARD_PATH}")
    data = json.loads(STORYBOARD_PATH.read_text(encoding="utf-8"))
    segs = data["segments"] if isinstance(data, dict) else data
    out = []
    for seg in segs:
        fycal = []
        for item in seg.get("fycal_imgs") or []:
            if isinstance(item, dict):
                fycal.append(item["file"])
            else:
                fycal.append(item[0])
        out.append(
            {
                "id": seg["id"],
                "sim": seg.get("sim", ""),
                "parts": list(seg.get("parts") or []),
                "fycal": fycal,
                "hud": list(seg.get("hud") or []),
                "narration": seg.get("narration") or "",
                "takeaway": seg.get("takeaway") or "",
            }
        )
    return out


def main() -> int:
    errors: list[str] = []

    if not BUILD_SCRIPT.exists():
        errors.append(f"missing {BUILD_SCRIPT}")
    else:
        src = BUILD_SCRIPT.read_text(encoding="utf-8")
        for token in (
            "load_segments",
            "STORYBOARD_PATH",
            "side_images",
            "burn_hud",
            "make_hud_overlay_png",
            "compose_sim_with_photos",
        ):
            if token not in src:
                errors.append(f"missing implementation in build script: {token}")

    try:
        segs = load_segments()
    except Exception as e:  # noqa: BLE001
        print("FAIL")
        print(" -", e)
        return 1

    # Optional Blender enhancement layer (P3)
    try:
        sb = json.loads(STORYBOARD_PATH.read_text(encoding="utf-8"))
        clips = ((sb.get("blender_enhancements") or {}).get("clips")) or []
        for clip in clips:
            script = ROOT / clip.get("script", "")
            if not script.exists():
                errors.append(f"blender script missing: {clip.get('script')}")
            else:
                # syntax-only check (bpy unavailable outside Blender)
                import ast

                ast.parse(script.read_text(encoding="utf-8"))
            out_rel = clip.get("out") or ""
            if out_rel:
                out_p = ROOT / out_rel
                if out_p.exists() and out_p.stat().st_size >= 1000:
                    print(f"blender clip present: {out_rel}", flush=True)
                else:
                    print(f"warn: blender clip not built yet: {out_rel}", flush=True)
        runner = ROOT / "render_blender_clips.py"
        if not runner.exists():
            errors.append("missing render_blender_clips.py")
        else:
            import ast

            ast.parse(runner.read_text(encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        errors.append(f"blender enhancement check failed: {e}")

    # P5: master edition + product_parts B-roll metadata
    try:
        sb = json.loads(STORYBOARD_PATH.read_text(encoding="utf-8"))
        master = sb.get("master_edition") or {}
        broll = master.get("product_parts_broll") or {}
        if not broll:
            errors.append("master_edition.product_parts_broll missing in storyboard.json")
        pp = sb.get("product_parts") or {}
        pp_script = ROOT / str(pp.get("script") or "render_product_parts.py")
        if not pp_script.exists():
            errors.append(f"product_parts script missing: {pp_script.name}")
        else:
            import ast

            ast.parse(pp_script.read_text(encoding="utf-8"))
        if not (ROOT / "fy301_common.py").exists():
            errors.append("missing fy301_common.py")
        if not (ROOT / "check_principle_deliverable.py").exists():
            errors.append("missing check_principle_deliverable.py")
        idx = ROOT / "parts_index.json"
        if idx.exists():
            raw_idx = json.loads(idx.read_text(encoding="utf-8"))
            for row in raw_idx.values():
                p = str((row or {}).get("path", ""))
                if Path(p).is_absolute() or re.match(r"^[A-Za-z]:/", p) or ":\\" in p:
                    errors.append(f"absolute path in parts_index.json: {p}")
    except Exception as e:  # noqa: BLE001
        errors.append(f"master/product_parts check failed: {e}")

    if len(segs) < 5:
        errors.append(f"storyboard expected >=5 segments, got {len(segs)}")

    parts_man = []
    if PARTS.joinpath("manifest.json").exists():
        parts_man = json.loads((PARTS / "manifest.json").read_text(encoding="utf-8"))
    by_label = {m["label"]: m for m in parts_man}

    fycal_man: dict[str, dict] = {}
    if not FYCAL_MANIFEST_PATH.exists():
        errors.append(f"missing {FYCAL_MANIFEST_PATH}")
    else:
        raw = json.loads(FYCAL_MANIFEST_PATH.read_text(encoding="utf-8"))
        for row in raw:
            f = str(row.get("file", ""))
            if Path(f).is_absolute() or ":\\" in f or f.startswith("\\\\") or re.match(r"^[A-Za-z]:/", f):
                errors.append(f"absolute path in FYCAL manifest: {f}")
            rel = Path(f).name
            if not rel:
                continue
            fycal_man[rel] = row
            if not (FYCAL_FIGS / rel).exists():
                errors.append(f"manifest file missing on disk: {rel}")

    if "fig14_piezo_base_labeled.png" not in fycal_man:
        errors.append("manifest missing fig14_piezo_base_labeled.png")
    if not (FYCAL_FIGS / "fig14_piezo_base_labeled.png").exists():
        errors.append("disk missing fig14_piezo_base_labeled.png")

    for seg in segs:
        if not seg.get("narration"):
            errors.append(f"segment {seg['id']} missing narration")
        if not seg.get("takeaway"):
            errors.append(f"segment {seg['id']} missing takeaway")
        if seg.get("sim"):
            # presence is optional at verify-only time; warn only
            sim_path = OUT / seg["sim"]
            if not sim_path.exists():
                print(f"warn: simulation not built yet: {seg['sim']}", flush=True)

        for lab in seg["parts"]:
            m = by_label.get(lab)
            if not m:
                errors.append(f"segment {seg['id']} unknown part label: {lab}")
                continue
            p = PARTS / m["file"]
            if not p.exists():
                errors.append(f"segment {seg['id']} missing part image: {p.name}")
        for fname in seg["fycal"]:
            p = FYCAL_FIGS / Path(fname).name
            if not p.exists():
                errors.append(f"segment {seg['id']} missing FYCAL image: {p.name}")
            elif p.name not in fycal_man:
                errors.append(f"segment {seg['id']} FYCAL image not in manifest: {p.name}")

        panel_n = len(seg["fycal"]) if seg["fycal"] else len(seg["parts"])
        if panel_n < 2:
            errors.append(f"segment {seg['id']} needs >=2 side-panel images, got {panel_n}")
        if len(seg["hud"]) < 2:
            errors.append(f"segment {seg['id']} needs >=2 hud badges, got {len(seg['hud'])}")

    if errors:
        print("FAIL")
        for e in errors:
            print(" -", e)
        return 1

    print(
        "OK: FY301 principle assets consistent "
        f"({len(segs)} segments from storyboard.json, side panels + hud, "
        f"{len(fycal_man)} FYCAL manifest entries, relative paths)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
