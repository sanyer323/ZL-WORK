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
        p = OUT / name
        if not p.exists() or p.stat().st_size < 1000:
            missing.append(p)
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
    args = ap.parse_args()

    if not STORYBOARD.exists():
        raise SystemExit(f"missing storyboard: {STORYBOARD}")

    run_step("verify assets + storyboard", [PY, str(ROOT / "verify_fycal_assets.py")])

    if args.verify_only:
        print("\nDONE (verify-only)")
        return 0

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

    if args.skip_compose:
        print("\nDONE (skip-compose)")
        return 0

    run_step("compose principle edition", [PY, str(ROOT / "build_principle_edition.py")])
    final = OUT / "FY301_原理讲解版.mp4"
    print(f"\nDONE -> {final}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
