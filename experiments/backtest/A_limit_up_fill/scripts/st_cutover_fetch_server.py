#!/usr/bin/env python3
"""实验A · ST切日抽检取数。

独立入口，只服务后续 UKING-ZL 人在环拉三只主板 ST/*ST 的切日样本。
默认监听 127.0.0.1:8765。密码只留在本次请求内存里，不写盘，用后置空。

--self-check 只用合成行验证规则，不监听端口、不登录、不写 data/。
"""
from __future__ import annotations

import hashlib
import json
import sys
import threading
import traceback
from datetime import datetime, timedelta, timezone
from decimal import Decimal, ROUND_HALF_UP
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import parse_qs

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT_PQ = DATA / "daily_st_cutover_window.parquet"
OUT_META = DATA / "daily_st_cutover_window_meta.json"
OUT_EV = DATA / "st_cutover_evidence.txt"

# 抽检窗必须是权限窗的子集。权限窗对照用 U+FF5E。
PERM_START = "2025-08-05"
PERM_END = "2026-08-12"
PERM_WINDOW_LABEL = "2025-08-05" + "\uFF5E" + "2026-08-12"
START = "2026-06-01"
END = "2026-08-12"
CUTOVER = "2026-07-06"
NAME_CHANGE_DATE = "2026-07-31"
NAME_CHANGE_CODE = "000793.XSHE"

CODES = (
    "000911.XSHE",
    "000793.XSHE",
    "603378.XSHG",
)

USER = "18930501903"
HOST, PORT = "127.0.0.1", 8765
TICK = Decimal("0.01")
PCT_PRE = Decimal("0.05")
PCT_POST = Decimal("0.10")
PCT_MAIN = Decimal("0.10")

PAGE_TITLE = "实验A" + " " + "\u00b7" + " " + "ST切日抽检取数"

COLUMNS = (
    "date",
    "code",
    "symbol",
    "board",
    "st",
    "st_flag",
    "name",
    "is_st",
    "limit_pct",
    "pre_close",
    "open",
    "high",
    "low",
    "close",
    "volume",
    "money",
    "paused",
    "limit_up",
    "limit_down",
    "is_one_word_up",
    "is_one_word_down",
    "is_limit_up_close",
    "is_limit_down_close",
    "is_suspended",
)

STATUS = {"state": "waiting", "detail": ""}
REJECT_LOG: list[str] = []
SERVE_CALLED = False
FETCH_CALLED = False

HTML = f"""<!doctype html><meta charset=utf-8><title>{PAGE_TITLE}</title>
<body style="font-family:sans-serif;max-width:32rem;margin:3rem auto">
<h1>{PAGE_TITLE}</h1>
<p>仅本机 127.0.0.1:8765。密码只在本次请求里交给本机 jqdatasdk，不外传、不落盘，用后置空。</p>
<p>抽检窗 {START} 至 {END}，且必须是权限窗 {PERM_WINDOW_LABEL} 的子集。</p>
<p>码表只有 000911.XSHE、000793.XSHE、603378.XSHG。鉴权后除未复权行情外，还要逐日核对 ST 状态和证券简称。</p>
<p>000793 在 {NAME_CHANGE_DATE} 有简称变更，不会整段窗打同一个静态标记。</p>
<form method=post>
<label>手机号（固定）<br><input value="{USER}" disabled style="width:100%"></label><br><br>
<label>登录密码<br><input name=password type=password autocomplete=off required style="width:100%"></label><br><br>
<button type=submit>鉴权并取数</button>
</form>
</body>"""


def abort(message: str) -> None:
    text = message if str(message).startswith("ABORT") else f"ABORT {message}"
    REJECT_LOG.append(text)
    raise SystemExit(text)


def assert_sample_window_is_subset() -> None:
    if PERM_WINDOW_LABEL != "2025-08-05\uFF5E2026-08-12":
        abort(f"permission window label must be 2025-08-05\uFF5E2026-08-12, got {PERM_WINDOW_LABEL}")
    if "\uFF5E" not in PERM_WINDOW_LABEL:
        abort("permission window label missing U+FF5E")
    if not (PERM_START <= START <= END <= PERM_END):
        abort(
            f"sample window {START}..{END} is not a subset of {PERM_WINDOW_LABEL}"
        )


def assert_page_title() -> None:
    title = PAGE_TITLE
    if title != "实验A \u00b7 ST切日抽检取数":
        abort(f"HTML title mismatch: {title!r}")
    spot = title.index("A")
    if title[spot + 1] != " " or title[spot + 2] != "\u00b7" or title[spot + 3] != " ":
        abort("HTML title must be A, space, U+00B7, space")
    if f"<title>{PAGE_TITLE}</title>" not in HTML or f"<h1>{PAGE_TITLE}</h1>" not in HTML:
        abort("HTML title is not on the page")
    for banned in ("扩样", "封板", "EXPAND"):
        if banned in HTML:
            abort(f"HTML contains banned wording {banned}")


def assert_output_paths() -> None:
    expected = {
        OUT_PQ.name: "daily_st_cutover_window.parquet",
        OUT_META.name: "daily_st_cutover_window_meta.json",
        OUT_EV.name: "st_cutover_evidence.txt",
    }
    for actual, want in expected.items():
        if actual != want:
            abort(f"output name drifted: {actual}")
    if (HOST, PORT) != ("127.0.0.1", 8765):
        abort("bind must stay 127.0.0.1:8765")


def assert_code_list() -> None:
    if CODES != ("000911.XSHE", "000793.XSHE", "603378.XSHG"):
        abort(f"code list drifted: {CODES}")
    for banned in ("603922", "603557", "002759", "002731", "300", "301", "688"):
        for code in CODES:
            if code.startswith(banned):
                abort(f"locked code list contains {code}")


def lock_constants() -> None:
    assert_sample_window_is_subset()
    assert_page_title()
    assert_output_paths()
    assert_code_list()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def round_half_up(x: float, tick: Decimal = TICK) -> float:
    dec = Decimal(str(x)).quantize(tick, rounding=ROUND_HALF_UP)
    if dec < tick:
        dec = tick
    return float(dec)


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


def pct_equals(value, expected: str) -> bool:
    return Decimal(str(value)) == Decimal(expected)


def pct_text(value) -> str:
    return format(Decimal(str(value)).quantize(Decimal("0.01")), "f")


def norm_date(value) -> str:
    if value is None:
        return ""
    if hasattr(value, "strftime"):
        try:
            return value.strftime("%Y-%m-%d")
        except Exception:
            return ""
    try:
        if isinstance(value, float) and value != value:
            return ""
    except Exception:
        return ""
    text = str(value).strip()
    if text.lower() in {"", "nat", "none", "nan", "NaT"}:
        return ""
    if "T" in text:
        text = text.split("T", 1)[0]
    if " " in text:
        text = text.split(" ", 1)[0]
    text = text.replace("/", "-")
    if len(text) >= 10 and text[4] == "-" and text[7] == "-":
        return text[:10]
    return ""


