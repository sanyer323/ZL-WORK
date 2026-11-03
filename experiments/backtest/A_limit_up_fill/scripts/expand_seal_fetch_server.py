#!/usr/bin/env python3
"""Local-only expand-window fetch for seal events; never log secrets."""
from __future__ import annotations

import hashlib
import json
import sys
import threading
import traceback
from datetime import datetime, timezone
from decimal import Decimal, ROUND_HALF_UP
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import parse_qs

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT_PQ = DATA / "daily_expand_window.parquet"
OUT_META = DATA / "daily_expand_window_meta.json"
OUT_SEAL = DATA / "seal_event_subset.parquet"
OUT_EV = DATA / "expand_seal_evidence.txt"
STATUS = {"state": "waiting", "detail": ""}

# Fixed reproducible list ~25 names: main board + ChiNext mix. NO full-market pull.
CODES = [
    "000001.XSHE",  # 平安银行
    "000002.XSHE",  # 万科A
    "000063.XSHE",  # 中兴通讯
    "000100.XSHE",  # TCL科技
    "000858.XSHE",  # 五粮液
    "002415.XSHE",  # 海康威视
    "002594.XSHE",  # 比亚迪
    "600000.XSHG",  # 浦发银行
    "600036.XSHG",  # 招商银行
    "600519.XSHG",  # 贵州茅台
    "600887.XSHG",  # 伊利股份
    "601318.XSHG",  # 中国平安
    "601398.XSHG",  # 工商银行
    "601888.XSHG",  # 中国中免
    "603288.XSHG",  # 海天味业
    "300015.XSHE",  # 爱尔眼科
    "300059.XSHE",  # 东方财富
    "300124.XSHE",  # 汇川技术
    "300274.XSHE",  # 阳光电源
    "300408.XSHE",  # 三环集团
    "300498.XSHE",  # 温氏股份
    "300750.XSHE",  # 宁德时代
    "300760.XSHE",  # 迈瑞医疗
    "300782.XSHE",  # 卓胜微
    "301236.XSHE",  # 软通动力
]
START = "2025-07-26"
END = "2026-08-02"
USER = "18930501903"
HOST, PORT = "127.0.0.1", 8765
TICK = Decimal("0.01")

HTML = """<!doctype html><meta charset=utf-8><title>实验A 窗内扩样找封板</title>
<body style="font-family:sans-serif;max-width:28rem;margin:3rem auto">
<h1>实验 A · 权限窗内扩样找封板</h1>
<p>仅本机 127.0.0.1。密码只在本机调用 jqdatasdk，不外传、不落盘。</p>
<p>日期窗固定 2025-07-26～2026-08-02；约 25 只固定股票，非全市场。</p>
<form method=post>
<label>手机号（固定）<br><input value="18930501903" disabled style="width:100%"></label><br><br>
<label>登录密码<br><input name=password type=password required style="width:100%"></label><br><br>
<button type=submit>鉴权并扩样取数</button>
</form>
</body>"""


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


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
    if c.startswith("300") or c.startswith("301") or c.startswith("688"):
        return "chi_next", 0.20
    return "main", 0.10


def enrich(raw):
    import pandas as pd

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
        if dt < START or dt > END:
            continue
        rows.append(
            {
                "date": dt,
                "code": code,
                "symbol": code,
                "board": board,
                "limit_pct": pct,
                "pre_close": pre,
                "open": o,
                "high": h,
                "low": l,
                "close": c,
                "volume": vol,
                "money": float(getattr(r, "money", 0) or 0),
                "paused": paused,
                "limit_up": limit_up,
                "limit_down": limit_down,
                "is_one_word_up": bool(one_up),
                "is_one_word_down": bool(one_down),
                "is_limit_up_close": bool(close_up),
                "is_limit_down_close": bool(close_down),
                "is_suspended": bool(paused) or vol <= 0,
            }
        )
    return pd.DataFrame(rows)


