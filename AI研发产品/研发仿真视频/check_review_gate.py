# -*- coding: utf-8 -*-
"""
审片门禁：检查 storyboard 是否覆盖 skill 要求的关键手册数据与结构。
不渲染、不配音。人工勾选见 REVIEW_CHECKLIST.md。
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
STORYBOARD = ROOT / "storyboard.json"
CHECKLIST = ROOT / "REVIEW_CHECKLIST.md"
SRT = ROOT / "out" / "FY301_原理讲解版.srt"

# (label, patterns) — any pattern hit counts as covered across narration+hud+takeaway
REQUIRED = [
    ("压电驱动 0–100 V", [r"0\s*[–\-〜~到至]\s*100\s*V", r"零到一百伏", r"0-100 V"]),
    ("目标/正常电压区", [r"50\s*V", r"三十到七十", r"30\s*[–\-〜~到至]\s*70", r"五十伏"]),
    ("FYCAL 供气 20 psi", [r"20\s*psi", r"二十磅", r"FYCAL\s*@\s*20"]),
    ("FYCAL @0 V ≤2", [r"≤\s*2", r"不高于两磅", r"0\s*V.*2"]),
    ("FYCAL @50 V ~6", [r"5\.8", r"6\.2", r"六点", r"50\s*V.*6", r"≈\s*6"]),
    ("FYCAL @100 V ~12–13", [r"12\s*[–\-〜~到至]\s*13", r"十二到十三", r"100\s*V.*12"]),
    ("Hall 间隙 2–4 mm", [r"2\s*[–\-〜~到至]\s*4\s*mm", r"二到四毫米", r"Hall.*间隙"]),
    ("环路 ~3.8 mA", [r"3\.8\s*mA", r"三点八毫安", r"~?\s*3\.8"]),
]


def corpus_from_storyboard(data: dict) -> str:
    parts: list[str] = []
    for seg in data.get("segments") or []:
        parts.append(str(seg.get("narration") or ""))
        parts.append(str(seg.get("takeaway") or ""))
        parts.append(str(seg.get("part_note") or ""))
        parts.append(str(seg.get("title") or ""))
        for h in seg.get("hud") or []:
            parts.append(str(h))
    return "\n".join(parts)


def main() -> int:
    errors: list[str] = []
    warns: list[str] = []

    if not CHECKLIST.exists():
        errors.append("missing REVIEW_CHECKLIST.md (审片清单模板)")

    if not STORYBOARD.exists():
        print("FAIL")
        print(" - missing storyboard.json")
        return 1

    data = json.loads(STORYBOARD.read_text(encoding="utf-8"))
    segs = data.get("segments") or []
    if len(segs) < 5:
        errors.append(f"expected >=5 segments, got {len(segs)}")

    for seg in segs:
        sid = seg.get("id", "?")
        if not (seg.get("takeaway") or "").strip():
            errors.append(f"segment {sid}: missing takeaway")
        if len(seg.get("hud") or []) < 2:
            errors.append(f"segment {sid}: need >=2 hud badges")
        side = len(seg.get("fycal_imgs") or []) + len(seg.get("parts") or [])
        if side < 2:
            errors.append(f"segment {sid}: need >=2 side refs (fycal_imgs/parts)")

    text = corpus_from_storyboard(data)
    for label, patterns in REQUIRED:
        ok = any(re.search(p, text, flags=re.IGNORECASE) for p in patterns)
        if not ok:
            errors.append(f"handbook data missing from storyboard: {label}")

    # Optional SRT soft check
    if SRT.exists():
        srt = SRT.read_text(encoding="utf-8", errors="ignore")
        soft = [
            ("3.8 mA / 三点八", [r"3\.8", r"三点八"]),
            ("Hall / 霍尔", [r"Hall", r"霍尔"]),
            ("FYCAL", [r"FYCAL", r"标定"]),
        ]
        for label, patterns in soft:
            if not any(re.search(p, srt) for p in patterns):
                warns.append(f"SRT soft-miss: {label}")
    else:
        warns.append("principle SRT not built yet (ok at verify-only)")

    # Blender 05 should be registered once P4 lands
    clips = ((data.get("blender_enhancements") or {}).get("clips")) or []
    ids = {c.get("segment_id") for c in clips}
    if "05" not in ids:
        errors.append("blender_enhancements missing segment 05 (signal flow)")
    else:
        script = ROOT / next(c["script"] for c in clips if c.get("segment_id") == "05")
        if not script.exists():
            errors.append(f"missing blender script for 05: {script}")

    for w in warns:
        print("warn:", w, flush=True)

    if errors:
        print("FAIL")
        for e in errors:
            print(" -", e)
        return 1

    print(
        "OK: review gate passed "
        f"({len(segs)} segments, {len(REQUIRED)} handbook checks, checklist present)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