def as_paused(value) -> bool:
    if value is None or value == "":
        return False
    if isinstance(value, str):
        return value.strip().lower() in {"1", "true", "yes"}
    try:
        if isinstance(value, float) and value != value:
            return False
    except Exception:
        return False
    return float(value) != 0.0


def as_float(value):
    if value is None or value == "":
        return None
    try:
        if isinstance(value, float) and value != value:
            return None
    except Exception:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def as_volume(value):
    number = as_float(value)
    if number is None:
        return None
    return int(number)


def classify_security_name(name: str | None) -> str | None:
    if name is None:
        return None
    head = str(name).strip().replace("\uff0a", "*").replace(" ", "")
    if not head:
        return None
    if "退市" in head or (head.endswith("退") and not head.startswith("*ST") and not head.startswith("ST")):
        return "退市整理"
    if head.startswith("*ST") or "*ST" in head[:4]:
        return "*ST"
    if head.startswith("ST"):
        return "ST"
    return None


def _interval_covers(item: dict, code: str, date_s: str) -> bool:
    if str(item.get("code") or "") != code:
        return False
    if not str(item.get("name") or "").strip():
        return False
    start = norm_date(item.get("start"))
    if not start or date_s < start:
        return False
    end = item.get("end")
    if end not in (None, ""):
        end_s = norm_date(end)
        if end_s and date_s > end_s:
            return False
    return True


def name_on_date(intervals: list[dict], code: str, date_s: str) -> str | None:
    best_start = None
    best_name = None
    for item in intervals:
        if not _interval_covers(item, code, date_s):
            pass
        else:
            start = norm_date(item.get("start"))
            if best_start is None or start >= best_start:
                best_start = start
                best_name = str(item.get("name")).strip()
    return best_name


def new_status_probe() -> dict:
    """结果槽全部留空。只有鉴权后的真实调用才能填。"""
    return {
        "is_st_called": False,
        "is_st_error": None,
        "is_st_frame_shape": None,
        "is_st_columns": None,
        "is_st_cells": None,
        "name_source": None,
        "name_errors": [],
        "name_columns": None,
        "observed_multiple_categories_under_is_st_true": None,
        "is_st_true_flags": None,
        "static_name_stamp_used": False,
        "ex_rights_ref_checked": None,
        "empty_codes": [],
        "query_count": None,
    }


def board_st_day_pct(code: str, date_s: str, st_flag: str) -> tuple[str, Decimal]:
    """board_st_day_effective。越窗、300/301/688、退市整理都直接 ABORT。"""
    if code.startswith("300") or code.startswith("301") or code.startswith("688"):
        abort(f"300/301/688 code={code} date={date_s}")
    if not date_s:
        abort("empty date")
    if date_s < PERM_START or date_s > PERM_END:
        abort(f"outside permission window {PERM_WINDOW_LABEL} date={date_s}")
    if date_s < START or date_s > END:
        abort(f"outside sample window {START}..{END} date={date_s}")
    if st_flag == "退市整理":
        abort(f"退市整理 code={code} date={date_s} 不按普通ST的5%或10%计算")
    if st_flag in {"ST", "*ST"}:
        pct = PCT_PRE if date_s < CUTOVER else PCT_POST
        return "main", pct
    if st_flag == "否":
        return "main", PCT_MAIN
    abort(f"unknown st_flag={st_flag} code={code} date={date_s}")
    raise AssertionError("unreachable")


def row_violation(code: str, date_s: str, st_flag: str) -> str | None:
    if code.startswith("300") or code.startswith("301") or code.startswith("688"):
        return f"300/301/688 code={code} date={date_s or 'empty'}"
    if code not in CODES:
        return f"code not in locked list code={code}"
    if not date_s:
        return "empty date"
    if date_s < PERM_START or date_s > PERM_END:
        return f"outside permission window {PERM_WINDOW_LABEL} date={date_s}"
    if date_s < START or date_s > END:
        return f"outside sample window {START}..{END} date={date_s}"
    if st_flag == "退市整理":
        return f"退市整理 code={code} date={date_s} excluded_from_5pct_10pct"
    if st_flag not in {"ST", "*ST"}:
        return f"st_flag not ST/*ST code={code} date={date_s} flag={st_flag}"
    return None


def name_change_conflicts(rows: list[dict]) -> list[str]:
    """000793 在 2026-07-31 由 *ST 改为 ST。两边都出现时不准打同一个静态标记。"""
    hit = [row for row in rows if str(row.get("code")) == NAME_CHANGE_CODE]
    before = [row for row in hit if str(row.get("date")) < NAME_CHANGE_DATE]
    after = [row for row in hit if str(row.get("date")) >= NAME_CHANGE_DATE]
    found = []
    if any(row.get("st_flag") != "*ST" for row in before):
        found.append("000793 date<2026-07-31 st_flag is not *ST")
    if any(row.get("st_flag") != "ST" for row in after):
        found.append("000793 date>=2026-07-31 st_flag is not ST")
    if before and after and len({row.get("st_flag") for row in hit}) < 2:
        found.append("000793 static st_flag across 2026-07-31")
    return found


def _price_problem(raw: dict) -> str | None:
    pre = as_float(raw.get("pre_close"))
    if pre is None or pre <= 0:
        return f"invalid pre_close code={raw.get('code')} date={norm_date(raw.get('date'))}"
    for key in ("open", "high", "low", "close"):
        if as_float(raw.get(key)) is None:
            return f"invalid {key} code={raw.get('code')} date={norm_date(raw.get('date'))}"
    if as_volume(raw.get("volume")) is None:
        return f"invalid volume code={raw.get('code')} date={norm_date(raw.get('date'))}"
    return None


