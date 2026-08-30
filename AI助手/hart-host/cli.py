#!/usr/bin/env python3
"""FY301-first HART CLI. Writes disabled unless --write."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from devices.fy301 import load_learned, match_intent
from hart.commands import parse_command_0, parse_command_1, parse_command_2, parse_command_3


LOG_DIR = ROOT / "learn_log"


def log_session(event: dict) -> None:
    LOG_DIR.mkdir(exist_ok=True)
    p = LOG_DIR / f"{datetime.now(timezone.utc).strftime('%Y%m%d')}.jsonl"
    event["ts"] = datetime.now(timezone.utc).isoformat()
    p.open("a", encoding="utf-8").write(json.dumps(event, ensure_ascii=False) + "\n")


def cmd_say(args: argparse.Namespace) -> int:
    name, spec = match_intent(args.text)
    print(f"意图: {name}")
    print(json.dumps(spec, ensure_ascii=False, indent=2))
    if spec.get("command") is None:
        print("尚未学会该 HART 命令。接上 modem 后用 poll/read/probe，对照 Trex 把结果发我。")
        return 2
    if spec.get("write") and not args.write:
        print("这是写/方法类操作，默认拒绝。确认现场安全后加 --write。")
        return 3
    if args.dry_run or not args.port:
        print("dry-run 或未指定 --port，不发帧。")
        return 0
    return run_command(args, spec["command"])


def open_modem(args):
    from hart.uart import HartModem

    return HartModem(args.port, baud=args.baud, timeout=args.timeout)


def run_command(args, command: int, payload: bytes = b"") -> int:
    modem = open_modem(args)
    try:
        parsed, raw = modem.transact_parsed(command, payload)
    except Exception as e:
        print(f"失败: {e}")
        log_session({"op": "error", "command": command, "error": str(e)})
        return 1
    finally:
        modem.close()
    rec = {
        "op": "rx",
        "command": command,
        "raw_hex": raw.hex(),
        "data_hex": parsed.data.hex(),
    }
    log_session(rec)
    print(f"CMD {command} data={parsed.data.hex()}")
    try:
        if command == 0:
            ident = parse_command_0(parsed.data)
            print(ident)
        elif command == 1:
            print(parse_command_1(parsed.data))
        elif command == 2:
            print(parse_command_2(parsed.data))
        elif command == 3:
            print(parse_command_3(parsed.data))
    except ValueError as e:
        print(f"解析提示: {e}（把 raw_hex 发我一起看）")
    return 0


def cmd_poll(args) -> int:
    return run_command(args, 0)


def cmd_read(args) -> int:
    for c in (1, 2, 3):
        print(f"--- command {c} ---")
        rc = run_command(args, c)
        if rc:
            return rc
    return 0


def cmd_probe(args) -> int:
    start, end = args.range
    for c in range(start, end + 1):
        print(f"--- probe command {c} ---")
        try:
            run_command(args, c)
        except Exception as e:
            print(e)
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description="FY301-first HART host")
    p.add_argument("--port", help="USB modem COM, e.g. COM5 or /dev/ttyUSB0")
    p.add_argument("--baud", type=int, default=1200)
    p.add_argument("--timeout", type=float, default=2.0)
    p.add_argument("--write", action="store_true", help="允许写/方法（默认只读）")
    p.add_argument("--dry-run", action="store_true")
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("say", help="中文/自然语言意图")
    s.add_argument("text")
    s.set_defaults(func=cmd_say)

    sub.add_parser("poll", help="HART Command 0").set_defaults(func=cmd_poll)
    sub.add_parser("read", help="Command 1/2/3").set_defaults(func=cmd_read)

    pr = sub.add_parser("probe", help="扫描命令号（只读探测）")
    pr.add_argument("--range", nargs=2, type=int, default=[0, 3], metavar=("FROM", "TO"))
    pr.set_defaults(func=cmd_probe)

    args = p.parse_args()
    if args.cmd in ("poll", "read", "probe") and not args.port and not args.dry_run:
        print("需要 --port，或加 --dry-run")
        return 2
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
