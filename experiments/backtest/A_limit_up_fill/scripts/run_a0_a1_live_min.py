#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Experiment A — A0/A1/A1k LIVE_MIN prototype on daily_min_sample.

Uses permission-window sample only [2025-08-04, 2026-08-11].
NOT investment advice. No live trading. Reuses fill logic from run_a0_a1_fill.py.
"""
from __future__ import annotations

import hashlib
import json
import sys
from datetime import datetime
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

import pandas as pd
import yaml

ROOT = Path(__file__).resolve().parents[1]
PARAMS_PATH = ROOT / "params.yaml"
OUT_DIR = ROOT / "results" / "live_sample"
SAMPLE_PATH = ROOT / "data" / "daily_min_sample.parquet"
HYP_DOC = "智库/金融股票/假设-A-涨停可成交性.md"
TICK = Decimal("0.01")
PERM_START, PERM_END = "2025-08-04", "2026-08-11"

sys.path.insert(0, str(ROOT / "scripts"))
from run_a0_a1_fill import (  # noqa: E402
    board_segment_table,
    file_sha256,
    load_params,
    run_leg,
    summarize,
)


def round_half_up(x: float, tick: Decimal = TICK) -> float:
    d = Decimal(str(x)).quantize(tick, rounding=ROUND_HALF_UP)
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


def board_and_pct(code: str) -> tuple[str, float]:
    c = str(code)
    # ChiNext / STAR ~ 20%; main ~ 10%. ST not in this 3-name min sample.
    if c.startswith("300") or c.startswith("301") or c.startswith("688"):
        return "chi_next", 0.20
    return "main", 0.10


def enrich_live_bars(raw: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for r in raw.itertuples(index=False):
        code = str(getattr(r, "code"))
        board, pct = board_and_pct(code)
        pre = float(r.pre_close)
        o, h, l, c = float(r.open), float(r.high), float(r.low), float(r.close)
        vol = int(float(r.volume) or 0)
        paused = float(getattr(r, "paused", 0) or 0) != 0.0
        limit_up, limit_down = limit_prices(pre, pct)
        one_up = (o == h == l == c == limit_up) and vol > 0
        one_down = (o == h == l == c == limit_down) and vol > 0
        close_up = abs(c - limit_up) < 1e-9
        close_down = abs(c - limit_down) < 1e-9
        dt = pd.Timestamp(r.date).strftime("%Y-%m-%d")
        rows.append(
            {
                "date": dt,
                "symbol": code,
                "board": board,
                "st": False,
                "limit_pct": pct,
                "pre_close": pre,
                "open": o,
                "high": h,
                "low": l,
                "close": c,
                "volume": vol,
                "limit_up": limit_up,
                "limit_down": limit_down,
                "is_one_word_up": bool(one_up),
                "is_one_word_down": bool(one_down),
                "is_limit_up_close": bool(close_up),
                "is_limit_down_close": bool(close_down),
                "is_suspended": bool(paused) or vol <= 0,
                "tradable": (not paused) and vol > 0,
                "data_mode": "live_min",
                "FAKE": False,
                "hypothesis_id": "A",
            }
        )
    df = pd.DataFrame(rows)
    # Guard: stay inside permission window
    bad = df[(df["date"] < PERM_START) | (df["date"] > PERM_END)]
    if len(bad):
        raise SystemExit(f"ABORT: bars outside permission window: {bad['date'].unique().tolist()}")
    return df


def main() -> int:
    params = load_params()
    fill_cfg = params.get("fill") or {}
    fail_policy = params.get("fail_policy", "skip")
    fail_rule = params.get("fail_rule", "close_seal_incl_non_one_word")
    kappa = float((params.get("a1k") or {}).get("kappa", 0.01))
    groups = list(params.get("groups") or ["A0", "A1", "A1k"])
    # Short sample: rebalance every 3 sessions so A0/A1 get >1 fill attempt
    rebal_every = 3

    if not SAMPLE_PATH.exists():
        raise SystemExit(f"missing sample: {SAMPLE_PATH}")

    raw = pd.read_parquet(SAMPLE_PATH)
    df = enrich_live_bars(raw)
    symbols = sorted(df["symbol"].unique().tolist())
    d0, d1 = str(df["date"].min()), str(df["date"].max())
    # Single LIVE_MIN window (too short for real IS/holdout); holdout_min = last 3 days for table shape only
    dates = sorted(df["date"].unique())
    if len(dates) < 4:
        raise SystemExit(f"LIVE_MIN too short: {len(dates)} dates")
    is_a, is_b = dates[0], dates[-4]  # leave last 3 for holdout_min shape
    ho_a, ho_b = dates[-3], dates[-1]

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    fill_default = fill_cfg.get("default", "next_open")
    assert fill_default in ("next_open", "open")
    fill_jobs = [("open", "default"), ("close", "robustness")]

    summary_rows = []
    equity_all = []
    for fill_price, fill_role in fill_jobs:
        for seg_name, a, b in (("LIVE_MIN_IS", is_a, is_b), ("LIVE_MIN_holdout", ho_a, ho_b)):
            mode_map = {}
            for mode in groups:
                eq, st, port, last_px = run_leg(
                    df, symbols, mode, rebal_every, a, b, kappa=kappa, fill_price=fill_price
                )
                # Retag FAKE flags for live outputs
                eq = eq.copy()
                eq["data_mode"] = "live_min"
                eq["FAKE"] = False
                mode_map[mode] = (eq, st, port, last_px)
                equity_all.append(eq.assign(segment=seg_name, fill_role=fill_role))
            row = summarize(seg_name, fill_price, mode_map)
            row["data_mode"] = "live_min"
            row["FAKE"] = False
            row["fill_role"] = fill_role
            row["fail_policy"] = fail_policy
            row["fail_rule"] = fail_rule
            summary_rows.append(row)

    summary_df = pd.DataFrame(summary_rows)
    equity_df = pd.concat(equity_all, ignore_index=True)

    primary = summary_df[summary_df["fill_price"] == "open"].copy()
    robust = summary_df[summary_df["fill_price"] == "close"].copy()

    board_is = board_segment_table(df, is_a, is_b)
    board_ho = board_segment_table(df, ho_a, ho_b)
    for bdf in (board_is, board_ho):
        bdf["data_mode"] = "live_min"
        bdf["FAKE"] = False
    board_df = pd.concat(
        [board_is.assign(oos="LIVE_MIN_IS"), board_ho.assign(oos="LIVE_MIN_holdout")],
        ignore_index=True,
    )

    primary_path = OUT_DIR / "summary_LIVE_MIN_next_open.csv"
    robust_path = OUT_DIR / "summary_LIVE_MIN_next_close_ROBUSTNESS.csv"
    equity_path = OUT_DIR / "equity_curves.csv"
    blocked_path = OUT_DIR / "blocked_and_turnover.csv"
    board_path = OUT_DIR / "board_segment_main_vs_chinext.csv"
    residual_path = OUT_DIR / "end_residual_positions.json"
    enriched_path = OUT_DIR / "enriched_daily_min_bars.parquet"
    meta_path = OUT_DIR / "RUN_META.json"
    three_path = OUT_DIR / "THREE_LINE_SUMMARY.md"

    primary.to_csv(primary_path, index=False)
    robust.to_csv(robust_path, index=False)
    equity_df.to_csv(equity_path, index=False)
    board_df.to_csv(board_path, index=False)
    df.to_parquet(enriched_path, index=False)

    blocked_cols = [
        c
        for c in primary.columns
        if "blocked" in c
        or "turnover" in c
        or c in ("segment", "fill_price", "FAKE", "data_mode", "hypothesis_id", "fail_policy", "fail_rule")
        or c.startswith("nav_gap")
        or c.startswith("return_gap")
    ]
    primary[blocked_cols].to_csv(blocked_path, index=False)

    residual = {
        "hypothesis_id": "A",
        "data_mode": "live_min",
        "LIVE_MIN": True,
        "FAKE": False,
        "fail_policy": fail_policy,
        "fail_rule": fail_rule,
        "fill_default": "next_open",
        "disclaimer": "NOT stock advice. LIVE_MIN 3 symbols ~10 sessions only.",
        "note": "Residuals from DEFAULT next_open legs only",
        "rows": primary[
            [
                "segment",
                "A0_end_residual_weights",
                "A1_end_residual_weights",
                "A1k_end_residual_weights",
                "A0_end_cash",
                "A1_end_cash",
                "A1k_end_cash",
            ]
        ].to_dict(orient="records"),
    }
    residual_path.write_text(json.dumps(residual, ensure_ascii=False, indent=2), encoding="utf-8")

    as_of = datetime.now().astimezone().isoformat(timespec="seconds")
    limit_counts = {
        "n_one_word_up": int(df["is_one_word_up"].sum()),
        "n_one_word_down": int(df["is_one_word_down"].sum()),
        "n_close_seal_up": int(df["is_limit_up_close"].sum()),
        "n_close_seal_down": int(df["is_limit_down_close"].sum()),
        "n_suspended": int(df["is_suspended"].sum()),
    }
    meta = {
        "as_of": as_of,
        "timezone_note": "Asia/Shanghai (UKING-ZL local)",
        "run_tag": "LIVE_MIN",
        "hypothesis_id": "A",
        "hypothesis_doc": HYP_DOC,
        "experiment_id": params.get("experiment_id", "A_limit_up_fill"),
        "data_mode": "live_min",
        "LIVE_MIN": True,
        "FAKE": False,
        "permission_window": f"{PERM_START} .. {PERM_END}",
        "sample_window": f"{d0} .. {d1}",
        "sample_path": "data/daily_min_sample.parquet",
        "sample_sha256": file_sha256(SAMPLE_PATH),
        "sample_rows": int(len(df)),
        "symbols": symbols,
        "n_sessions": int(df["date"].nunique()),
        "warning": (
            "LIVE_MIN prototype only: 3 names, ~10 trading days inside JoinQuant permission window. "
            "NOT a real backtest conclusion. NOT stock advice. No live trading."
        ),
        "script": "scripts/run_a0_a1_live_min.py",
        "core_fill_logic": "scripts/run_a0_a1_fill.py (imported)",
        "params_path": "params.yaml",
        "fill_default": "next_open",
        "fill_robustness": "next_close_separate_file",
        "fail_policy": fail_policy,
        "fail_rule": fail_rule,
        "groups": groups,
        "kappa": kappa,
        "rebalance_every_sessions": rebal_every,
        "signal": "dummy_fixed_rotation_100pct_one_symbol",
        "limit_rule": "unadjusted OHLC + pre_close; round_half_up to 0.01; board pct main=10%/chinext=20%",
        "oos_split_note": (
            "LIVE_MIN too short for production OOS; LIVE_MIN_IS / LIVE_MIN_holdout are shape-only "
            f"({is_a}..{is_b} / {ho_a}..{ho_b}); do NOT tune on holdout."
        ),
        "limit_event_counts": limit_counts,
        "outputs": {
            "summary_default_next_open": "results/live_sample/summary_LIVE_MIN_next_open.csv",
            "summary_robustness_next_close": "results/live_sample/summary_LIVE_MIN_next_close_ROBUSTNESS.csv",
            "equity": "results/live_sample/equity_curves.csv",
            "blocked_turnover": "results/live_sample/blocked_and_turnover.csv",
            "board_segment": "results/live_sample/board_segment_main_vs_chinext.csv",
            "residual": "results/live_sample/end_residual_positions.json",
            "enriched_bars": "results/live_sample/enriched_daily_min_bars.parquet",
            "meta": "results/live_sample/RUN_META.json",
        },
        "status": "LIVE_MIN A0/A1 prototype on permission-window sample",
    }
    meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")

    # Three-line human summary
    p_is = primary[primary["segment"] == "LIVE_MIN_IS"].iloc[0]
    lines = [
        "# LIVE_MIN three-line summary (NOT advice)",
        "",
        f"1. Data: `{SAMPLE_PATH.name}` codes={symbols} window={d0}..{d1} (inside {PERM_START}..{PERM_END}); rows={len(df)}.",
        f"2. next_open LIVE_MIN_IS: A0_ret={p_is['A0_total_return']:.6f} A1_ret={p_is['A1_total_return']:.6f} "
        f"gap_A1-A0={p_is['nav_gap_A1_minus_A0']:.6f}; blocked_buys A1={int(p_is['A1_blocked_buys'])} "
        f"(one_word={int(p_is['A1_blocked_buys_one_word'])}, close_seal={int(p_is['A1_blocked_buys_close_seal'])}).",
        "3. Caveat: 3 names / ~10 sessions; limit events may be zero on this quiet window — prototype wiring only, not a fillability conclusion.",
        "",
        f"as_of={as_of}",
    ]
    three_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    (OUT_DIR / "README.txt").write_text(
        "\n".join(
            [
                "results/live_sample — LIVE_MIN A0/A1/A1k prototype (JoinQuant permission-window sample)",
                f"See: {HYP_DOC}",
                "DEFAULT fill = next_open (summary_LIVE_MIN_next_open.csv).",
                "next_close is ROBUSTNESS only — do not mix into one NAV number.",
                "NOT for investment decisions. No live trading. No stock picks.",
                "Does not overwrite results/fake/.",
                "",
            ]
        ),
        encoding="utf-8",
    )

    print("OK LIVE_MIN hypothesis_id=A fill_default=next_open")
    print(
        primary[
            ["segment", "A0_total_return", "A1_total_return", "A1k_total_return", "nav_gap_A1_minus_A0", "A1_blocked_buys"]
        ].to_string(index=False)
    )
    print("limit_event_counts", limit_counts)
    print(f"Wrote {meta_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