def enrich_rows(raw_rows: list[dict]) -> list[dict]:
    """富化。任一越窗/错板/退市整理/状态不清，整批 ABORT，不返回删掉坏行后的表。"""
    violations: list[str] = []
    pending: list[tuple[dict, str, str, str]] = []
    for raw in raw_rows:
        code = str(raw.get("code") or "")
        date_s = norm_date(raw.get("date"))
        st_flag = str(raw.get("st_flag") or "")
        reason = row_violation(code, date_s, st_flag)
        price_reason = _price_problem(raw)
        if reason:
            violations.append(reason)
        elif price_reason:
            violations.append(price_reason)
        else:
            pending.append((raw, code, date_s, st_flag))
    conflicts = name_change_conflicts(
        [
            {"code": code, "date": date_s, "st_flag": st_flag}
            for _raw, code, date_s, st_flag in pending
        ]
    )
    violations.extend(conflicts)
    if violations:
        abort(" | ".join(violations))

    rows: list[dict] = []
    for raw, code, date_s, st_flag in pending:
        board, pct = board_st_day_pct(code, date_s, st_flag)
        pre = float(as_float(raw.get("pre_close")))
        open_ = float(as_float(raw.get("open")))
        high = float(as_float(raw.get("high")))
        low = float(as_float(raw.get("low")))
        close = float(as_float(raw.get("close")))
        volume = int(as_volume(raw.get("volume")))
        paused = as_paused(raw.get("paused"))
        limit_up, limit_down = limit_prices(pre, float(pct))
        one_up = (open_ == high == low == close == limit_up) and volume > 0
        one_down = (open_ == high == low == close == limit_down) and volume > 0
        rows.append(
            {
                "date": date_s,
                "code": code,
                "symbol": code,
                "board": board,
                "st": st_flag in {"ST", "*ST"},
                "st_flag": st_flag,
                "name": str(raw.get("name") or ""),
                "is_st": raw.get("is_st"),
                "limit_pct": float(pct),
                "pre_close": pre,
                "open": open_,
                "high": high,
                "low": low,
                "close": close,
                "volume": volume,
                "money": float(as_float(raw.get("money")) or 0.0),
                "paused": paused,
                "limit_up": limit_up,
                "limit_down": limit_down,
                "is_one_word_up": bool(one_up),
                "is_one_word_down": bool(one_down),
                "is_limit_up_close": abs(close - limit_up) < 1e-9,
                "is_limit_down_close": abs(close - limit_down) < 1e-9,
                "is_suspended": bool(paused) or volume <= 0,
            }
        )
    return rows


def _pick_col(df, options: tuple[str, ...]):
    lookup = {str(column).lower(): column for column in df.columns}
    for name in options:
        if name in lookup:
            return lookup[name]
    return None


def _text_cell(value) -> str:
    if value is None:
        return ""
    if isinstance(value, float):
        try:
            if value != value:
                return ""
        except Exception:
            return ""
    text = str(value).strip()
    if text.lower() in {"", "nat", "none", "nan", "<na>"}:
        return ""
    return text


def _prev_day(date_s: str) -> str:
    day = datetime.strptime(date_s, "%Y-%m-%d")
    return (day - timedelta(days=1)).strftime("%Y-%m-%d")


def _rows_from_name_records(df, code_col, name_col, start_col, org_col) -> dict[str, list[dict]]:
    pending: dict[str, list[dict]] = {}
    for rec in df.to_dict(orient="records"):
        start = norm_date(rec.get(start_col))
        name = _text_cell(rec.get(name_col))
        code = _text_cell(rec.get(code_col))
        if not code or not name or not start:
            pass
        else:
            org_name = _text_cell(rec.get(org_col)) if org_col else ""
            pending.setdefault(code, []).append(
                {"name": name, "start": start, "org_name": org_name}
            )
    return pending


def _intervals_without_end_column(pending: dict[str, list[dict]]) -> list[dict]:
    """无 end_date 列时，new_name 覆盖 [start_date, 下一行 start_date)。

    org_name 只补该代码最早一行 start_date 之前。它不是 start_date 当日及以后的简称。
    最后一行没有下一行，向后敞开；缺 org_name 的前缀保持未覆盖，不整段盖同一个简称。
    """
    intervals = []
    for code, rows in pending.items():
        rows.sort(key=lambda item: item["start"])
        earliest = rows[0]
        org_name = earliest.get("org_name") or ""
        if org_name:
            intervals.append(
                {
                    "code": code,
                    "name": org_name,
                    "start": "0001-01-01",
                    "end": _prev_day(earliest["start"]),
                }
            )
        for index, row in enumerate(rows):
            nxt = rows[index + 1]["start"] if index + 1 < len(rows) else ""
            end = _prev_day(nxt) if nxt else None
            if end is None or end >= row["start"]:
                intervals.append(
                    {
                        "code": code,
                        "name": row["name"],
                        "start": row["start"],
                        "end": end,
                    }
                )
    return intervals


def intervals_from_name_frame(df) -> list[dict]:
    code_col = _pick_col(df, ("code", "sec_code", "security"))
    # new_name 是聚宽变更后简称。org_name 不在候选里，避免被当成 start_date 起的当前简称。
    name_col = _pick_col(df, ("name", "short_name", "display_name", "abbr", "new_name"))
    start_col = _pick_col(df, ("start_date", "begin_date", "change_date"))
    end_col = _pick_col(df, ("end_date", "stop_date"))
    if code_col is None or name_col is None or start_col is None or str(name_col).lower() == "org_name":
        seen = [str(column) for column in getattr(df, "columns", [])]
        abort(f"name history columns not recognized: {seen}")
    if end_col:
        intervals = []
        for rec in df.to_dict(orient="records"):
            start = norm_date(rec.get(start_col))
            name = _text_cell(rec.get(name_col))
            code = _text_cell(rec.get(code_col))
            if not code or not name or not start:
                pass
            else:
                end_raw = rec.get(end_col)
                end = norm_date(end_raw) if end_raw not in (None, "") else ""
                intervals.append(
                    {
                        "code": code,
                        "name": name,
                        "start": start,
                        "end": end or None,
                    }
                )
        return intervals
    org_col = _pick_col(df, ("org_name",))
    pending = _rows_from_name_records(df, code_col, name_col, start_col, org_col)
    return _intervals_without_end_column(pending)


def join_price_and_status(price_rows: list[dict], intervals: list[dict], is_st_map: dict, probe: dict) -> list[dict]:
    joined = []
    true_flags: set[str] = set()
    saw_true = False
    for row in price_rows:
        date_s = norm_date(row.get("date"))
        code = str(row.get("code") or "")
        if (date_s, code) not in is_st_map:
            is_st_val = None
        else:
            is_st_val = is_st_map[(date_s, code)]
        name = name_on_date(intervals, code, date_s) if date_s else None
        klass = classify_security_name(name) if name else None
        if klass in {"*ST", "ST", "退市整理"}:
            flag = klass
        elif name and is_st_val is False and klass is None:
            # 简称已经覆盖、且对不上 ST/*ST/退市时，is_st=False 才是普通股。
            # 没有覆盖的日期走 MISSING，不能因为 is_st=False 默当成普通股。
            flag = "否"
        elif is_st_val is True and klass is None:
            flag = "UNSPLIT"
        else:
            flag = "MISSING"
        if is_st_val is True:
            saw_true = True
            true_flags.add(flag)
        merged = dict(row)
        merged["date"] = date_s
        merged["st_flag"] = flag
        merged["name"] = name or ""
        merged["is_st"] = is_st_val
        joined.append(merged)
    if saw_true:
        categories = {flag for flag in true_flags if flag in {"ST", "*ST", "退市整理"}}
        probe["observed_multiple_categories_under_is_st_true"] = len(categories) > 1
        probe["is_st_true_flags"] = sorted(true_flags)
    else:
        probe["observed_multiple_categories_under_is_st_true"] = None
        probe["is_st_true_flags"] = []
    probe["static_name_stamp_used"] = False
    return joined


