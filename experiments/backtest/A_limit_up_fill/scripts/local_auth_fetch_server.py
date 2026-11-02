#!/usr/bin/env python3
"""Local-only one-shot page: user posts password on 127.0.0.1; never log secrets."""
from __future__ import annotations

import hashlib
import json
import os
import sys
import threading
import traceback
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import parse_qs

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT_PQ = DATA / "daily_min_sample.parquet"
OUT_META = DATA / "daily_min_sample_meta.json"
OUT_AUTH = DATA / "auth_evidence.txt"
STATUS = {"state": "waiting", "detail": ""}

CODES = ["000001.XSHE", "600000.XSHG", "300750.XSHE"]
START = "2024-07-01"
END = "2024-09-30"
USER = "18930501903"
HOST, PORT = "127.0.0.1", 8765

HTML = """<!doctype html><meta charset=utf-8><title>实验A 聚宽鉴权</title>
<body style="font-family:sans-serif;max-width:28rem;margin:3rem auto">
<h1>实验 A · 聚宽鉴权</h1>
<p>仅本机 127.0.0.1。密码不会发给回测 Bot，只在本机进程里调用 jqdatasdk。</p>
<form method=post>
<label>手机号（固定）<br><input value="18930501903" disabled style="width:100%"></label><br><br>
<label>登录密码<br><input name=password type=password required style="width:100%"></label><br><br>
<button type=submit>鉴权并拉最小日频</button>
</form>
<p style="color:#666">完成后可关闭此页。窗口保持开着直到提示成功。</p>
</body>"""


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def do_fetch(password: str) -> None:
    import jqdatasdk as jq

    STATUS["state"] = "authing"
    jq.set_params(request_timeout=60, request_attempt_count=2, enable_auth_prompt=False)
    jq.auth(USER, password)
    if not jq.is_auth():
        raise RuntimeError("is_auth=False")
    try:
        qc = jq.get_query_count()
        qc_note = f"query_count_keys={sorted(qc.keys()) if isinstance(qc, dict) else type(qc).__name__}"
    except Exception as e:
        qc_note = f"query_count_err={type(e).__name__}"
    OUT_AUTH.write_text(
        f"AUTH_OK\nas_of={datetime.now().astimezone().isoformat(timespec='seconds')}\nuser={USER}\n{qc_note}\n",
        encoding="utf-8",
    )
    STATUS["state"] = "fetching"
    frames = []
    import pandas as pd

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
    all_df = pd.concat(frames, ignore_index=True)
    DATA.mkdir(parents=True, exist_ok=True)
    all_df.to_parquet(OUT_PQ, index=False)
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
        "rows": int(len(all_df)),
        "parquet": OUT_PQ.name,
        "sha256": sha256_file(OUT_PQ),
        "security_info": info_rows,
        "auth_evidence": OUT_AUTH.name,
        "note": "minimal sample via local_auth_fetch_server; China-IP host",
    }
    OUT_META.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    try:
        jq.logout()
    except Exception:
        pass
    STATUS["state"] = "done"
    STATUS["detail"] = f"rows={len(all_df)} sha256={meta['sha256'][:16]}..."


class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):
        # never log body/password
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
        qs = parse_qs(raw)
        password = (qs.get("password") or [""])[0]
        if not password:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"missing password")
            return
        try:
            do_fetch(password)
            msg = (
                "<h1>成功</h1><p>AUTH_OK，样本已写入 data/。</p>"
                f"<pre>{STATUS.get('detail','')}</pre>"
                "<p>可关闭此页，并告诉总管/回测「本机页已提交成功」。</p>"
            )
        except Exception as e:
            STATUS["state"] = "error"
            STATUS["detail"] = type(e).__name__
            msg = f"<h1>失败</h1><pre>{type(e).__name__}: {e}</pre>"
            # no password in traceback print to client carefully
            traceback.print_exc()
        finally:
            password = None  # noqa
        body = f"<!doctype html><meta charset=utf-8><body>{msg}</body>".encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)
        # Only stop on success so a wrong password can be retried without restarting.
        if STATUS.get("state") == "done":
            threading.Thread(target=lambda: (HTTPServer.shutdown(self.server)), daemon=True).start()
        else:
            STATUS["state"] = "waiting"
            STATUS["detail"] = STATUS.get("detail") or "last_attempt_failed"


def main() -> int:
    DATA.mkdir(parents=True, exist_ok=True)
    httpd = HTTPServer((HOST, PORT), Handler)
    print(f"OPEN http://{HOST}:{PORT}/  (waiting for local password submit)", flush=True)
    httpd.serve_forever()
    print("SERVER_STOPPED state=", STATUS["state"], STATUS.get("detail"), flush=True)
    return 0 if STATUS["state"] == "done" else 1


if __name__ == "__main__":
    raise SystemExit(main())
