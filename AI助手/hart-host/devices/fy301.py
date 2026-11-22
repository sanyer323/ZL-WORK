"""Map Chinese (or English) utterances to FY301 HART intents."""

from __future__ import annotations

import json
from pathlib import Path

LEARNED = Path(__file__).with_name("fy301_learned.json")


def load_learned() -> dict:
    return json.loads(LEARNED.read_text(encoding="utf-8"))


def match_intent(text: str, learned: dict | None = None) -> tuple[str, dict]:
    learned = learned or load_learned()
    t = text.strip().lower()
    aliases = [
        ("读身份", ("身份", "谁", "poll", "command 0", "厂家")),
        ("读阀门位置", ("阀位", "位置", "pv", "开度")),
        ("读回路电流", ("电流", "毫安", "ma", "回路")),
        ("读四变量", ("四变量", "sv", "tv", "qv", "全部变量")),
        ("读压电电压", ("压电", "piezo", "电压")),
        ("读霍尔值", ("霍尔", "hall")),
        ("自动校准", ("auto setup", "自动校准", "autosetup")),
    ]
    for name, keys in aliases:
        if any(k in t for k in keys):
            return name, learned["intents"][name]
    return "读身份", learned["intents"]["读身份"]