def _as_bool_or_none(value):
    if value is None:
        return None
    try:
        if isinstance(value, float) and value != value:
            return None
    except Exception:
        return None
    if isinstance(value, str):
        low = value.strip().lower()
        if low in {"true", "1"}:
            return True
        if low in {"false", "0"}:
            return False
        return None
    return bool(value)


def normalize_is_st_frame(df, codes: tuple[str, ...], probe: dict) -> dict:
    probe["is_st_frame_shape"] = type(df).__name__
    if df is None:
        abort("get_extras('is_st') returned None")
    columns = [str(column) for column in df.columns]
    probe["is_st_columns"] = columns
    out = {}
    frame = df
    date_col = _pick_col(df, ("date", "day", "time"))
    if date_col is not None:
        records = frame.to_dict(orient="records")
        for rec in records:
            date_s = norm_date(rec.get(date_col))
            for code in codes:
                if code not in frame.columns:
                    abort(f"get_extras('is_st') missing column {code}; columns={columns}")
                out[(date_s, code)] = _as_bool_or_none(rec.get(code))
    else:
        for idx, row in frame.iterrows():
            date_s = norm_date(idx)
            for code in codes:
                if code not in frame.columns:
                    abort(f"get_extras('is_st') missing column {code}; columns={columns}")
                out[(date_s, code)] = _as_bool_or_none(row[code])
    probe["is_st_cells"] = len(out)
    if not out:
        abort("get_extras('is_st') returned no cells")
    return out


def _finance_module(jq):
    finance = getattr(jq, "finance", None)
    if finance is not None:
        return finance
    import importlib

    return importlib.import_module("jqdatasdk.finance")


def fetch_name_intervals(jq, codes: tuple[str, ...], probe: dict) -> list[dict]:
    """只探测简称历史。探测失败就留错误，不准用当前简称铺满整段窗。"""
    errors = []
    try:
        finance = _finance_module(jq)
        table = getattr(finance, "STK_NAME_HISTORY", None)
        if table is None:
            raise AttributeError("STK_NAME_HISTORY missing")
        query = jq.query(table).filter(table.code.in_(list(codes)))
        df = finance.run_query(query)
        probe["name_columns"] = [str(column) for column in getattr(df, "columns", [])]
        intervals = intervals_from_name_frame(df)
        if not intervals:
            raise RuntimeError("STK_NAME_HISTORY returned no usable rows")
        probe["name_source"] = "finance.STK_NAME_HISTORY"
        probe["name_errors"] = errors
        return intervals
    except Exception as exc:
        errors.append(f"finance.STK_NAME_HISTORY: {type(exc).__name__}: {exc}")
    probe["name_source"] = None
    probe["name_errors"] = errors
    probe["static_name_stamp_used"] = False
    return []


def fetch_is_st_map(jq, codes: tuple[str, ...], probe: dict) -> dict:
    probe["is_st_called"] = True
    try:
        df = jq.get_extras("is_st", list(codes), start_date=START, end_date=END, df=True)
    except TypeError:
        try:
            df = jq.get_extras("is_st", list(codes), start_date=START, end_date=END)
        except Exception as exc:
            probe["is_st_error"] = f"{type(exc).__name__}: {exc}"
            abort(f"get_extras('is_st') failed: {probe['is_st_error']}")
    except Exception as exc:
        probe["is_st_error"] = f"{type(exc).__name__}: {exc}"
        abort(f"get_extras('is_st') failed: {probe['is_st_error']}")
    return normalize_is_st_frame(df, codes, probe)


def frame_to_price_rows(df, code: str) -> list[dict]:
    frame = df.reset_index()
    if "date" not in frame.columns:
        frame = frame.rename(columns={frame.columns[0]: "date"})
    rows = []
    for rec in frame.to_dict(orient="records"):
        rows.append(
            {
                "date": rec.get("date"),
                "code": code,
                "open": rec.get("open"),
                "high": rec.get("high"),
                "low": rec.get("low"),
                "close": rec.get("close"),
                "volume": rec.get("volume"),
                "money": rec.get("money", 0),
                "pre_close": rec.get("pre_close"),
                "paused": rec.get("paused", 0),
            }
        )
    return rows


def write_bundle(rows: list[dict], probe: dict, directory: Path, *, synthetic: bool) -> dict:
    if synthetic and directory.resolve() == DATA.resolve():
        abort("refuse synthetic rows under data/")
    for path in (OUT_PQ, OUT_META, OUT_EV):
        if path.name not in {
            "daily_st_cutover_window.parquet",
            "daily_st_cutover_window_meta.json",
            "st_cutover_evidence.txt",
        }:
            abort(f"refusing output name {path.name}")
    if not rows:
        abort("NO_DATA")
    import pandas as pd

    directory.mkdir(parents=True, exist_ok=True)
    frame = pd.DataFrame(rows)
    for column in COLUMNS:
        if column not in frame.columns:
            abort(f"missing column {column}")
    frame = frame.loc[:, list(COLUMNS)]
    pq_path = directory / OUT_PQ.name
    meta_path = directory / OUT_META.name
    ev_path = directory / OUT_EV.name
    frame.to_parquet(pq_path, index=False)
    dates = [str(item) for item in frame["date"].tolist()]
    flag_counts: dict[str, int] = {}
    for flag in frame["st_flag"].tolist():
        key = str(flag)
        flag_counts[key] = flag_counts.get(key, 0) + 1
    meta = {
        "as_of": datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds"),
        "vendor": "synthetic" if synthetic else "joinquant/jqdatasdk",
        "sample_id": "st_cutover",
        "synthetic": bool(synthetic),
        "jqdatasdk_version": probe.get("jqdatasdk_version"),
        "codes": list(CODES),
        "n_codes": len(CODES),
        "start": START,
        "end": END,
        "permission_window": PERM_WINDOW_LABEL,
        "fq": None,
        "price_rule": "board_st_day_effective",
        "price_basis": "unadjusted",
        "limit_round": "Decimal ROUND_HALF_UP 0.01",
        "rows": int(len(frame)),
        "date_min": min(dates) if dates else None,
        "date_max": max(dates) if dates else None,
        "st_flag_counts": flag_counts,
        "parquet": pq_path.name,
        "sha256": sha256_file(pq_path),
        "st_probe": probe,
        "query_count": probe.get("query_count"),
        "ex_rights_ref_checked": None,
        "static_name_stamp_used": False,
        "note": "st_cutover sample only; fq is null; ex-rights ref was not checked in this writer",
    }
    meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    lines = [
        "AUTH_OK" if not synthetic else "SYNTHETIC_BUNDLE",
        f"sample_id=st_cutover",
        f"permission_window={PERM_WINDOW_LABEL}",
        f"start={START}",
        f"end={END}",
        "fq=None",
        "price_rule=board_st_day_effective",
        f"codes={','.join(CODES)}",
        f"rows={len(frame)}",
        f"date_min={meta['date_min']}",
        f"date_max={meta['date_max']}",
        f"st_flag_counts={json.dumps(flag_counts, ensure_ascii=False)}",
        f"name_source={probe.get('name_source')}",
        f"is_st_mix_observation={probe.get('observed_multiple_categories_under_is_st_true')}",
        "static_name_stamp_used=False",
        "ex_rights_ref_checked=null",
        f"parquet={pq_path.name}",
        "gate_decided_here=no",
        "",
    ]
    ev_path.write_text("\n".join(lines), encoding="utf-8")
    return meta


