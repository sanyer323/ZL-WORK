#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Experiment A / hypothesis A — A0 vs A1/A1k fillability FAKE dry-run.

Default fill = next_open. next_close is robustness only (separate outputs).
data_mode=fake. NOT real-market conclusions. No live trading.
Aligns with: 智库/金融股票/假设-A-涨停可成交性.md
"""
from __future__ import annotations

import hashlib
import json
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import pandas as pd
import yaml

ROOT = Path(__file__).resolve().parents[1]
PARAMS_PATH = ROOT / "params.yaml"
OUT_DIR = ROOT / "results" / "fake"
HYP_DOC = "智库/金融股票/假设-A-涨停可成交性.md"


def load_params(path: Path = PARAMS_PATH) -> dict:
    with path.open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def parse_range(s: str) -> Tuple[str, str]:
    parts = [p.strip() for p in str(s).replace("..", " ").split() if p.strip() and p.strip() != ".."]
    if len(parts) < 2:
        raise ValueError(f"bad range: {s}")
    return parts[0], parts[1]


def file_sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


@dataclass
class FillStats:
    planned_buys: int = 0
    planned_sells: int = 0
    filled_buys: int = 0
    filled_sells: int = 0
    blocked_buys: int = 0
    blocked_sells: int = 0
    planned_turnover: float = 0.0
    actual_turnover: float = 0.0
    blocked_buys_one_word: int = 0
    blocked_buys_close_seal: int = 0
    blocked_buys_halt: int = 0
    blocked_sells_one_word: int = 0
    blocked_sells_close_seal: int = 0
    blocked_sells_halt: int = 0
    kappa_partial_buys: int = 0
    kappa_partial_sells: int = 0


@dataclass
class Portfolio:
    cash: float = 1.0
    shares: Dict[str, float] = field(default_factory=dict)

    def nav(self, px: Dict[str, float]) -> float:
        v = self.cash
        for sym, sh in self.shares.items():
            v += sh * px.get(sym, 0.0)
        return v

    def weights(self, px: Dict[str, float]) -> Dict[str, float]:
        n = self.nav(px)
        keys = set(self.shares) | set(px)
        if n <= 0:
            return {k: 0.0 for k in keys}
        return {k: (self.shares.get(k, 0.0) * px.get(k, 0.0)) / n for k in keys}


def target_weights_for_day(day_idx: int, symbols: List[str], every: int) -> Dict[str, float]:
    if not symbols:
        return {}
    bucket = (day_idx // every) % len(symbols)
    return {s: (1.0 if i == bucket else 0.0) for i, s in enumerate(symbols)}


def buy_block_reason(bar: dict, mode: str) -> Optional[str]:
    """Return block reason for BUY under A1/A1k, or None if free to try."""
    if mode == "A0":
        return None
    if (not bar.get("tradable", True)) or int(bar.get("volume", 0) or 0) <= 0 or bar.get("is_suspended"):
        return "halt_or_zero_volume"
    if bar.get("is_one_word_up"):
        return "one_word_up"
    # close seal up and not open one-word (one-word already caught)
    if bar.get("is_limit_up_close") and not bar.get("is_one_word_up"):
        if mode == "A1":
            return "close_seal_up_hard"
        if mode == "A1k":
            return "close_seal_up_kappa"  # partial, not full block
    return None


def sell_block_reason(bar: dict, mode: str) -> Optional[str]:
    if mode == "A0":
        return None
    if (not bar.get("tradable", True)) or int(bar.get("volume", 0) or 0) <= 0 or bar.get("is_suspended"):
        return "halt_or_zero_volume"
    if bar.get("is_one_word_down"):
        return "one_word_down"
    if bar.get("is_limit_down_close") and not bar.get("is_one_word_down"):
        if mode == "A1":
            return "close_seal_down_hard"
        if mode == "A1k":
            return "close_seal_down_kappa"
    return None


def execute_rebalance(
    port: Portfolio,
    px: Dict[str, float],
    target_w: Dict[str, float],
    bars: Dict[str, dict],
    mode: str,
    stats: FillStats,
    kappa: float,
    price_field: str,
) -> None:
    nav0 = port.nav(px)
    if nav0 <= 0:
        return
    cur_w = port.weights(px)
    syms = sorted(set(cur_w) | set(target_w) | set(px))

    planned = sum(abs(target_w.get(s, 0.0) - cur_w.get(s, 0.0)) for s in syms)
    stats.planned_turnover += planned * 0.5

    # sells first
    for s in syms:
        tw = target_w.get(s, 0.0)
        cw = cur_w.get(s, 0.0)
        if tw >= cw - 1e-15:
            continue
        stats.planned_sells += 1
        price = float(px.get(s, 0.0))
        if price <= 0:
            stats.blocked_sells += 1
            continue
        bar = bars.get(s, {})
        reason = sell_block_reason(bar, mode)
        desired_val = tw * nav0
        cur_val = port.shares.get(s, 0.0) * price
        sell_val = cur_val - desired_val
        if reason in ("halt_or_zero_volume", "one_word_down", "close_seal_down_hard"):
            stats.blocked_sells += 1
            if reason == "one_word_down":
                stats.blocked_sells_one_word += 1
            elif reason == "close_seal_down_hard":
                stats.blocked_sells_close_seal += 1
            else:
                stats.blocked_sells_halt += 1
            continue
        if reason == "close_seal_down_kappa":
            # cap sold shares by kappa * day volume
            max_shares = kappa * float(bar.get("volume", 0))
            sh_intent = sell_val / price
            sh = min(sh_intent, max_shares)
            if sh <= 0:
                stats.blocked_sells += 1
                stats.blocked_sells_close_seal += 1
                continue
            sell_val = sh * price
            stats.kappa_partial_sells += 1
        else:
            sh = sell_val / price
        port.shares[s] = port.shares.get(s, 0.0) - sh
        if abs(port.shares.get(s, 0.0)) < 1e-12:
            port.shares.pop(s, None)
        port.cash += sell_val
        stats.filled_sells += 1
        stats.actual_turnover += (sell_val / nav0) * 0.5

    nav1 = port.nav(px)
    cur_w = port.weights(px)

    for s in syms:
        tw = target_w.get(s, 0.0)
        cw = cur_w.get(s, 0.0)
        if tw <= cw + 1e-15:
            continue
        stats.planned_buys += 1
        price = float(px.get(s, 0.0))
        if price <= 0:
            stats.blocked_buys += 1
            continue
        bar = bars.get(s, {})
        reason = buy_block_reason(bar, mode)
        desired_val = tw * nav1
        cur_val = port.shares.get(s, 0.0) * price
        buy_val = desired_val - cur_val
        if reason in ("halt_or_zero_volume", "one_word_up", "close_seal_up_hard"):
            stats.blocked_buys += 1
            if reason == "one_word_up":
                stats.blocked_buys_one_word += 1
            elif reason == "close_seal_up_hard":
                stats.blocked_buys_close_seal += 1
            else:
                stats.blocked_buys_halt += 1
            continue
        if reason == "close_seal_up_kappa":
            max_shares = kappa * float(bar.get("volume", 0))
            sh_intent = buy_val / price
            sh = min(sh_intent, max_shares)
            if sh <= 0:
                stats.blocked_buys += 1
                stats.blocked_buys_close_seal += 1
                continue
            buy_val = sh * price
            stats.kappa_partial_buys += 1
        buy_val = min(buy_val, port.cash)
        if buy_val <= 0:
            continue
        sh = buy_val / price
        port.shares[s] = port.shares.get(s, 0.0) + sh
        port.cash -= buy_val
        stats.filled_buys += 1
        stats.actual_turnover += (buy_val / nav1) * 0.5


def run_leg(
    df: pd.DataFrame,
    symbols: List[str],
    mode: str,
    rebal_every: int,
    date_start: str,
    date_end: str,
    kappa: float,
    fill_price: str,
) -> Tuple[pd.DataFrame, FillStats, Portfolio, Dict[str, float]]:
    """fill_price: 'open' (default) or 'close' (robustness). Signal at d, fill at d+1."""
    sub = df[(df["date"] >= date_start) & (df["date"] <= date_end)].copy()
    dates = sorted(sub["date"].unique())
    port = Portfolio()
    stats = FillStats()
    equity_rows = []
    pending_target: Optional[Dict[str, float]] = None

    for i, d in enumerate(dates):
        day = sub[sub["date"] == d]
        # mark-to-market always at close for equity curve continuity
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

        if i % rebal_every == 0:
            pending_target = target_weights_for_day(i, symbols, rebal_every)

        equity_rows.append(
            {
                "date": d,
                "leg": mode,
                "fill_price": fill_price,
                "nav": port.nav(px_close),
                "cash": port.cash,
                "data_mode": "fake",
                "FAKE": True,
                "hypothesis_id": "A",
            }
        )

    last_px = px_close if dates else {}
    return pd.DataFrame(equity_rows), stats, port, last_px


def summarize(seg: str, fill_price: str, mode_map: dict) -> dict:
    # mode_map: mode -> (eq, stats, port, last_px)
    a0 = mode_map["A0"]
    rows = {
        "segment": seg,
        "fill_price": fill_price,
        "data_mode": "fake",
        "FAKE": True,
        "hypothesis_id": "A",
        "baseline": "A0_naive_next_open" if fill_price == "open" else "A0_naive_next_close_robustness",
    }

    def tret(eq: pd.DataFrame) -> float:
        if eq is None or eq.empty:
            return float("nan")
        return float(eq["nav"].iloc[-1] / eq["nav"].iloc[0] - 1.0)

    for mode, (eq, st, port, last_px) in mode_map.items():
        rows[f"{mode}_total_return"] = tret(eq)
        rows[f"{mode}_end_nav"] = float(eq["nav"].iloc[-1]) if len(eq) else None
        rows[f"{mode}_planned_turnover"] = st.planned_turnover
        rows[f"{mode}_actual_turnover"] = st.actual_turnover
        rows[f"{mode}_blocked_buys"] = st.blocked_buys
        rows[f"{mode}_blocked_sells"] = st.blocked_sells
        rows[f"{mode}_blocked_buys_one_word"] = st.blocked_buys_one_word
        rows[f"{mode}_blocked_buys_close_seal"] = st.blocked_buys_close_seal
        rows[f"{mode}_blocked_buys_halt"] = st.blocked_buys_halt
        rows[f"{mode}_blocked_sells_one_word"] = st.blocked_sells_one_word
        rows[f"{mode}_blocked_sells_close_seal"] = st.blocked_sells_close_seal
        rows[f"{mode}_blocked_sells_halt"] = st.blocked_sells_halt
        rows[f"{mode}_kappa_partial_buys"] = st.kappa_partial_buys
        rows[f"{mode}_end_cash"] = port.cash
        rows[f"{mode}_end_residual_weights"] = json.dumps(port.weights(last_px), ensure_ascii=False)

    eq0 = a0[0]
    for mode in mode_map:
        if mode == "A0":
            continue
        eq = mode_map[mode][0]
        if len(eq0) and len(eq):
            rows[f"nav_gap_{mode}_minus_A0"] = float(eq["nav"].iloc[-1] - eq0["nav"].iloc[-1])
            rows[f"return_gap_{mode}_minus_A0"] = tret(eq) - tret(eq0)
    return rows


def board_segment_table(df: pd.DataFrame, date_start: str, date_end: str) -> pd.DataFrame:
    sub = df[(df["date"] >= date_start) & (df["date"] <= date_end)]
    rows = []
    for board, g in sub.groupby("board"):
        rows.append(
            {
                "segment_window": f"{date_start}..{date_end}",
                "board": board,
                "limit_pct": float(g["limit_pct"].iloc[0]),
                "n_bars": int(len(g)),
                "n_one_word_up": int(g["is_one_word_up"].sum()),
                "n_one_word_down": int(g["is_one_word_down"].sum()),
                "n_close_seal_up": int(g["is_limit_up_close"].sum()),
                "n_close_seal_down": int(g["is_limit_down_close"].sum()),
                "n_suspended": int(g["is_suspended"].sum()),
                "data_mode": "fake",
                "FAKE": True,
                "hypothesis_id": "A",
            }
        )
    return pd.DataFrame(rows)


def main() -> int:
    params = load_params()
    fake = params.get("fake_run") or {}
    fill_cfg = params.get("fill") or {}
    fail_policy = params.get("fail_policy", fake.get("fail_policy", "skip"))
    if fail_policy != "skip":
        print(f"WARN: fake dry-run implements skip only; params fail_policy={fail_policy}", file=sys.stderr)

    kappa = float((params.get("a1k") or {}).get("kappa", fake.get("kappa", 0.01)))
    groups = list((params.get("groups") or fake.get("groups") or ["A0", "A1", "A1k"]))
    rebal_every = int(fake.get("rebalance_every_sessions", 5))

    data_path = ROOT / fake.get("data_path", "data/fake_daily_bars.parquet")
    if not data_path.exists():
        sys.path.insert(0, str(ROOT / "scripts"))
        from gen_fake_daily import main as gen_main

        gen_main()
    df = pd.read_parquet(data_path)
    symbols = sorted(df["symbol"].unique().tolist())

    oos = params.get("oos_split") or {}
    is_a, is_b = parse_range(oos.get("in_sample", "2021-01-01 .. 2023-12-31"))
    ho_a, ho_b = parse_range(oos.get("holdout", "2024-01-01 .. 2024-09-30"))
    ho_b = fake.get("holdout_end", ho_b)

    costs = params.get("costs") or {}
    cost_ph = fake.get("costs_placeholder") or {}
    cost_meta = {
        "costs.enabled": bool(costs.get("enabled", False)),
        "t_plus_one": costs.get("t_plus_one", True),
        "commission_rate_placeholder": cost_ph.get("commission_rate", 0.0003),
        "slippage_bps_placeholder": cost_ph.get("slippage_bps", 5),
        "note": cost_ph.get(
            "note",
            "costs.enabled=false for experiment A; placeholders for experiment B",
        ),
    }

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    # Default fill = open; close = robustness separate
    fill_default = fill_cfg.get("default", "next_open")
    assert fill_default in ("next_open", "open")
    fill_jobs = [("open", "default"), ("close", "robustness")]

    summary_rows = []
    equity_all = []
    for fill_price, fill_role in fill_jobs:
        for seg_name, a, b in (("IS", is_a, is_b), ("holdout", ho_a, ho_b)):
            mode_map = {}
            for mode in groups:
                eq, st, port, last_px = run_leg(
                    df, symbols, mode, rebal_every, a, b, kappa=kappa, fill_price=fill_price
                )
                mode_map[mode] = (eq, st, port, last_px)
                equity_all.append(eq.assign(segment=seg_name, fill_role=fill_role))
            row = summarize(seg_name, fill_price, mode_map)
            row["fill_role"] = fill_role
            row["fail_policy"] = fail_policy
            summary_rows.append(row)

    summary_df = pd.DataFrame(summary_rows)
    equity_df = pd.concat(equity_all, ignore_index=True)

    # Primary table = next_open only (do not mix with close)
    primary = summary_df[summary_df["fill_price"] == "open"].copy()
    robust = summary_df[summary_df["fill_price"] == "close"].copy()

    board_is = board_segment_table(df, is_a, is_b)
    board_ho = board_segment_table(df, ho_a, ho_b)
    board_df = pd.concat([board_is.assign(oos="IS"), board_ho.assign(oos="holdout")], ignore_index=True)

    primary_path = OUT_DIR / "summary_IS_holdout_next_open.csv"
    robust_path = OUT_DIR / "summary_IS_holdout_next_close_ROBUSTNESS.csv"
    equity_path = OUT_DIR / "equity_curves.csv"
    blocked_path = OUT_DIR / "blocked_and_turnover.csv"
    board_path = OUT_DIR / "board_segment_main_vs_chinext.csv"
    residual_path = OUT_DIR / "end_residual_positions.json"
    meta_path = OUT_DIR / "RUN_META.json"

    primary.to_csv(primary_path, index=False)
    robust.to_csv(robust_path, index=False)
    equity_df.to_csv(equity_path, index=False)
    board_df.to_csv(board_path, index=False)

    blocked_cols = [
        c
        for c in primary.columns
        if "blocked" in c or "turnover" in c or c in ("segment", "fill_price", "FAKE", "data_mode", "hypothesis_id")
        or c.startswith("nav_gap")
        or c.startswith("return_gap")
    ]
    primary[blocked_cols].to_csv(blocked_path, index=False)

    residual = {
        "hypothesis_id": "A",
        "data_mode": "fake",
        "FAKE": True,
        "fail_policy": fail_policy,
        "fill_default": "next_open",
        "note": "Residuals from DEFAULT next_open legs only",
        "rows": primary[
            ["segment", "A0_end_residual_weights", "A1_end_residual_weights", "A1k_end_residual_weights", "A0_end_cash", "A1_end_cash", "A1k_end_cash"]
        ].to_dict(orient="records"),
    }
    residual_path.write_text(json.dumps(residual, ensure_ascii=False, indent=2), encoding="utf-8")

    as_of = datetime.now().astimezone().isoformat(timespec="seconds")
    meta = {
        "as_of": as_of,
        "timezone_note": "Asia/Shanghai (UKING-ZL local)",
        "hypothesis_id": "A",
        "hypothesis_doc": HYP_DOC,
        "experiment_id": params.get("experiment_id", "A_limit_up_fill"),
        "data_mode": "fake",
        "FAKE": True,
        "warning": "FAKE dry-run only. Do NOT treat as real backtest conclusions or stock advice.",
        "script": "scripts/run_a0_a1_fill.py",
        "params_path": "params.yaml",
        "fake_data_path": str(data_path.relative_to(ROOT)).replace("\\", "/"),
        "fake_data_sha256": file_sha256(data_path),
        "fill_default": "next_open",
        "fill_robustness": "next_close_separate_file",
        "fail_policy": fail_policy,
        "groups": groups,
        "kappa": kappa,
        "rebalance_every_sessions": rebal_every,
        "signal": "dummy_fixed_rotation_100pct_one_symbol",
        "legs": {
            "A0": "naive next_open 100% fill; limits/halts ignored",
            "A1": "honest-hard: one-word-up buy=0; one-word-down sell=0; close-seal-up buy=0; close-seal-down sell=0; halt/zero-vol fail",
            "A1k": "same as A1 but non-one-word close-seal buys/sells capped by kappa*day_volume",
        },
        "limit_rule": "unadjusted OHLC + pre_close; round_half_up to 0.01",
        "oos_split": {
            "in_sample": f"{is_a} .. {is_b}",
            "holdout": f"{ho_a} .. {ho_b}",
            "rule": oos.get("rule"),
            "holdout_not_used_for_tuning": True,
        },
        "costs_assumptions": cost_meta,
        "board_segments": ["main", "chi_next"],
        "outputs": {
            "summary_default_next_open": "results/fake/summary_IS_holdout_next_open.csv",
            "summary_robustness_next_close": "results/fake/summary_IS_holdout_next_close_ROBUSTNESS.csv",
            "equity": "results/fake/equity_curves.csv",
            "blocked_turnover": "results/fake/blocked_and_turnover.csv",
            "board_segment": "results/fake/board_segment_main_vs_chinext.csv",
            "residual": "results/fake/end_residual_positions.json",
        },
        "self_check": {
            "unadjusted_limit_judge": True,
            "fill_open_close_not_mixed": True,
            "halt_fails": True,
            "after_hours_fixed_price_default_off": True,
            "holdout_not_tuned": True,
        },
        "status": "scaffold + fake dry-run",
    }
    meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")

    (OUT_DIR / "README.txt").write_text(
        "\n".join(
            [
                "results/fake — FAKE dry-run outputs for hypothesis A",
                f"See: {HYP_DOC}",
                "DEFAULT fill = next_open (summary_IS_holdout_next_open.csv).",
                "next_close is ROBUSTNESS only — do not mix into one NAV number.",
                "All numbers use synthetic bars (data_mode=fake). Not for investment decisions.",
                "Holdout was NOT used for tuning.",
                "",
            ]
        ),
        encoding="utf-8",
    )

    print("OK fake dry-run hypothesis_id=A fill_default=next_open")
    print(primary[["segment", "A0_total_return", "A1_total_return", "A1k_total_return", "nav_gap_A1_minus_A0"]].to_string(index=False))
    print(f"Wrote {meta_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
