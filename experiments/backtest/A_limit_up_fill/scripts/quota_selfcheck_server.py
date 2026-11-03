#!/usr/bin/env python3
"""Local-only quota/permission self-check; never log secrets."""
from __future__ import annotations

import json
import sys
import threading
import traceback
from datetime import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import parse_qs

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = DATA / "quota_check_evidence.txt"
OUT_JSON = DATA / "quota_check_evidence.json"
STATUS = {"state": "waiting", "detail": ""}
USER = "18930501903"
HOST, PORT = "127.0.0.1", 8765
PROBE_OUT = ("000001.XSHE", "2024-08-01", "2024-08-01")  # outside yesterday window
PROBE_IN = ("000001.XSHE", "2026-07-28", "2026-07-28")   # inside window

HTML = """<!doctype html><meta charset=utf-8><title>实验A 额度自检</title>
<body style="font-family:sans-serif;max-width:28rem;margin:3rem auto">
<h1>实验 A · 额度/权限窗自检</h1>
<p>仅本机 127.0.0.1。密码只在本机调用 jqdatasdk，不外传。</p>
<form method=post>
<label>手机号（固定）<br><input value="18930501903" disabled style="width:100%"></label><br><br>
<label>登录密码<br><input name=password type=password required style="width:100%"></label><br><br>
<button type=submit>鉴权并自检额度</button>
</form>
</body>"""


def run_check(password: str) -> dict:
    import jqdatasdk as jq

    STATUS["state"] = "authing"
    jq.set_params(request_timeout=60, request_attempt_count=2, enable_auth_prompt=False)
    jq.auth(USER, password)
    if not jq.is_auth():
        raise RuntimeError("is_auth=False")

    result = {
        "as_of": datetime.now().astimezone().isoformat(timespec="seconds"),
        "user": USER,
        "jqdatasdk_version": getattr(jq, "__version__", "unknown"),
        "AUTH_OK": True,
    }
    try:
        qc = jq.get_query_count()
        result["query_count"] = qc if isinstance(qc, dict) else {"raw_type": type(qc).__name__, "raw": str(qc)}
    except Exception as e:
        result["query_count_err"] = f"{type(e).__name__}: {e}"

    def probe(label, code, start, end):
        try:
            df = jq.get_price(
                code,
                start_date=start,
                end_date=end,
                frequency="daily",
                fields=["close"],
                skip_paused=False,
                fq=None,
            )
            n = 0 if df is None else len(df)
            return {"ok": True, "code": code, "start": start, "end": end, "rows": n}
        except Exception as e:
            return {
                "ok": False,
                "code": code,
                "start": start,
                "end": end,
                "error_type": type(e).__name__,
                "error": str(e),
            }

    result["probe_outside_window"] = probe("out", *PROBE_OUT)
    result["probe_inside_window"] = probe("in", *PROBE_IN)

    # permission window hint from errors or success
    out = result["probe_outside_window"]
    inn = result["probe_inside_window"]
    if not out.get("ok") and out.get("error"):
        result["permission_window_hint"] = out["error"]
    elif out.get("ok") and inn.get("ok"):
        result["permission_window_hint"] = "outside probe succeeded; window may have expanded vs 2025-07-26..2026-08-02"
    else:
        result["permission_window_hint"] = "see probe results"

    DATA.mkdir(parents=True, exist_ok=True)
    lines = [
        "QUOTA_CHECK_OK" if result.get("AUTH_OK") else "QUOTA_CHECK_FAIL",
        f"as_of={result['as_of']}",
        f"user={USER}",
        f"query_count={json.dumps(result.get('query_count') or result.get('query_count_err'), ensure_ascii=False)}",
        f"probe_outside={json.dumps(result['probe_outside_window'], ensure_ascii=False)}",
        f"probe_inside={json.dumps(result['probe_inside_window'], ensure_ascii=False)}",
        f"permission_window_hint={result.get('permission_window_hint','')}",
        "",
    ]
    OUT.write_text("\n".join(lines), encoding="utf-8")
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    try:
        jq.logout()
    except Exception:
        pass
    STATUS["state"] = "done"
    STATUS["detail"] = f"wrote {OUT.name}"
    return result


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
            result = run_check(password)
            msg = (
                "<h1>完成</h1><pre>"
                + json.dumps(result, ensure_ascii=False, indent=2)
                + "</pre><p>可关闭此页。</p>"
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
    print(f"OPEN http://{HOST}:{PORT}/  (quota self-check)", flush=True)
    httpd.serve_forever()
    print("SERVER_STOPPED state=", STATUS["state"], STATUS.get("detail"), flush=True)
    return 0 if STATUS["state"] == "done" else 1


if __name__ == "__main__":
    raise SystemExit(main())