def _fetch_authed(jq) -> None:
    REJECT_LOG.clear()
    lock_constants()
    probe = new_status_probe()
    probe["jqdatasdk_version"] = getattr(jq, "__version__", "unknown")
    try:
        qc = jq.get_query_count()
        probe["query_count"] = qc if isinstance(qc, dict) else str(type(qc).__name__)
    except Exception as exc:
        probe["query_count"] = f"query_count_err={type(exc).__name__}: {exc}"

    STATUS["state"] = "fetching"
    price_rows: list[dict] = []
    empty_codes: list[str] = []
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
            empty_codes.append(code)
        else:
            price_rows.extend(frame_to_price_rows(df, code))
    probe["empty_codes"] = empty_codes
    if not price_rows:
        abort(f"NO_DATA empty_codes={empty_codes}")

    is_st_map = fetch_is_st_map(jq, CODES, probe)
    intervals = fetch_name_intervals(jq, CODES, probe)
    if not intervals:
        abort(
            "name history unavailable; refuse static ST stamp. "
            + json.dumps(probe, ensure_ascii=False, default=str)
        )
    joined = join_price_and_status(price_rows, intervals, is_st_map, probe)
    enriched = enrich_rows(joined)
    meta = write_bundle(enriched, probe, DATA, synthetic=False)
    STATUS["state"] = "done"
    STATUS["detail"] = (
        f"rows={meta['rows']} date={meta['date_min']}..{meta['date_max']} "
        f"flags={json.dumps(meta['st_flag_counts'], ensure_ascii=False)}"
    )


def do_fetch(password: str) -> None:
    global FETCH_CALLED
    FETCH_CALLED = True
    import jqdatasdk as jq

    jq.set_params(request_timeout=60, request_attempt_count=2, enable_auth_prompt=False)
    try:
        STATUS["state"] = "authing"
        jq.auth(USER, password)
        if not jq.is_auth():
            raise RuntimeError("is_auth=False")
        _fetch_authed(jq)
    finally:
        password = ""
        try:
            jq.logout()
        except Exception:
            pass


class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):
        sys.stderr.write("%s - %s\n" % (self.address_string(), fmt % args))

    def _send(self, status: int, body: bytes, content_type: str = "text/plain; charset=utf-8") -> None:
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path.startswith("/status"):
            body = json.dumps(STATUS, ensure_ascii=False).encode()
            self._send(200, body, "application/json")
            return
        self._send(200, HTML.encode(), "text/html; charset=utf-8")

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        raw = self.rfile.read(length).decode("utf-8", errors="replace")
        password = (parse_qs(raw).get("password") or [""])[0]
        raw = ""
        abort_exc = None
        if not password:
            self._send(400, "missing password".encode())
            return
        try:
            try:
                do_fetch(password)
                msg = (
                    f"<h1>{PAGE_TITLE}</h1>"
                    f"<p>AUTH_OK。样本已写入 data/{OUT_PQ.name}。</p>"
                    f"<pre>{STATUS.get('detail', '')}</pre>"
                    "<p>可关闭此页。本页只表示取数结束，不表示抽检过关。</p>"
                )
            except SystemExit as exc:
                abort_exc = exc
                STATUS["state"] = "error"
                STATUS["detail"] = str(exc)[:500]
                msg = f"<h1>{PAGE_TITLE}</h1><h2>ABORT</h2><pre>{exc}</pre>"
            except Exception as exc:
                STATUS["state"] = "error"
                STATUS["detail"] = type(exc).__name__
                msg = f"<h1>{PAGE_TITLE}</h1><h2>失败</h2><pre>{type(exc).__name__}: {exc}</pre>"
                traceback.print_exc()
        finally:
            password = ""
        body = (
            f"<!doctype html><meta charset=utf-8><title>{PAGE_TITLE}</title><body>{msg}</body>"
        ).encode()
        self._send(200, body, "text/html; charset=utf-8")
        if abort_exc is not None:
            raise abort_exc
        if STATUS.get("state") == "done":
            threading.Thread(target=self.server.shutdown, daemon=True).start()
        else:
            STATUS["state"] = "waiting"


def serve() -> None:
    global SERVE_CALLED
    SERVE_CALLED = True
    lock_constants()
    DATA.mkdir(parents=True, exist_ok=True)
    httpd = HTTPServer((HOST, PORT), Handler)
    print(f"OPEN http://{HOST}:{PORT}/  ({PAGE_TITLE})", flush=True)
    try:
        httpd.serve_forever()
    except SystemExit:
        raise
    print("SERVER_STOPPED state=", STATUS["state"], STATUS.get("detail"), flush=True)


def _expect_abort(fn, token: str) -> None:
    REJECT_LOG.clear()
    try:
        fn()
    except SystemExit as exc:
        text = str(exc)
        if "ABORT" not in text or token not in text:
            abort(f"self-check bad abort text token={token} text={text}")
        if not any(token in item for item in REJECT_LOG):
            abort(f"self-check abort left no record for {token}")
        return
    abort(f"self-check expected SystemExit containing {token}")


def _raw(code: str, date_s: str, st_flag: str, pre: str = "10", name: str = "") -> dict:
    price = float(Decimal(pre))
    return {
        "date": date_s,
        "code": code,
        "st_flag": st_flag,
        "name": name,
        "is_st": True,
        "pre_close": price,
        "open": price,
        "high": price,
        "low": price,
        "close": price,
        "volume": 1000,
        "money": 10000,
        "paused": False,
    }


