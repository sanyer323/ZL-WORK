# -*- coding: utf-8 -*-
"""
FY301 原理讲解版一键流水线

默认：
1) 校验 storyboard / 图片资源
2) 若 01–05 仿真缺失则 render_sims
3) 合成原理讲解版 build_principle_edition

示例：
  python run_principle_pipeline.py
  python run_principle_pipeline.py --verify-only
  python run_principle_pipeline.py --force-sims
  python run_principle_pipeline.py --skip-compose
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
STORYBOARD = ROOT / "storyboard.json"
OUT = ROOT / "out"
PY = sys.executable


def run_step(title: str, argv: list[str]) -> None:
    print(f"\n=== {title} ===", flush=True)
    print("+", " ".join(argv), flush=True)
    r = subprocess.run(argv, cwd=str(ROOT))
    if r.returncode != 0:
        raise SystemExit(f"STEP FAILED: {title} (exit {r.returncode})")


def load_sim_names() -> list[str]:
    data = json.loads(STORYBOARD.read_text(encoding="utf-8"))
    return [seg["sim"] for seg in data["segments"]]


def missing_sims() -> list[Path]:
    missing = []
    for name in load_sim_names():
        plain = OUT / name
        blend = OUT / "blender" / name
        ok_plain = plain.exists() and plain.stat().st_size >= 1000
        ok_blend = blend.exists() and blend.stat().st_size >= 1000
        if not (ok_plain or ok_blend):
            missing.append(plain)
    return missing


def main() -> int:
    ap = argparse.ArgumentParser(description="FY301 principle edition one-click pipeline")
    ap.add_argument("--verify-only", action="store_true", help="只跑资源/分镜校验")
    ap.add_argument("--force-sims", action="store_true", help="强制重渲 01–05 仿真")
    ap.add_argument("--skip-sims", action="store_true", help="不渲染仿真（缺文件则失败）")
    ap.add_argument("--skip-compose", action="store_true", help="校验/仿真后不合成成片")
    ap.add_argument(
        "--rebuild-manifest",
        action="store_true",
        help="合成前按磁盘 PNG 重建 FYCAL 相对路径 manifest",
    )
    ap.add_argument(
        "--with-blender",
        action="store_true",
        help="合成前尝试渲染 Blender 增强段（01–05）；失败则回退 matplotlib",
    )
    ap.add_argument(
        "--require-blender",
        action="store_true",
        help="与 --with-blender 联用：Blender 失败则中止（不回退）",
    )
    ap.add_argument("--blender", default=None, help="Blender 可执行文件路径（可选）")
    ap.add_argument(
        "--with-product-parts",
        action="store_true",
        help="尝试渲染产品部件透明 B-roll（需 AI研发产品/SMAR SKD 照片）",
    )
    ap.add_argument(
        "--build-master",
        action="store_true",
        help="原理片合成后再构建研发完整版 master（含可选 product_parts B-roll）",
    )
    ap.add_argument(
        "--strict-deliverable",
        action="store_true",
        help="合成后运行成片验收；缺 mp4/srt 时失败",
    )
    args = ap.parse_args()

    if not STORYBOARD.exists():
        raise SystemExit(f"missing storyboard: {STORYBOARD}")

    run_step("verify assets + storyboard", [PY, str(ROOT / "verify_fycal_assets.py")])
    run_step("check default deliverable + mesh pack", [PY, str(ROOT / "check_default_deliverable.py")])
    run_step("review gate (handbook data + checklist)", [PY, str(ROOT / "check_review_gate.py")])

    if args.verify_only:
        print("\nDONE (verify-only)")
        return 0

    mesh_dir = ROOT / "blender" / "meshes"
    if not (mesh_dir / "piezo_disk.obj").exists():
        run_step("build placeholder meshes", [PY, str(ROOT / "blender" / "build_placeholder_meshes.py")])
        run_step("re-check mesh pack", [PY, str(ROOT / "check_default_deliverable.py")])

    if args.rebuild_manifest:
        run_step("rebuild FYCAL manifest", [PY, str(ROOT / "rebuild_fycal_manifest.py")])
        run_step("re-verify after manifest rebuild", [PY, str(ROOT / "verify_fycal_assets.py")])

    need_sims = args.force_sims or bool(missing_sims())
    if need_sims and args.skip_sims:
        miss = ", ".join(p.name for p in missing_sims()) or "(force requested)"
        raise SystemExit(f"--skip-sims but simulation videos missing/forced: {miss}")

    if need_sims:
        reason = "forced" if args.force_sims else "missing/incomplete"
        run_step(f"render sims ({reason})", [PY, str(ROOT / "render_sims.py")])
    else:
        print("\n=== render sims ===\nskip (01–05 already present; use --force-sims to rebuild)", flush=True)

    if args.with_blender or args.require_blender:
        bcmd = [PY, str(ROOT / "render_blender_clips.py")]
        if args.blender:
            bcmd += ["--blender", args.blender]
        print("\n=== blender enhancement clips ===", flush=True)
        print("+", " ".join(bcmd), flush=True)
        br = subprocess.run(bcmd, cwd=str(ROOT))
        if br.returncode != 0:
            if args.require_blender:
                raise SystemExit(f"STEP FAILED: blender clips (exit {br.returncode})")
            print(
                f"warn: blender clips failed (exit {br.returncode}); "
                "principle compose will fall back to matplotlib sims",
                flush=True,
            )

    if args.with_product_parts:
        print("\n=== product parts transparent B-roll ===", flush=True)
        pr = subprocess.run([PY, str(ROOT / "render_product_parts.py")], cwd=str(ROOT))
        if pr.returncode != 0:
            print(
                f"warn: product_parts render failed (exit {pr.returncode}); "
                "master B-roll will be skipped where clips are missing",
                flush=True,
            )

    if args.skip_compose:
        print("\nDONE (skip-compose)")
        return 0

    run_step("compose principle edition", [PY, str(ROOT / "build_principle_edition.py")])
    run_step("check principle deliverable (soft)", [PY, str(ROOT / "check_principle_deliverable.py")])

    if args.build_master:
        run_step("build master edition", [PY, str(ROOT / "build_master.py")])

    final = OUT / "FY301_原理讲解版.mp4"
    if args.strict_deliverable:
        r = subprocess.run([PY, str(ROOT / "check_principle_deliverable.py")], cwd=str(ROOT))
        if r.returncode != 0:
            raise SystemExit("strict deliverable check failed")
    print(f"\nDONE -> {final}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
