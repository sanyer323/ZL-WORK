"""HART UART frame encode/decode (master → field device)."""

from __future__ import annotations

from dataclasses import dataclass


def xor_checksum(data: bytes) -> int:
    x = 0
    for b in data:
        x ^= b
    return x


@dataclass
class HartFrame:
    delimiter: int
    address: bytes
    command: int
    data: bytes
    checksum: int

    @property
    def is_long(self) -> bool:
        return (self.delimiter & 0x80) != 0


def build_master_frame(command: int, payload: bytes = b"", *, long_addr: bytes | None = None, poll_addr: int = 0) -> bytes:
    """long_addr: 5 bytes (manufacturer+type+id) if known; else short frame poll."""
    if long_addr and len(long_addr) == 5:
        delimiter = 0x82
        # Primary master, burst off
        addr = bytes([long_addr[0] | 0x80, *long_addr[1:]])
    else:
        delimiter = 0x02
        addr = bytes([0x80 | (poll_addr & 0x3F)])
    body = bytes([delimiter]) + addr + bytes([command, len(payload)]) + payload
    return body + bytes([xor_checksum(body)])


def wrap_preamble(frame: bytes, n: int = 5) -> bytes:
    return bytes([0xFF] * n) + frame


def parse_response(buf: bytes) -> HartFrame:
    """Find first non-0xFF after preamble and parse one frame."""
    i = 0
    while i < len(buf) and buf[i] == 0xFF:
        i += 1
    if i >= len(buf):
        raise ValueError("no HART frame (only preamble)")
    delim = buf[i]
    i += 1
    if delim & 0x80:
        addr = buf[i : i + 5]
        i += 5
    else:
        addr = buf[i : i + 1]
        i += 1
    cmd = buf[i]
    bc = buf[i + 1]
    i += 2
    data = buf[i : i + bc]
    i += bc
    chk = buf[i]
    body = bytes([delim]) + addr + bytes([cmd, bc]) + data
    if xor_checksum(body) != chk:
        raise ValueError("HART checksum mismatch")
    return HartFrame(delim, addr, cmd, data, chk)