def _independent_limits(pre: str, pct: str) -> tuple[str, str]:
    pre_d = Decimal(pre)
    pct_d = Decimal(pct)
    up = (pre_d * (Decimal("1") + pct_d)).quantize(TICK, rounding=ROUND_HALF_UP)
    down = (pre_d * (Decimal("1") - pct_d)).quantize(TICK, rounding=ROUND_HALF_UP)
    if abs(up - pre_d) < TICK:
        up = pre_d + TICK
    if abs(down - pre_d) < TICK:
        down = pre_d - TICK
    if down < TICK:
        down = TICK
    return format(up, "f"), format(down, "f")


def _data_names() -> set[str]:
    if not DATA.exists():
        return set()
    return {path.name for path in DATA.iterdir()}


def _jq_stk_name_history_columns() -> list[str]:
    return [
        "id",
        "code",
        "company_id",
        "new_name",
        "new_spelling",
        "org_name",
        "org_spelling",
        "start_date",
        "pub_date",
        "reason",
    ]


def _jq_name_frame(pd, rows: list[dict]):
    columns = _jq_stk_name_history_columns()
    frame = pd.DataFrame(rows, columns=columns)
    seen = [str(column) for column in frame.columns]
    if seen != columns:
        abort(f"jq name fixture columns drifted: {seen}")
    return frame


def _check_jq_stk_name_history(pd) -> None:
    """聚宽 finance.STK_NAME_HISTORY 今晚这组列。new_name 才是变更后简称。"""
    columns = _jq_stk_name_history_columns()
    two_rows = [
        {
            "id": 1,
            "code": "000793.XSHE",
            "company_id": 1,
            "new_name": "*ST华闻",
            "new_spelling": "sthw",
            "org_name": "华闻集团",
            "org_spelling": "hwjt",
            "start_date": "2026-03-02",
            "pub_date": "2026-07-20",
            "reason": "简称变更",
        },
        {
            "id": 2,
            "code": "000793.XSHE",
            "company_id": 1,
            "new_name": "ST华闻",
            "new_spelling": "sthw",
            "org_name": "*ST华闻",
            "org_spelling": "sthw",
            "start_date": "2026-07-31",
            "pub_date": "2026-07-01",
            "reason": "简称变更",
        },
    ]
    parsed = intervals_from_name_frame(_jq_name_frame(pd, two_rows))
    if name_on_date(parsed, "000793.XSHE", "2026-03-01") != "华闻集团":
        abort(f"jq org_name prefix {parsed}")
    if name_on_date(parsed, "000793.XSHE", "2026-03-02") != "*ST华闻":
        abort("jq new_name must start on start_date")
    if name_on_date(parsed, "000793.XSHE", "2026-07-30") != "*ST华闻":
        abort("jq two-row 2026-07-30")
    if classify_security_name(name_on_date(parsed, "000793.XSHE", "2026-07-30")) != "*ST":
        abort("jq two-row 2026-07-30 class")
    if name_on_date(parsed, "000793.XSHE", "2026-07-31") != "ST华闻":
        abort("jq two-row 2026-07-31")
    if classify_security_name(name_on_date(parsed, "000793.XSHE", "2026-07-31")) != "ST":
        abort("jq two-row 2026-07-31 class")
    star = [item for item in parsed if item["code"] == "000793.XSHE" and item["start"] == "2026-03-02"]
    plain = [item for item in parsed if item["code"] == "000793.XSHE" and item["start"] == "2026-07-31"]
    if len(star) != 1 or star[0]["name"] != "*ST华闻" or star[0]["end"] != "2026-07-30":
        abort(f"jq two-row half-open {parsed}")
    if len(plain) != 1 or plain[0]["name"] != "ST华闻" or plain[0]["end"] is not None:
        abort(f"jq two-row open tail {parsed}")

    one_row = {
        "id": 3,
        "code": "000793.XSHE",
        "company_id": 1,
        "new_name": "ST华闻",
        "new_spelling": "sthw",
        "org_name": "*ST华闻",
        "org_spelling": "sthw",
        "start_date": "2026-07-31",
        "pub_date": "2026-07-01",
        "reason": "简称变更",
    }
    parsed_one = intervals_from_name_frame(_jq_name_frame(pd, [one_row]))
    if name_on_date(parsed_one, "000793.XSHE", "2026-06-01") != "*ST华闻":
        abort("jq org_name prefix inside window")
    if name_on_date(parsed_one, "000793.XSHE", "2026-07-30") != "*ST华闻":
        abort("jq one-row 2026-07-30")
    if classify_security_name(name_on_date(parsed_one, "000793.XSHE", "2026-07-30")) != "*ST":
        abort("jq one-row 2026-07-30 class")
    if name_on_date(parsed_one, "000793.XSHE", "2026-07-31") != "ST华闻":
        abort("jq one-row used org_name on start_date")
    if classify_security_name(name_on_date(parsed_one, "000793.XSHE", "2026-07-31")) != "ST":
        abort("jq one-row 2026-07-31 class")
    prior = [item for item in parsed_one if item["name"] == "*ST华闻"]
    current = [item for item in parsed_one if item["name"] == "ST华闻"]
    if len(prior) != 1 or prior[0]["end"] != "2026-07-30" or not prior[0]["start"] < "2026-07-31":
        abort(f"jq org prefix interval {parsed_one}")
    if len(current) != 1 or current[0]["start"] != "2026-07-31" or current[0]["end"] is not None:
        abort(f"jq new_name interval {parsed_one}")

    mixed_rows = list(two_rows)
    mixed_rows.append(
        {
            "id": 4,
            "code": "000911.XSHE",
            "company_id": 2,
            "new_name": "*ST广糖",
            "new_spelling": "stgt",
            "org_name": "广农糖业",
            "org_spelling": "gnty",
            "start_date": "2026-07-06",
            "pub_date": "2026-06-15",
            "reason": "简称变更",
        }
    )
    parsed_mixed = intervals_from_name_frame(_jq_name_frame(pd, mixed_rows))
    if name_on_date(parsed_mixed, "000793.XSHE", "2026-07-30") != "*ST华闻":
        abort("jq other code cut 000793")
    if name_on_date(parsed_mixed, "000793.XSHE", "2026-07-31") != "ST华闻":
        abort("jq other code rewrote 000793")
    if name_on_date(parsed_mixed, "000911.XSHE", "2026-07-05") != "广农糖业":
        abort("jq per-code org prefix")
    if name_on_date(parsed_mixed, "000911.XSHE", "2026-07-06") != "*ST广糖":
        abort("jq per-code new_name")
    closed = [
        item for item in parsed_mixed if item["code"] == "000793.XSHE" and item["start"] == "2026-03-02"
    ]
    if len(closed) != 1 or closed[0]["end"] != "2026-07-30":
        abort(f"jq cross-code end {parsed_mixed}")

    gap_row = {
        "id": 5,
        "code": "000793.XSHE",
        "company_id": 1,
        "new_name": "ST华闻",
        "new_spelling": "sthw",
        "org_name": None,
        "org_spelling": None,
        "start_date": "2026-07-31",
        "pub_date": "2026-07-31",
        "reason": "简称变更",
    }
    parsed_gap = intervals_from_name_frame(_jq_name_frame(pd, [gap_row]))
    if name_on_date(parsed_gap, "000793.XSHE", "2026-07-30") is not None:
        abort("missing org_name stamped backward")
    if name_on_date(parsed_gap, "000793.XSHE", "2026-07-31") != "ST华闻":
        abort("gap row lost new_name")
    probe = new_status_probe()
    joined_gap = join_price_and_status(
        [_raw("000793.XSHE", "2026-07-30", "", name="")],
        parsed_gap,
        {("2026-07-30", "000793.XSHE"): False},
        probe,
    )
    if joined_gap[0]["st_flag"] == "否":
        abort("uncovered name treated as ordinary")
    if joined_gap[0]["st_flag"] != "MISSING":
        abort(f"uncovered name flag {joined_gap[0]['st_flag']}")
    if probe.get("static_name_stamp_used") is not False:
        abort("static name stamp flag")
    _expect_abort(lambda: enrich_rows(joined_gap), "flag=MISSING")

    bare_columns = [column for column in columns if column != "new_name"]
    bare = pd.DataFrame([{key: gap_row[key] for key in bare_columns}], columns=bare_columns)
    _expect_abort(lambda: intervals_from_name_frame(bare), "columns not recognized")
    print("SELF_CHECK jq_name_columns=" + ",".join(columns))
    print("SELF_CHECK jq_new_name_two_rows=ok jq_new_name_org_prefix=ok")
    print("SELF_CHECK jq_org_name_not_current=ok jq_uncovered_not_ordinary=ok")
    print("SELF_CHECK jq_unknown_columns_abort=ok")


