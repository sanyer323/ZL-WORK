#!/usr/bin/env python3
"""Minimal JoinQuant daily pull for experiment A. Creds via env only; never log secrets."""
from __future__ import annotations

import hashlib
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT_PQ = DATA / "daily_min_sample.parquet"
OUT_META = DATA / "daily_min_sample_meta.json"

# Minimal: few names, ~3 calendar months ending before today (Asia/Shanghai)
CODES = [
    "000001.XSHE",  # 平安银行 主板
    "600000.XSHG",  # 浦发银行 主板
    "300750.XSHE",  # 宁德时代 创业板
]
START = "2024-07-01"
END = "2024-09-30"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    user = os.environ.get("JQDATA_USERNAME") or "18930501903"
    password = os.environ.get("JQDATA_PASSWORD")
    token = os.environ.get("JQDATA_TOKEN")
    if not password and not token:
        print("MISSING_CRED: set JQDATA_PASSWORD or JQDATA_TOKEN", file=sys.stderr)
        return 2

    import jqdatasdk as jq

    if token:
        jq.auth_by_token(token)
    else:
        jq.auth(user, password)

    if not jq.is_auth():
        print("AUTH_FAIL", file=sys.stderr)
        return 3

    # Do not print account details beyond query count shape
    try:
        qc = jq.get_query_count()
        print("AUTH_OK query_count_keys=", sorted(qc.keys()) if isinstance(qc, dict) else type(qc).__name__)
    except Exception as e:
        print("AUTH_OK query_count_err=", type(e).__name__)

    # fq=None → 不复权；含 open/close/high/low/volume/money；另取 paused
    frames = []
    for code in CODES:
        df = jq.get_price(
            code,
            start_date=START,
            end_date=END,
            frequency="daily",
            fields=["open", "close", "high", "low", "volume", "money", "pre_close", "paused"],
            skip_paused=False,
            fq=None,
        )
        if df is None or len(df) == 0:
            print(f"EMPTY {code}")
            continue
        df = df.reset_index().rename(columns={"index": "date"})
        df["code"] = code
        frames.append(df)
        print(f"ROWS {code}={len(df)}")

    if not frames:
        print("NO_DATA", file=sys.stderr)
        jq.logout()
        return 4

    all_df = pd.concat(frames, ignore_index=True)
    DATA.mkdir(parents=True, exist_ok=True)
    all_df.to_parquet(OUT_PQ, index=False)

    # Security info: board / start_date (IPO) for limit_pct later
    info_rows = []
    for code in CODES:
        try:
            info = jq.get_security_info(code)
            info_rows.append(
                {
                    "code": code,
                    "display_name": getattr(info, "display_name", None),
                    "start_date": str(getattr(info, "start_date", "")),
                    "end_date": str(getattr(info, "end_date", "")),
                    "type": getattr(info, "type", None),
                }
            )
        except Exception as e:
            info_rows.append({"code": code, "error": type(e).__name__})

    meta = {
        "as_of": datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds"),
        "vendor": "joinquant/jqdatasdk",
        "jqdatasdk_version": getattr(jq, "__version__", "unknown"),
        "codes": CODES,
        "start": START,
        "end": END,
        "fq": None,
        "fields": ["open", "close", "high", "low", "volume", "money", "pre_close", "paused", "code", "date"],
        "rows": int(len(all_df)),
        "parquet": str(OUT_PQ.name),
        "sha256": sha256_file(OUT_PQ),
        "security_info": info_rows,
        "note": "minimal sample for A0/A1 scaffold; not full A-share universe",
    }
    OUT_META.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    print("WROTE", OUT_PQ, "rows=", len(all_df), "sha256=", meta["sha256"][:16] + "...")
    try:
        jq.logout()
    except Exception:
        pass
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