def do_fetch(password: str) -> None:
    import jqdatasdk as jq
    import pandas as pd

    STATUS["state"] = "authing"
    jq.set_params(request_timeout=60, request_attempt_count=2, enable_auth_prompt=False)
    jq.auth(USER, password)
    if not jq.is_auth():
        raise RuntimeError("is_auth=False")
    try:
        qc = jq.get_query_count()
        qc_note = json.dumps(qc, ensure_ascii=False) if isinstance(qc, dict) else str(type(qc).__name__)
    except Exception as e:
        qc = None
        qc_note = f"query_count_err={type(e).__name__}: {e}"

    STATUS["state"] = "fetching"
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
            continue
        df = df.reset_index().rename(columns={"index": "date"})
        df["code"] = code
        frames.append(df)
    if not frames:
        raise RuntimeError("NO_DATA")

    raw = pd.concat(frames, ignore_index=True)
    enriched = enrich(raw)
    DATA.mkdir(parents=True, exist_ok=True)
    enriched.to_parquet(OUT_PQ, index=False)

    seal_mask = (
        enriched["is_one_word_up"]
        | enriched["is_one_word_down"]
        | enriched["is_limit_up_close"]
        | enriched["is_limit_down_close"]
    )
    seal = enriched.loc[seal_mask].copy()
    seal.to_parquet(OUT_SEAL, index=False)

    counts = {
        "n_one_word_up": int(enriched["is_one_word_up"].sum()),
        "n_one_word_down": int(enriched["is_one_word_down"].sum()),
        "n_close_seal_up": int(enriched["is_limit_up_close"].sum()),
        "n_close_seal_down": int(enriched["is_limit_down_close"].sum()),
        "n_suspended": int(enriched["is_suspended"].sum()),
        "n_seal_subset_rows": int(len(seal)),
    }
    meta = {
        "as_of": datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds"),
        "vendor": "joinquant/jqdatasdk",
        "jqdatasdk_version": getattr(jq, "__version__", "unknown"),
        "codes": CODES,
        "n_codes": len(CODES),
        "start": START,
        "end": END,
        "fq": None,
        "rows": int(len(enriched)),
        "date_min": str(enriched["date"].min()) if len(enriched) else None,
        "date_max": str(enriched["date"].max()) if len(enriched) else None,
        "parquet": OUT_PQ.name,
        "seal_subset": OUT_SEAL.name,
        "sha256": sha256_file(OUT_PQ),
        "limit_event_counts": counts,
        "seal_subset_empty": len(seal) == 0,
        "query_count": qc if isinstance(qc, dict) else qc_note,
        "note": "expand_seal_fetch_server; permission window only; fixed code list; NOT full market",
    }
    OUT_META.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")

    as_of = datetime.now().astimezone().isoformat(timespec="seconds")
    lines = [
        "AUTH_OK",
        f"as_of={as_of}",
        f"user={USER}",
        f"query_count={qc_note}",
        f"start={START}",
        f"end={END}",
        f"n_codes={len(CODES)}",
        f"total_rows={len(enriched)}",
        f"limit_event_counts={json.dumps(counts, ensure_ascii=False)}",
        f"seal_subset_empty={len(seal) == 0}",
        f"seal_subset_rows={len(seal)}",
        f"parquet={OUT_PQ.name}",
        f"seal_subset={OUT_SEAL.name}",
        "",
    ]
    OUT_EV.write_text("\n".join(lines), encoding="utf-8")

    try:
        jq.logout()
    except Exception:
        pass
    STATUS["state"] = "done"
    STATUS["detail"] = (
        f"rows={len(enriched)} seal={len(seal)} "
        f"one_up={counts['n_one_word_up']} close_up={counts['n_close_seal_up']}"
    )


class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):
        sys.stderr.write("%s - %s\n" % (self.address_string(), fmt % args))

    def do_GET(self):
        if self.path.startswith("/status"):
            body = json.dumps(STATUS).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        body = HTML.encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        raw = self.rfile.read(length).decode("utf-8", errors="replace")
        password = (parse_qs(raw).get("password") or [""])[0]
        if not password:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"missing password")
            return
        try:
            do_fetch(password)
            msg = (
                "<h1>成功</h1><p>AUTH_OK，扩样与封板子集已写入 data/。</p>"
                f"<pre>{STATUS.get('detail','')}</pre>"
                "<p>可关闭此页，并告诉总管「扩样页已提交成功」。</p>"
            )
        except Exception as e:
            STATUS["state"] = "error"
            STATUS["detail"] = type(e).__name__
            msg = f"<h1>失败</h1><pre>{type(e).__name__}: {e}</pre>"
            traceback.print_exc()
        finally:
            password = None  # noqa
        body = f"<!doctype html><meta charset=utf-8><body>{msg}</body>".encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)
        if STATUS.get("state") == "done":
            threading.Thread(target=lambda: HTTPServer.shutdown(self.server), daemon=True).start()
        else:
            STATUS["state"] = "waiting"
            STATUS["detail"] = STATUS.get("detail") or "last_attempt_failed"


def main() -> int:
    DATA.mkdir(parents=True, exist_ok=True)
    httpd = HTTPServer((HOST, PORT), Handler)
    print(f"OPEN http://{HOST}:{PORT}/  (expand seal fetch waiting)", flush=True)
    httpd.serve_forever()
    print("SERVER_STOPPED state=", STATUS["state"], STATUS.get("detail"), flush=True)
    return 0 if STATUS["state"] == "done" else 1


if __name__ == "__main__":
    raise SystemExit(main())