def run_self_check() -> int:
    if SERVE_CALLED or FETCH_CALLED:
        abort("self-check must run before serve or fetch")
    lock_constants()
    source = Path(__file__).read_text(encoding="utf-8")
    silent_drop = "cont" + "inue"
    expand_tag = "LIVE_" + "EXPAND"
    expand_file = "daily_" + "expand_window"
    if silent_drop in source:
        abort("self-check found a silent-drop keyword")
    if expand_tag in source or expand_file in source:
        abort("self-check found an expand deliverable token")
    print("TITLE_CODEPOINTS", " ".join(f"U+{ord(ch):04X}" for ch in PAGE_TITLE))
    print("PERM_LABEL_CODEPOINTS", " ".join(f"U+{ord(ch):04X}" for ch in PERM_WINDOW_LABEL))
    print("SELF_CHECK network=no serve=no")

    board, pct = board_st_day_pct("000911.XSHE", "2026-07-05", "*ST")
    if board != "main" or pct != PCT_PRE:
        abort(f"pre-cut pct {pct}")
    _board, pct = board_st_day_pct("000911.XSHE", "2026-07-06", "ST")
    if pct != PCT_POST:
        abort(f"cut-day pct {pct}")
    _board, pct = board_st_day_pct("000911.XSHE", "2026-06-01", "*ST")
    if pct != PCT_PRE:
        abort("sample start pct")
    _board, pct = board_st_day_pct("603378.XSHG", "2026-08-12", "*ST")
    if pct != PCT_POST:
        abort("sample end pct")
    _board, pct = board_st_day_pct("000911.XSHE", "2026-07-06", "否")
    if pct != PCT_MAIN:
        abort("main non-st pct")
    print("SELF_CHECK pre_cut=0.05 post_cut=0.10 main_non_st=0.10")

    up, down = limit_prices(10.0, 0.05)
    exp_up, exp_down = _independent_limits("10.00", "0.05")
    if Decimal(str(up)) != Decimal(exp_up) or Decimal(str(down)) != Decimal(exp_down):
        abort(f"half-up mismatch 0.05 {up},{down} vs {exp_up},{exp_down}")
    up, down = limit_prices(10.0, 0.10)
    exp_up, exp_down = _independent_limits("10.00", "0.10")
    if Decimal(str(up)) != Decimal(exp_up) or Decimal(str(down)) != Decimal(exp_down):
        abort(f"half-up mismatch 0.10 {up},{down} vs {exp_up},{exp_down}")
    if Decimal("1.005").quantize(TICK, rounding=ROUND_HALF_UP) != Decimal("1.01"):
        abort("ROUND_HALF_UP tick check failed")
    print(f"SELF_CHECK half_up_10_at_0.05={limit_prices(10.0, 0.05)} half_up_10_at_0.10={limit_prices(10.0, 0.10)}")

    _expect_abort(lambda: board_st_day_pct("000911.XSHE", "2025-08-04", "*ST"), "2025-08-04")
    _expect_abort(lambda: board_st_day_pct("000911.XSHE", "2026-08-13", "*ST"), "2026-08-13")
    _expect_abort(lambda: board_st_day_pct("000911.XSHE", "2026-05-31", "*ST"), "2026-05-31")
    _expect_abort(lambda: board_st_day_pct("000911.XSHE", "2025-08-05", "*ST"), "outside sample window")
    _expect_abort(lambda: board_st_day_pct("300750.XSHE", "2026-07-06", "*ST"), "300/301/688")
    _expect_abort(lambda: board_st_day_pct("301236.XSHE", "2026-07-06", "*ST"), "300/301/688")
    _expect_abort(lambda: board_st_day_pct("688981.XSHG", "2026-07-06", "*ST"), "300/301/688")
    _expect_abort(
        lambda: enrich_rows([_raw("000911.XSHE", "2026-07-03", "退市整理", name="广糖退")]),
        "退市整理",
    )
    print("SELF_CHECK abort_perm_early=ok abort_perm_late=ok abort_outside_sample=ok")
    print("SELF_CHECK abort_300=ok abort_301=ok abort_688=ok abort_delist_recorded=ok")

    good = _raw("000911.XSHE", "2026-07-03", "*ST", name="*ST广糖")
    bad = _raw("000911.XSHE", "2026-08-13", "*ST", name="*ST广糖")
    returned = True
    try:
        enrich_rows([good, bad])
    except SystemExit as exc:
        returned = False
        if "ABORT" not in str(exc) or "2026-08-13" not in str(exc):
            abort(f"mixed window abort text {exc}")
    if returned:
        abort("mixed window returned rows instead of ABORT")
    print("SELF_CHECK mixed_window_no_return=ok")

    _expect_abort(lambda: enrich_rows([_raw("000911.XSHE", "2026-07-06", "否")]), "st_flag not ST/*ST")
    rows = enrich_rows(
        [
            _raw("000911.XSHE", "2026-07-03", "*ST", name="*ST广糖"),
            _raw("000911.XSHE", "2026-07-06", "*ST", name="*ST广糖"),
        ]
    )
    if len(rows) != 2 or not pct_equals(rows[0]["limit_pct"], "0.05") or not pct_equals(rows[1]["limit_pct"], "0.10"):
        abort(f"enrich pct rows={rows}")
    if rows[0]["limit_up"] != limit_prices(10.0, 0.05)[0] or rows[1]["limit_up"] != limit_prices(10.0, 0.10)[0]:
        abort("enrich limit_up drift")
    if rows[0]["st"] is not True or rows[0]["board"] != "main":
        abort("enrich st/board")
    print("SELF_CHECK enrich_cutover_pair=ok")

    _expect_abort(
        lambda: enrich_rows(
            [
                _raw("000793.XSHE", "2026-07-03", "*ST", name="*ST华闻"),
                _raw("000793.XSHE", "2026-07-31", "*ST", name="*ST华闻"),
            ]
        ),
        "000793 static st_flag",
    )
    split_rows = enrich_rows(
        [
            _raw("000793.XSHE", "2026-07-03", "*ST", name="*ST华闻"),
            _raw("000793.XSHE", "2026-07-31", "ST", name="ST华闻"),
        ]
    )
    if [row["st_flag"] for row in split_rows] != ["*ST", "ST"]:
        abort("000793 split flags")
    if not pct_equals(split_rows[0]["limit_pct"], "0.05") or not pct_equals(split_rows[1]["limit_pct"], "0.10"):
        abort("000793 split pct")
    print("SELF_CHECK 000793_split=ok 000793_static_abort=ok")

    if classify_security_name("\uff0aST华闻") != "*ST":
        abort("fullwidth star name")
    if classify_security_name("退市华闻") != "退市整理" or classify_security_name("华闻退") != "退市整理":
        abort("delist name")
    if classify_security_name("ST华闻") != "ST" or classify_security_name("*ST广糖") != "*ST":
        abort("st name")
    intervals = [
        {"code": "000793.XSHE", "name": "*ST华闻", "start": "2026-03-02", "end": "2026-07-30"},
        {"code": "000793.XSHE", "name": "ST华闻", "start": "2026-07-31", "end": None},
    ]
    if classify_security_name(name_on_date(intervals, "000793.XSHE", "2026-07-30")) != "*ST":
        abort("name on 2026-07-30")
    if classify_security_name(name_on_date(intervals, "000793.XSHE", "2026-07-31")) != "ST":
        abort("name on 2026-07-31")
    probe = new_status_probe()
    if probe["observed_multiple_categories_under_is_st_true"] is not None:
        abort("probe template was prefilled")
    joined = join_price_and_status(
        [
            _raw("000793.XSHE", "2026-07-03", "", name=""),
            _raw("000793.XSHE", "2026-07-31", "", name=""),
        ],
        intervals,
        {
            ("2026-07-03", "000793.XSHE"): True,
            ("2026-07-31", "000793.XSHE"): True,
        },
        probe,
    )
    if [row["st_flag"] for row in joined] != ["*ST", "ST"]:
        abort(f"join flags {joined}")
    if probe["observed_multiple_categories_under_is_st_true"] is not True:
        abort("mix observation was not computed from the fixture")
    if new_status_probe()["observed_multiple_categories_under_is_st_true"] is not None:
        abort("fixture observation leaked into the blank probe")
    print("SELF_CHECK name_split=ok probe_template_unrun=ok mix_observed_from_fixture=ok")

    try:
        import pandas as pd
    except ImportError:
        print("SELF_CHECK name_frame=skip_no_pandas")
    else:
        frame = pd.DataFrame(
            [
                {
                    "code": "000793.XSHE",
                    "name": "*ST华闻",
                    "start_date": "2026-03-02",
                    "end_date": "2026-07-30",
                },
                {
                    "code": "000793.XSHE",
                    "name": "ST华闻",
                    "start_date": "2026-07-31",
                    "end_date": None,
                },
            ]
        )
        parsed = intervals_from_name_frame(frame)
        if classify_security_name(name_on_date(parsed, "000793.XSHE", "2026-07-30")) != "*ST":
            abort("name frame end_date")
        if classify_security_name(name_on_date(parsed, "000793.XSHE", "2026-07-31")) != "ST":
            abort("name frame parse")
        print("SELF_CHECK name_frame=ok")
        _check_jq_stk_name_history(pd)

    before = _data_names()
    sample_rows = enrich_rows([_raw("000911.XSHE", "2026-07-03", "*ST", name="*ST广糖")])
    _expect_abort(lambda: write_bundle(sample_rows, new_status_probe(), DATA, synthetic=True), "synthetic")
    if _data_names() != before:
        abort(f"synthetic write touched data/: {_data_names() - before}")
    print("SELF_CHECK synthetic_not_written_to_data=ok")

    import tempfile

    tmp = Path(tempfile.mkdtemp(prefix="st_cutover_selfcheck_"))
    try:
        meta = write_bundle(rows, new_status_probe(), tmp, synthetic=True)
        if meta["fq"] is not None or meta["synthetic"] is not True:
            abort("tmp meta lost fq/synthetic")
        if meta["permission_window"] != PERM_WINDOW_LABEL:
            abort("tmp meta permission label")
        read_back = __import__("pandas").read_parquet(tmp / OUT_PQ.name)
        got = read_back["limit_pct"].tolist()
        if not pct_equals(got[0], "0.05") or not pct_equals(got[1], "0.10"):
            abort(f"parquet roundtrip pct {got}")
        evidence = (tmp / OUT_EV.name).read_text(encoding="utf-8")
        if PERM_WINDOW_LABEL not in evidence or "fq=None" not in evidence:
            abort("evidence missing window or fq")
        if "password" in evidence.lower():
            abort("evidence contains password")
        print("SELF_CHECK tmp_parquet_roundtrip=ok")
    finally:
        for path in tmp.iterdir():
            path.unlink()
        tmp.rmdir()

    if SERVE_CALLED or FETCH_CALLED:
        abort("self-check invoked serve or fetch")
    if _data_names() != before:
        abort("data dir changed during self-check")
    print("SELF_CHECK pass")
    return 0


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if "--self-check" in args:
        return run_self_check()
    if args:
        abort("unknown args; use --self-check, or no args to serve")
    serve()
    return 0 if STATUS.get("state") == "done" else 1


lock_constants()


if __name__ == "__main__":
    raise SystemExit(main())
