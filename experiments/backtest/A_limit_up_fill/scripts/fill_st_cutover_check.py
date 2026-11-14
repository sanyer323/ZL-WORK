#!/usr/bin/env python3
"""按切日抽检口径读新 parquet，挑选切日前/后各一行，打印是否达标。

不监听 8765，不登录，不引用扩样复跑脚本。
没有真数文件时用 --demo 跑合成夹具，只在内存里演示。
合成行不写入 data/，也不能当成抽检过关。
本脚本只打印，不改 results/live_sample/ST_CUTOVER_CHECK.md。
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import st_cutover_fetch_server as st

ROOT = st.ROOT
DATA = st.DATA
OUT_PQ = st.OUT_PQ
OUT_META = st.OUT_META


def _tradable(row: dict) -> bool:
    return (not bool(row.get("paused"))) and int(row.get("volume") or 0) > 0


def _in_sample(date_s: str) -> bool:
    return bool(date_s) and st.START <= date_s <= st.END and st.PERM_START <= date_s <= st.PERM_END


def window_counts(rows: list[dict]) -> dict[str, int]:
    counts = {"early": 0, "late": 0, "empty": 0, "outside_sample": 0, "in_window": 0}
    for row in rows:
        date_s = st.norm_date(row.get("date"))
        if not date_s:
            counts["empty"] += 1
        elif date_s < st.PERM_START:
            counts["early"] += 1
        elif date_s > st.PERM_END:
            counts["late"] += 1
        elif date_s < st.START or date_s > st.END:
            counts["outside_sample"] += 1
        else:
            counts["in_window"] += 1
    return counts


def _pre_key(row: dict) -> tuple:
    return (0 if _tradable(row) else 1, str(row.get("date")))


def _post_key(row: dict) -> tuple:
    date_s = str(row.get("date"))
    tradable = 0 if _tradable(row) else 1
    if str(row.get("code")) == st.NAME_CHANGE_CODE:
        in_star = 0 if "2026-07-06" <= date_s <= "2026-07-29" else 1
        return (tradable, in_star, date_s)
    on_cut = 0 if date_s == st.CUTOVER else 1
    return (tradable, on_cut, date_s)


def _side_rows(rows: list[dict], code: str, *, before: bool) -> list[dict]:
    found = []
    for row in rows:
        date_s = st.norm_date(row.get("date"))
        if str(row.get("code")) != code or not _in_sample(date_s):
            pass
        elif row.get("st_flag") not in {"ST", "*ST"} or not bool(row.get("st")):
            pass
        elif before and date_s < st.CUTOVER:
            found.append(row)
        elif (not before) and date_s >= st.CUTOVER:
            found.append(row)
    if before:
        found.sort(key=_pre_key)
        if found:
            tradable = [row for row in found if _tradable(row)]
            pool = tradable or found
            pool.sort(key=lambda row: str(row.get("date")), reverse=True)
            return pool
        return found
    found.sort(key=_post_key)
    return found


def choose_pairs(rows: list[dict]) -> list[tuple[dict, dict]]:
    pairs = []
    normalized = []
    for row in rows:
        item = dict(row)
        item["date"] = st.norm_date(row.get("date"))
        normalized.append(item)
    for code in st.CODES:
        pre = _side_rows(normalized, code, before=True)
        post = _side_rows(normalized, code, before=False)
        if pre and post:
            pairs.append((pre[0], post[0]))
    return pairs


def _prices_match(row: dict) -> bool:
    up, down = st.limit_prices(float(row["pre_close"]), float(row["limit_pct"]))
    return abs(up - float(row["limit_up"])) < 1e-8 and abs(down - float(row["limit_down"])) < 1e-8


def _expected_pct(date_s: str) -> str:
    return "0.05" if date_s < st.CUTOVER else "0.10"


def assess(rows: list[dict], meta: dict, *, source: str) -> dict:
    counts = window_counts(rows)
    rule_problems: list[str] = []
    if counts["early"] or counts["late"] or counts["empty"] or counts["outside_sample"]:
        rule_problems.append(
            "越窗 "
            f"early={counts['early']} late={counts['late']} "
            f"empty={counts['empty']} outside_sample={counts['outside_sample']}"
        )
    for row in rows:
        date_s = st.norm_date(row.get("date"))
        code = str(row.get("code") or "")
        if code.startswith("300") or code.startswith("301") or code.startswith("688"):
            rule_problems.append(f"300/301/688 code={code} date={date_s}")
        if row.get("st_flag") == "退市整理":
            rule_problems.append(f"退市整理 code={code} date={date_s}")
    in_window = []
    for row in rows:
        item = dict(row)
        item["date"] = st.norm_date(row.get("date"))
        if _in_sample(item["date"]):
            in_window.append(item)
    for row in in_window:
        if row.get("st_flag") in {"ST", "*ST"} and row.get("board") == "main":
            expected = _expected_pct(str(row["date"]))
            if not st.pct_equals(row.get("limit_pct"), expected):
                rule_problems.append(
                    f"pct code={row.get('code')} date={row.get('date')} "
                    f"got={row.get('limit_pct')} expected={expected}"
                )
            elif not _prices_match(row):
                rule_problems.append(
                    f"limit price mismatch code={row.get('code')} date={row.get('date')}"
                )
    conflicts = st.name_change_conflicts(in_window)
    rule_problems.extend(conflicts)
    pairs = choose_pairs(rows)
    pair = pairs[0] if pairs else None
    if pair is None:
        rule_problems.append("缺少同一标的切日前与切日后各一行")
    else:
        pre, post = pair
        if str(pre.get("code")) != str(post.get("code")):
            rule_problems.append("切日前/后不是同一证券")
        if str(pre.get("date")) >= st.CUTOVER or str(post.get("date")) < st.CUTOVER:
            rule_problems.append("切日前后日期放反了")
        if not _tradable(pre) or not _tradable(post):
            rule_problems.append("选中的样本不是可交易日")
        if str(post.get("code")) == st.NAME_CHANGE_CODE and str(post.get("date")) == "2026-07-30":
            rule_problems.append("000793 的 2026-07-30 全日停牌，不能当唯一切日后样本")
        if not st.pct_equals(pre.get("limit_pct"), "0.05") or not st.pct_equals(post.get("limit_pct"), "0.10"):
            rule_problems.append("选中行的幅度不是 0.05 / 0.10")
    fq = meta.get("fq", "MISSING")
    if fq is not None:
        rule_problems.append(f"fq 不是 null：{fq!r}")
    if meta.get("price_rule") not in (None, "board_st_day_effective") and source == "joinquant":
        rule_problems.append("price_rule 不是 board_st_day_effective")
    blockers: list[str] = []
    if source != "joinquant" or meta.get("synthetic") is True or meta.get("vendor") != "joinquant/jqdatasdk":
        blockers.append("没有聚宽真数交件，抽检不能过关")
    if meta.get("sample_id") not in (None, "st_cutover") and source == "joinquant":
        blockers.append("sample_id 不是 st_cutover")
    gate_passed = source == "joinquant" and not rule_problems and not blockers
    demo_consistent = source == "synthetic" and not rule_problems
    text = render_report(
        pair=pair,
        extras=pairs[1:] if pairs else [],
        rule_problems=rule_problems,
        blockers=blockers,
        counts=counts,
        gate_passed=gate_passed,
        demo_consistent=demo_consistent,
        source=source,
    )
    return {
        "text": text,
        "gate_passed": gate_passed,
        "demo_consistent": demo_consistent,
        "pair": pair,
        "extras": pairs[1:] if pairs else [],
        "rule_problems": rule_problems,
        "blockers": blockers,
        "counts": counts,
    }


def _cell(row: dict, pct_label: str) -> str:
    ohlc = f"{row['open']} / {row['high']} / {row['low']} / {row['close']}"
    return "\n".join(
        [
            f"| code | {row['code']} |",
            f"| trade_date | {row['date']} |",
            f"| board / st_flag | {row['board']} / {row['st_flag']} |",
            f"| pre_close | {row['pre_close']} |",
            f"| pct_used | {st.pct_text(row['limit_pct'])} |",
            f"| limit_up | {row['limit_up']} |",
            f"| limit_down | {row['limit_down']} |",
            f"| open / high / low / close | {ohlc} |",
            f"| volume | {row['volume']} |",
            f"| one_word_up / close_seal_up | {row['is_one_word_up']} / {row['is_limit_up_close']} |",
            "| 判板依据 | 未复权；前收盘/除权参考价；非复权价 |",
            f"| 期望幅度 | {pct_label} |",
        ]
    )


def render_report(*, pair, extras, rule_problems, blockers, counts, gate_passed, demo_consistent, source: str) -> str:
    pre_ok = pair is not None and st.pct_equals(pair[0].get("limit_pct"), "0.05")
    post_ok = pair is not None and st.pct_equals(pair[1].get("limit_pct"), "0.10")
    fq_ok = "fq 不是 null" not in " | ".join(rule_problems)
    suffix = "（仅合成，不是真数过关）" if source != "joinquant" else ""
    lines = [
        f"真数抽检是否达标: {'是' if gate_passed else '否'}",
        f"GATE_PASSED={'yes' if gate_passed else 'no'}",
        f"来源: {source}",
    ]
    if source == "synthetic":
        lines.append(f"合成规则演示是否自洽: {'是' if demo_consistent else '否'}")
        lines.append(f"DEMO_CONSISTENT={'yes' if demo_consistent else 'no'}")
        lines.append("说明: 合成行不是真数交件，不能当成抽检过关。")
    lines.append("")
    if pair is None:
        lines.append("没有凑齐同一标的的切日前/后各一行。")
    else:
        pre, post = pair
        lines.extend(
            [
                "## 样本 A · 切日前（期望 pct=0.05）",
                "",
                "| 字段 | 值 |",
                "|------|-----|",
                _cell(pre, "0.05"),
                "",
                "## 样本 B · 切日及以后（期望 pct=0.10）",
                "",
                "| 字段 | 值 |",
                "|------|-----|",
                _cell(post, "0.10"),
                "",
            ]
        )
    lines.extend(
        [
            "## 结论",
            "",
            "| 项 | 值 |",
            "|----|-----|",
            f"| 切日前 5% 正确 | {'是' if pre_ok else '否'}{suffix} |",
            f"| 切日后 10% 正确 | {'是' if post_ok else '否'}{suffix} |",
            f"| 未用复权判板 | {'是' if fq_ok else '否'}{suffix} |",
            f"| 门禁 | {'过' if gate_passed else '未过'} |",
            "",
            (
                "越窗计数: "
                f"early={counts['early']} late={counts['late']} "
                f"empty={counts['empty']} outside_sample={counts['outside_sample']} "
                f"in_window={counts['in_window']}"
            ),
        ]
    )
    if extras:
        lines.append("")
        lines.append("附加对照（不代替上面这一对最低样本）:")
        for pre, post in extras:
            lines.append(
                f"- {pre['code']} {pre['date']} {pre['st_flag']} {st.pct_text(pre['limit_pct'])}"
                f" / {post['date']} {post['st_flag']} {st.pct_text(post['limit_pct'])}"
            )
    if rule_problems:
        lines.append("")
        lines.append("规则问题:")
        for item in rule_problems:
            lines.append(f"- {item}")
    if blockers:
        lines.append("")
        lines.append("过关阻断:")
        for item in blockers:
            lines.append(f"- {item}")
    lines.append("")
    return "\n".join(lines)


def _data_names() -> set[str]:
    if not DATA.exists():
        return set()
    return {path.name for path in DATA.iterdir()}


def _demo_rows() -> list[dict]:
    specs = [
        ("000911.XSHE", "2026-07-03", "*ST", "*ST广糖"),
        ("000911.XSHE", "2026-07-06", "*ST", "*ST广糖"),
        ("000793.XSHE", "2026-07-03", "*ST", "*ST华闻"),
        ("000793.XSHE", "2026-07-08", "*ST", "*ST华闻"),
        ("000793.XSHE", "2026-07-31", "ST", "ST华闻"),
        ("603378.XSHG", "2026-06-15", "*ST", "*ST亚士"),
        ("603378.XSHG", "2026-07-15", "*ST", "*ST亚士"),
    ]
    raw = []
    for code, date_s, flag, name in specs:
        raw.append(
            {
                "date": date_s,
                "code": code,
                "st_flag": flag,
                "name": name,
                "is_st": True,
                "pre_close": 10,
                "open": 10,
                "high": 10.2,
                "low": 9.8,
                "close": 10.1,
                "volume": 1000,
                "money": 10000,
                "paused": False,
            }
        )
    return st.enrich_rows(raw)


def run_demo() -> int:
    before = _data_names()
    rows = _demo_rows()
    meta = {
        "fq": None,
        "vendor": "synthetic",
        "synthetic": True,
        "sample_id": "st_cutover",
        "price_rule": "board_st_day_effective",
    }
    result = assess(rows, meta, source="synthetic")
    bad = dict(rows[0])
    bad["date"] = "2025-08-04"
    bad_result = assess([bad], meta, source="synthetic")
    outside = dict(rows[0])
    outside["date"] = "2026-05-31"
    outside_result = assess([outside], meta, source="synthetic")
    print(result["text"], end="")
    print(
        "负例越权限窗: "
        f"early={bad_result['counts']['early']} "
        f"GATE_PASSED={'yes' if bad_result['gate_passed'] else 'no'} "
        f"DEMO_CONSISTENT={'yes' if bad_result['demo_consistent'] else 'no'}"
    )
    print(
        "负例越抽检窗: "
        f"outside_sample={outside_result['counts']['outside_sample']} "
        f"GATE_PASSED={'yes' if outside_result['gate_passed'] else 'no'}"
    )
    if _data_names() != before:
        print("DEMO_WROTE_DATA=yes")
        return 1
    pair = result["pair"]
    extras = {str(pre["code"]): (pre, post) for pre, post in result["extras"]}
    huawen = extras.get("000793.XSHE")
    ok = (
        result["gate_passed"] is False
        and result["demo_consistent"] is True
        and pair is not None
        and pair[0]["code"] == "000911.XSHE"
        and pair[0]["date"] == "2026-07-03"
        and pair[1]["date"] == "2026-07-06"
        and huawen is not None
        and huawen[1]["date"] == "2026-07-08"
        and huawen[1]["st_flag"] == "*ST"
        and bad_result["counts"]["early"] == 1
        and bad_result["gate_passed"] is False
        and bad_result["counts"]["in_window"] == 0
        and outside_result["counts"]["outside_sample"] == 1
        and outside_result["gate_passed"] is False
    )
    if not ok:
        print("DEMO_ASSERT=fail")
        return 1
    print("DEMO_ASSERT=ok")
    print("DEMO_WROTE_DATA=no")
    return 0


def _records_from_parquet(path: Path) -> list[dict]:
    import pandas as pd

    frame = pd.read_parquet(path)
    rows = frame.to_dict(orient="records")
    cleaned = []
    for row in rows:
        item = {}
        for key, value in row.items():
            if value is not None:
                try:
                    if value != value:
                        value = None
                except Exception:
                    pass
            item[key] = value
        item["date"] = st.norm_date(item.get("date"))
        cleaned.append(item)
    return cleaned


def run_real() -> int:
    if not OUT_PQ.exists():
        print("真数抽检是否达标: 否")
        print("GATE_PASSED=no")
        print(f"来源: missing")
        print(f"原因: 还没有 {OUT_PQ.name}。本轮不拉数，抽检未过关。")
        return 2
    meta = {}
    if OUT_META.exists():
        meta = json.loads(OUT_META.read_text(encoding="utf-8"))
    rows = _records_from_parquet(OUT_PQ)
    source = "joinquant"
    if meta.get("synthetic") is True or meta.get("vendor") != "joinquant/jqdatasdk":
        source = "unverified"
    result = assess(rows, meta, source=source)
    print(result["text"], end="")
    if result["counts"]["early"] or result["counts"]["late"] or result["counts"]["empty"] or result["counts"]["outside_sample"]:
        raise SystemExit("ABORT st_cutover check found out-of-window rows")
    return 0 if result["gate_passed"] else 1


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if "--demo" in args:
        return run_demo()
    if args:
        raise SystemExit("ABORT unknown args; use --demo or no args to read the parquet")
    return run_real()


if __name__ == "__main__":
    raise SystemExit(main())
