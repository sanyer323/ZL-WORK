#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Experiment A — A0/A1/A1k LIVE_EXPAND on daily_expand_window (permission window).

Input: data/daily_expand_window.parquet (full bars, NOT seal_event_subset alone).
Window: [2025-07-26, 2026-08-02]. NOT advice. No live trading.
Reuses execute_rebalance / FillStats from run_a0_a1_fill.py.
Seal-aware dummy: day before close-seal events, force target so fill day hits blocked.
"""
from __future__ import annotations

import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "results" / "live_expand"
SAMPLE_PATH = ROOT / "data" / "daily_expand_window.parquet"
SEAL_SUBSET_PATH = ROOT / "data" / "seal_event_subset.parquet"
EVIDENCE_PATH = ROOT / "data" / "expand_seal_evidence.txt"
HYP_DOC = "智库/金融股票/假设-A-涨停可成交性.md"
PERM_START, PERM_END = "2025-07-26", "2026-08-02"

sys.path.insert(0, str(ROOT / "scripts"))
from run_a0_a1_fill import (  # noqa: E402
    FillStats,
    Portfolio,
    board_segment_table,
    execute_rebalance,
    file_sha256,
    load_params,
    summarize,
    target_weights_for_day,
)


def enrich_expand_bars(raw: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for r in raw.itertuples(index=False):
        code = str(getattr(r, "code"))
        board = str(getattr(r, "board", "main") or "main")
        if board in ("chi_next", "chinext", "ChiNext"):
            board = "chi_next"
        elif board in ("star", "STAR"):
            board = "star"
        else:
            board = "main"
        vol = int(float(r.volume) or 0)
        paused = bool(getattr(r, "paused", False))
        suspended = bool(getattr(r, "is_suspended", False)) or paused or vol <= 0
        dt = pd.Timestamp(r.date).strftime("%Y-%m-%d")
        rows.append(
            {
                "date": dt,
                "symbol": code,
                "board": board,
                "st": False,
                "limit_pct": float(getattr(r, "limit_pct", 0.1) or 0.1),
                "pre_close": float(r.pre_close),
                "open": float(r.open),
                "high": float(r.high),
                "low": float(r.low),
                "close": float(r.close),
                "volume": vol,
                "limit_up": float(getattr(r, "limit_up")),
                "limit_down": float(getattr(r, "limit_down")),
                "is_one_word_up": bool(getattr(r, "is_one_word_up", False)),
                "is_one_word_down": bool(getattr(r, "is_one_word_down", False)),
                "is_limit_up_close": bool(getattr(r, "is_limit_up_close", False)),
                "is_limit_down_close": bool(getattr(r, "is_limit_down_close", False)),
                "is_suspended": bool(suspended),
                "tradable": (not suspended) and vol > 0,
                "data_mode": "live_expand",
                "FAKE": False,
                "hypothesis_id": "A",
            }
        )
    df = pd.DataFrame(rows)
    bad = df[(df["date"] < PERM_START) | (df["date"] > PERM_END)]
    if len(bad):
        raise SystemExit(f"ABORT: bars outside permission window: {sorted(bad['date'].unique().tolist())[:5]}")
    return df


def build_seal_signal_targets(df: pd.DataFrame, dates: List[str]) -> Dict[str, Dict[str, float]]:
    """Map SIGNAL date -> target weights so FILL day (=next session) coincides with seal.

    - close_seal_up on D for S: signal on D_prev target S=1 → fill on D buy blocked (A1)
    - close_seal_down on D for S: signal D_prev2 target S=1 (enter); signal D_prev target {} (exit)
      → fill sell on D sell blocked (A1)
    """
    idx = {d: i for i, d in enumerate(dates)}
    out: Dict[str, Dict[str, float]] = {}

    up = df.loc[df["is_limit_up_close"], ["date", "symbol"]].drop_duplicates()
    for r in up.itertuples(index=False):
        i = idx.get(str(r.date))
        if i is None or i < 1:
            continue
        out[dates[i - 1]] = {str(r.symbol): 1.0}

    dn = df.loc[df["is_limit_down_close"], ["date", "symbol"]].drop_duplicates()
    for r in dn.itertuples(index=False):
        i = idx.get(str(r.date))
        if i is None or i < 2:
            continue
        # prefer enter earlier unless a seal-up signal already owns that slot
        if dates[i - 2] not in out:
            out[dates[i - 2]] = {str(r.symbol): 1.0}
        out[dates[i - 1]] = {}  # all-cash exit attempt into seal-down fill day
    return out


def run_leg_seal_aware(
    df: pd.DataFrame,
    symbols: List[str],
    mode: str,
    rebal_every: int,
    date_start: str,
    date_end: str,
    kappa: float,
    fill_price: str,
    seal_signals: Dict[str, Dict[str, float]],
) -> Tuple[pd.DataFrame, FillStats, Portfolio, Dict[str, float]]:
    sub = df[(df["date"] >= date_start) & (df["date"] <= date_end)].copy()
    dates = sorted(sub["date"].unique())
    port = Portfolio()
    stats = FillStats()
    equity_rows = []
    pending_target: Optional[Dict[str, float]] = None
    px_close: Dict[str, float] = {}

    for i, d in enumerate(dates):
        day = sub[sub["date"] == d]
        px_close = {r.symbol: float(r.close) for r in day.itertuples()}
        px_fill = {r.symbol: float(getattr(r, fill_price)) for r in day.itertuples()}
        bars = {
            r.symbol: {
                "volume": int(r.volume),
                "tradable": bool(r.tradable),
                "is_suspended": bool(r.is_suspended),
                "is_one_word_up": bool(r.is_one_word_up),
                "is_one_word_down": bool(r.is_one_word_down),
                "is_limit_up_close": bool(r.is_limit_up_close),
                "is_limit_down_close": bool(r.is_limit_down_close),
                "board": r.board,
            }
            for r in day.itertuples()
        }

        if pending_target is not None:
            execute_rebalance(
                port, px_fill, pending_target, bars, mode=mode, stats=stats, kappa=kappa, price_field=fill_price
            )
            pending_target = None

        if d in seal_signals:
            pending_target = seal_signals[d]
        elif i % rebal_every == 0:
            pending_target = target_weights_for_day(i, symbols, rebal_every)

        equity_rows.append(
            {
                "date": d,
                "leg": mode,
                "fill_price": fill_price,
                "nav": port.nav(px_close),
                "cash": port.cash,
                "data_mode": "live_expand",
                "FAKE": False,
                "hypothesis_id": "A",
            }
        )

    last_px = px_close if dates else {}
    return pd.DataFrame(equity_rows), stats, port, last_px


def main() -> int:
    params = load_params()
    fill_cfg = params.get("fill") or {}
    fail_policy = params.get("fail_policy", "skip")
    fail_rule = params.get("fail_rule", "close_seal_incl_non_one_word")
    kappa = float((params.get("a1k") or {}).get("kappa", 0.01))
    groups = list(params.get("groups") or ["A0", "A1", "A1k"])
    fake = params.get("fake_run") or {}
    rebal_every = int(fake.get("rebalance_every_sessions", 5))

    if not SAMPLE_PATH.exists():
        raise SystemExit(f"missing sample: {SAMPLE_PATH}")

    raw = pd.read_parquet(SAMPLE_PATH)
    df = enrich_expand_bars(raw)
    symbols = sorted(df["symbol"].unique().tolist())
    d0, d1 = str(df["date"].min()), str(df["date"].max())
    dates = sorted(df["date"].unique())
    if len(dates) < 20:
        raise SystemExit(f"LIVE_EXPAND too short: {len(dates)} dates")

    seal_signals = build_seal_signal_targets(df, dates)

    cut = max(10, int(len(dates) * 0.8))
    cut = min(cut, len(dates) - 5)
    is_a, is_b = dates[0], dates[cut - 1]
    ho_a, ho_b = dates[cut], dates[-1]

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    fill_default = fill_cfg.get("default", "next_open")
    assert fill_default in ("next_open", "open")
    fill_jobs = [("open", "default"), ("close", "robustness")]

    summary_rows = []
    equity_all = []
    for fill_price, fill_role in fill_jobs:
        for seg_name, a, b in (("LIVE_EXPAND_IS", is_a, is_b), ("LIVE_EXPAND_holdout", ho_a, ho_b)):
            mode_map = {}
            for mode in groups:
                eq, st, port, last_px = run_leg_seal_aware(
                    df, symbols, mode, rebal_every, a, b, kappa=kappa, fill_price=fill_price, seal_signals=seal_signals
                )
                eq = eq.copy()
                eq["data_mode"] = "live_expand"
                eq["FAKE"] = False
                mode_map[mode] = (eq, st, port, last_px)
                equity_all.append(eq.assign(segment=seg_name, fill_role=fill_role))
            row = summarize(seg_name, fill_price, mode_map)
            row["data_mode"] = "live_expand"
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
        bdf["data_mode"] = "live_expand"
        bdf["FAKE"] = False
    board_df = pd.concat(
        [board_is.assign(oos="LIVE_EXPAND_IS"), board_ho.assign(oos="LIVE_EXPAND_holdout")],
        ignore_index=True,
    )

    primary_path = OUT_DIR / "summary_LIVE_EXPAND_next_open.csv"
    robust_path = OUT_DIR / "summary_LIVE_EXPAND_next_close_ROBUSTNESS.csv"
    equity_path = OUT_DIR / "equity_curves.csv"
    blocked_path = OUT_DIR / "blocked_and_turnover.csv"
    board_path = OUT_DIR / "board_segment_main_vs_chinext.csv"
    residual_path = OUT_DIR / "end_residual_positions.json"
    enriched_path = OUT_DIR / "enriched_daily_expand_bars.parquet"
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
        "data_mode": "live_expand",
        "LIVE_EXPAND": True,
        "FAKE": False,
        "fail_policy": fail_policy,
        "fail_rule": fail_rule,
        "fill_default": "next_open",
        "disclaimer": "NOT stock advice. LIVE_EXPAND permission-window bars only. No live trading.",
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
        "n_seal_subset_rows": int(pd.read_parquet(SEAL_SUBSET_PATH).shape[0]) if SEAL_SUBSET_PATH.exists() else None,
        "n_seal_signal_days": int(len(seal_signals)),
    }
    evidence_txt = EVIDENCE_PATH.read_text(encoding="utf-8") if EVIDENCE_PATH.exists() else ""

    meta = {
        "as_of": as_of,
        "timezone_note": "Asia/Shanghai (UKING-ZL local)",
        "run_tag": "LIVE_EXPAND",
        "hypothesis_id": "A",
        "hypothesis_doc": HYP_DOC,
        "experiment_id": params.get("experiment_id", "A_limit_up_fill"),
        "data_mode": "live_expand",
        "LIVE_EXPAND": True,
        "FAKE": False,
        "permission_window": f"{PERM_START} .. {PERM_END}",
        "sample_window": f"{d0} .. {d1}",
        "sample_path": "data/daily_expand_window.parquet",
        "sample_sha256": file_sha256(SAMPLE_PATH),
        "sample_rows": int(len(df)),
        "seal_subset_path": "data/seal_event_subset.parquet",
        "expand_seal_evidence_path": "data/expand_seal_evidence.txt",
        "expand_seal_evidence_excerpt": evidence_txt.strip().splitlines()[:16],
        "symbols": symbols,
        "n_sessions": int(df["date"].nunique()),
        "n_codes": int(df["symbol"].nunique()),
        "warning": (
            "LIVE_EXPAND: permission-window JoinQuant bars (25 codes). "
            "Seal-aware dummy + rotation fallback — NOT alpha. NOT stock advice. No live trading."
        ),
        "script": "scripts/run_a0_a1_live_expand.py",
        "core_fill_logic": "scripts/run_a0_a1_fill.py execute_rebalance (imported)",
        "params_path": "params.yaml",
        "fill_default": "next_open",
        "fill_robustness": "next_close_separate_file",
        "fail_policy": fail_policy,
        "fail_rule": fail_rule,
        "groups": groups,
        "kappa": kappa,
        "rebalance_every_sessions": rebal_every,
        "signal": "seal_aware_dummy_plus_fixed_rotation_fallback",
        "signal_note": (
            "On session before close_seal_up, force 100% that symbol so next-open fill hits A1 block; "
            "before close_seal_down, enter then exit into seal day. Elsewhere rotate every N sessions. "
            "NOT a stock pick."
        ),
        "oos_split_note": (
            "LIVE_EXPAND shape-only IS/holdout inside permission window "
            f"({is_a}..{is_b} / {ho_a}..{ho_b}); do NOT tune on holdout."
        ),
        "limit_event_counts": limit_counts,
        "outputs": {
            "summary_default_next_open": "results/live_expand/summary_LIVE_EXPAND_next_open.csv",
            "summary_robustness_next_close": "results/live_expand/summary_LIVE_EXPAND_next_close_ROBUSTNESS.csv",
            "equity": "results/live_expand/equity_curves.csv",
            "blocked_turnover": "results/live_expand/blocked_and_turnover.csv",
            "board_segment": "results/live_expand/board_segment_main_vs_chinext.csv",
            "residual": "results/live_expand/end_residual_positions.json",
            "enriched_bars": "results/live_expand/enriched_daily_expand_bars.parquet",
            "meta": "results/live_expand/RUN_META.json",
            "three_line": "results/live_expand/THREE_LINE_SUMMARY.md",
        },
        "status": "LIVE_EXPAND A0/A1/A1k on permission-window expand bars; seal-aware dummy for blocked>0",
        "git": "not committed (per dispatch)",
    }
    meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")

    p_is = primary[primary["segment"] == "LIVE_EXPAND_IS"].iloc[0]
    p_ho = primary[primary["segment"] == "LIVE_EXPAND_holdout"].iloc[0]
    lines = [
        "# LIVE_EXPAND three-line summary (NOT advice)",
        "",
        f"1. Data: `{SAMPLE_PATH.name}` n_codes={df['symbol'].nunique()} window={d0}..{d1} "
        f"(inside {PERM_START}..{PERM_END}); rows={len(df)}; "
        f"limit_event close_seal_up={limit_counts['n_close_seal_up']} close_seal_down={limit_counts['n_close_seal_down']}; "
        f"seal_signal_days={limit_counts['n_seal_signal_days']}.",
        f"2. next_open LIVE_EXPAND_IS: A0_ret={p_is['A0_total_return']:.6f} A1_ret={p_is['A1_total_return']:.6f} "
        f"A1k_ret={p_is['A1k_total_return']:.6f} gap_A1-A0={p_is['nav_gap_A1_minus_A0']:.6f}; "
        f"A1_blocked_buys={int(p_is['A1_blocked_buys'])} "
        f"(one_word={int(p_is['A1_blocked_buys_one_word'])}, close_seal={int(p_is['A1_blocked_buys_close_seal'])}); "
        f"A1_blocked_sells={int(p_is['A1_blocked_sells'])} "
        f"(close_seal={int(p_is['A1_blocked_sells_close_seal'])}). "
        f"holdout A0_ret={p_ho['A0_total_return']:.6f} A1_ret={p_ho['A1_total_return']:.6f} "
        f"A1_blocked_buys={int(p_ho['A1_blocked_buys'])} A1_blocked_sells={int(p_ho['A1_blocked_sells'])}.",
        "3. Caveat: seal-aware dummy forces targets into known close-seal sessions so blocked reflects limit_event; "
        "NOT a product fillability conclusion; NOT stock advice; no live trading.",
        "",
        f"as_of={as_of}",
    ]
    three_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    (OUT_DIR / "README.txt").write_text(
        "\n".join(
            [
                "results/live_expand — LIVE_EXPAND A0/A1/A1k on JoinQuant permission-window expand bars",
                f"See: {HYP_DOC}",
                "DEFAULT fill = next_open (summary_LIVE_EXPAND_next_open.csv).",
                "next_close is ROBUSTNESS only — do not mix into one NAV number.",
                "Main input = daily_expand_window.parquet (full bars). seal_event_subset is event slice only.",
                "Seal-aware dummy makes A1 blocked_* reflect close-seal events; not an alpha signal.",
                "NOT for investment decisions. No live trading. No stock picks.",
                "Does not overwrite results/live_sample/ or results/fake/.",
                "",
            ]
        ),
        encoding="utf-8",
    )

    print("OK LIVE_EXPAND hypothesis_id=A fill_default=next_open seal_aware=1")
    print(
        primary[
            [
                "segment",
                "A0_total_return",
                "A1_total_return",
                "A1k_total_return",
                "nav_gap_A1_minus_A0",
                "A1_blocked_buys",
                "A1_blocked_buys_close_seal",
                "A1_blocked_sells",
                "A1_blocked_sells_close_seal",
                "A1k_blocked_buys",
                "A1k_kappa_partial_buys",
            ]
        ].to_string(index=False)
    )
    print("limit_event_counts", limit_counts)
    print(f"Wrote {meta_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
