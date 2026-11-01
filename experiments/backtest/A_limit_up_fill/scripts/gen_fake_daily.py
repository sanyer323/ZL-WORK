#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate FAKE daily bars for Experiment A dry-run. NOT real market data.

hypothesis_id=A; data_mode=fake. Aligns with 智库/金融股票/假设-A-涨停可成交性.md
"""
from __future__ import annotations

import hashlib
import json
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT_PARQUET = DATA / "fake_daily_bars.parquet"
OUT_CSV = DATA / "fake_daily_bars.csv"
OUT_META = DATA / "fake_daily_bars_meta.json"
FAKE_README = DATA / "FAKE_README.txt"

SYMBOLS = [
    {"symbol": "FAKE600001.XSHG", "board": "main", "limit_pct": 0.10, "start": 10.0},
    {"symbol": "FAKE000002.XSHE", "board": "main", "limit_pct": 0.10, "start": 8.5},
    {"symbol": "FAKE300001.XSHE", "board": "chi_next", "limit_pct": 0.20, "start": 25.0},
]

IS_START, IS_END = "2021-01-01", "2023-12-31"
HO_START, HO_END = "2024-01-01", "2024-09-30"
TICK = Decimal("0.01")


def round_half_up(x: float, tick: Decimal = TICK) -> float:
    d = Decimal(str(x)).quantize(tick, rounding=ROUND_HALF_UP)
    # edge guards from hypothesis doc
    if d < tick:
        d = tick
    return float(d)


def limit_prices(pre_close: float, pct: float) -> tuple[float, float]:
    pre = Decimal(str(pre_close))
    raw_up = pre * (Decimal("1") + Decimal(str(pct)))
    raw_down = pre * (Decimal("1") - Decimal(str(pct)))
    up = Decimal(str(round_half_up(float(raw_up))))
    down = Decimal(str(round_half_up(float(raw_down))))
    if abs(up - pre) < TICK:
        up = pre + TICK
    if abs(down - pre) < TICK:
        down = pre - TICK
    if down < TICK:
        down = TICK
    return float(up), float(down)


def build_calendar() -> pd.DatetimeIndex:
    return pd.bdate_range(IS_START, HO_END, freq="C")


def gen_symbol(cfg: dict, dates: pd.DatetimeIndex, rng: np.random.Generator) -> pd.DataFrame:
    n = len(dates)
    prev = cfg["start"]
    pct = cfg["limit_pct"]
    rows = []
    # Deterministic event cadences so A0/A1 diverge.
    force_one_word_up = set(range(23, n, 61))
    force_one_word_down = set(range(41, n, 67))
    force_close_seal_up = set(range(11, n, 43))  # non-one-word close seal up
    force_close_seal_down = set(range(19, n, 47))
    force_suspend = set(range(71, n, 89))

    for i, dt in enumerate(dates):
        limit_up, limit_down = limit_prices(prev, pct)
        suspended = i in force_suspend
        if suspended:
            o = h = l = c = round_half_up(prev)
            vol = 0
            one_up = one_down = False
            close_up = close_down = False
        elif i in force_one_word_up:
            o = h = l = c = limit_up
            vol = int(rng.integers(100_000, 800_000))
            one_up, one_down = True, False
            close_up, close_down = True, False
        elif i in force_one_word_down:
            o = h = l = c = limit_down
            vol = int(rng.integers(100_000, 800_000))
            one_up, one_down = False, True
            close_up, close_down = False, True
        elif i in force_close_seal_up:
            # open not at limit; close seals up (non-one-word)
            o = round_half_up(prev * (1.0 + float(rng.uniform(-0.01, 0.02))))
            o = min(max(o, limit_down), round_half_up(limit_up - 0.01))
            c = limit_up
            h = limit_up
            l = round_half_up(min(o, prev) * (1.0 - abs(float(rng.normal(0, 0.005)))))
            l = max(l, limit_down)
            vol = int(rng.integers(300_000, 2_500_000))
            one_up = one_down = False
            close_up, close_down = True, False
        elif i in force_close_seal_down:
            o = round_half_up(prev * (1.0 + float(rng.uniform(-0.02, 0.01))))
            o = min(max(o, round_half_up(limit_down + 0.01)), limit_up)
            c = limit_down
            l = limit_down
            h = round_half_up(max(o, prev) * (1.0 + abs(float(rng.normal(0, 0.005)))))
            h = min(h, limit_up)
            vol = int(rng.integers(300_000, 2_500_000))
            one_up = one_down = False
            close_up, close_down = False, True
        else:
            shock = float(rng.normal(0.0, pct * 0.25))
            raw = prev * (1.0 + shock)
            c = round_half_up(min(max(raw, limit_down), limit_up))
            o = round_half_up(prev * (1.0 + float(rng.normal(0.0, pct * 0.08))))
            o = min(max(o, limit_down), limit_up)
            h = round_half_up(max(o, c, prev) * (1.0 + abs(float(rng.normal(0, 0.002)))))
            l = round_half_up(min(o, c, prev) * (1.0 - abs(float(rng.normal(0, 0.002)))))
            h = min(max(h, o, c), limit_up)
            l = max(min(l, o, c), limit_down)
            vol = int(rng.integers(200_000, 2_000_000))
            one_up = (o == h == l == c == limit_up) and vol > 0
            one_down = (o == h == l == c == limit_down) and vol > 0
            close_up = c >= limit_up - 1e-12
            close_down = c <= limit_down + 1e-12

        rows.append(
            {
                "date": dt.strftime("%Y-%m-%d"),
                "symbol": cfg["symbol"],
                "board": cfg["board"],
                "st": False,
                "limit_pct": pct,
                "pre_close": round_half_up(prev),
                "open": o,
                "high": h,
                "low": l,
                "close": c,
                "volume": int(vol),
                "limit_up": limit_up,
                "limit_down": limit_down,
                "is_one_word_up": bool(one_up),
                "is_one_word_down": bool(one_down),
                "is_limit_up_close": bool(close_up),
                "is_limit_down_close": bool(close_down),
                "is_suspended": bool(suspended),
                "tradable": (not suspended) and int(vol) > 0,
                "data_mode": "fake",
                "FAKE": True,
                "hypothesis_id": "A",
            }
        )
        prev = float(c)

    return pd.DataFrame(rows)


def main() -> int:
    DATA.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(20260101)
    dates = build_calendar()
    df = pd.concat([gen_symbol(cfg, dates, rng) for cfg in SYMBOLS], ignore_index=True)
    df = df.sort_values(["date", "symbol"]).reset_index(drop=True)
    df.to_parquet(OUT_PARQUET, index=False)
    df.to_csv(OUT_CSV, index=False)
    sha = hashlib.sha256(OUT_PARQUET.read_bytes()).hexdigest()
    meta = {
        "hypothesis_id": "A",
        "data_mode": "fake",
        "FAKE": True,
        "warning": "NOT real market data. Do NOT treat outputs as investment conclusions.",
        "hypothesis_doc": "智库/金融股票/假设-A-涨停可成交性.md",
        "symbols": [s["symbol"] for s in SYMBOLS],
        "boards": sorted({s["board"] for s in SYMBOLS}),
        "limit_pct_by_board": {"main": 0.10, "chi_next": 0.20},
        "round": "half_up_to_0.01_on_unadjusted_pre_close",
        "date_min": str(df["date"].min()),
        "date_max": str(df["date"].max()),
        "n_rows": int(len(df)),
        "n_dates": int(df["date"].nunique()),
        "n_one_word_up": int(df["is_one_word_up"].sum()),
        "n_one_word_down": int(df["is_one_word_down"].sum()),
        "n_close_seal_up": int(df["is_limit_up_close"].sum()),
        "n_suspended": int(df["is_suspended"].sum()),
        "oos_split": {
            "in_sample": f"{IS_START} .. {IS_END}",
            "holdout": f"{HO_START} .. {HO_END}",
        },
        "parquet": "data/fake_daily_bars.parquet",
        "csv": "data/fake_daily_bars.csv",
        "sha256_parquet": sha,
    }
    OUT_META.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    FAKE_README.write_text(
        "\n".join(
            [
                "FAKE DATA — 非真数",
                "================",
                "本目录下文件名含 fake 的行情均为合成假数据，仅用于实验 A / 假设 A 骨架干跑。",
                "对齐文档：智库/金融股票/假设-A-涨停可成交性.md",
                "禁止把基于本数据的净值差、换手、受阻统计当作真实市场结论或荐股依据。",
                "真数路径（等本机 8765 鉴权提交后）：data/daily_min_sample.parquet",
                "",
                f"parquet: {OUT_PARQUET.name}",
                f"csv: {OUT_CSV.name}",
                f"sha256(parquet): {sha}",
                f"rows: {len(df)}  dates: {df['date'].nunique()}  symbols: {df['symbol'].nunique()}",
                f"boards: main(+/-10%), chi_next(+/-20%)",
                "",
            ]
        ),
        encoding="utf-8",
    )
    print(f"Wrote {OUT_PARQUET} rows={len(df)} sha256={sha[:12]}...")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
