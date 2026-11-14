# -*- coding: utf-8 -*-
"""
Post-compose deliverable gate for FY301 principle edition.
Checks output mp4/srt when present; safe to run before first compose (warn-only).
"""
from __future__ import annotations

import re
from pathlib import Path

from fy301_common import OUT, ROOT, load_storyboard, probe_duration

MIN_PRINCIPLE_SECONDS = 45.0
MIN_SRT_CUES = 8


def parse_srt_cues(text: str) -> int:
    return len(re.findall(r"^\d+\s*$", text, flags=re.MULTILINE))


def main() -> int:
    errors: list[str] = []
    warns: list[str] = []

    data = load_storyboard()
    out_cfg = data.get("output") or {}
    mp4_rel = str(out_cfg.get("principle_mp4") or "out/FY301_原理讲解版.mp4")
    srt_rel = str(out_cfg.get("principle_srt") or "out/FY301_原理讲解版.srt")
    mp4 = ROOT / mp4_rel if not Path(mp4_rel).is_absolute() else Path(mp4_rel)
    srt = ROOT / srt_rel if not Path(srt_rel).is_absolute() else Path(srt_rel)

    if not mp4.exists():
        warns.append(f"principle mp4 not built yet: {mp4_rel}")
    else:
        dur = probe_duration(mp4)
        if dur < MIN_PRINCIPLE_SECONDS:
            errors.append(f"principle mp4 too short: {dur:.1f}s < {MIN_PRINCIPLE_SECONDS}s")
        else:
            print(f"principle mp4 duration: {dur:.1f}s", flush=True)
        if mp4.stat().st_size < 500_000:
            errors.append(f"principle mp4 suspiciously small: {mp4.stat().st_size} bytes")

    if not srt.exists():
        warns.append(f"principle srt not built yet: {srt_rel}")
    else:
        srt_text = srt.read_text(encoding="utf-8", errors="ignore")
        cues = parse_srt_cues(srt_text)
        if cues < MIN_SRT_CUES:
            errors.append(f"principle srt too few cues: {cues} < {MIN_SRT_CUES}")
        for term in ("压电", "先导", "滑阀", "霍尔", "FYCAL"):
            if term not in srt_text:
                errors.append(f"principle srt missing keyword: {term}")

    # Segment sims: at least matplotlib or blender present
    missing_sims = []
    for seg in data.get("segments") or []:
        sim = seg.get("sim") or ""
        if not sim:
            continue
        plain = OUT / sim
        blend = OUT / "blender" / sim
        if not ((plain.exists() and plain.stat().st_size > 1000) or (blend.exists() and blend.stat().st_size > 1000)):
            missing_sims.append(sim)
    if missing_sims:
        warns.append("segment sims not built: " + ", ".join(missing_sims))

    for w in warns:
        print("warn:", w, flush=True)
    if errors:
        print("FAIL")
        for e in errors:
            print(" -", e)
        return 1

    print("OK: principle deliverable checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
