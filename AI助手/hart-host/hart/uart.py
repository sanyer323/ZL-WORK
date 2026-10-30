"""USB HART modem as virtual serial port (typical 1200 8O1)."""

from __future__ import annotations

import time

import serial

from hart.frame import build_master_frame, parse_response, wrap_preamble


class HartModem:
    def __init__(self, port: str, baud: int = 1200, timeout: float = 2.0, preamble: int = 5):
        self.port = port
        self.preamble = preamble
        self.ser = serial.Serial(
            port=port,
            baudrate=baud,
            bytesize=serial.EIGHTBITS,
            parity=serial.PARITY_ODD,
            stopbits=serial.STOPBITS_ONE,
            timeout=timeout,
        )

    def close(self) -> None:
        self.ser.close()

    def transact(self, command: int, payload: bytes = b"", *, long_addr: bytes | None = None, poll_addr: int = 0) -> bytes:
        frame = wrap_preamble(
            build_master_frame(command, payload, long_addr=long_addr, poll_addr=poll_addr),
            self.preamble,
        )
        self.ser.reset_input_buffer()
        self.ser.write(frame)
        self.ser.flush()
        time.sleep(0.05)
        raw = self.ser.read(512)
        if not raw:
            raise TimeoutError("HART 无应答：查回路电阻≥250Ω、仪表供电、COM 口")
        return raw

    def transact_parsed(self, command: int, payload: bytes = b"", **kw):
        raw = self.transact(command, payload, **kw)
        return parse_response(raw), raw
