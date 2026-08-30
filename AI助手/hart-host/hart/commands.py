"""HART universal / common-practice command helpers."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Identity:
    manufacturer_id: int
    device_type: int
    device_id: bytes
    univ_rev: int
    device_rev: int
    software_rev: int
    long_addr: bytes


def parse_command_0(data: bytes) -> Identity:
    """Command 0 response data (skip 2 status bytes at start of data)."""
    if len(data) < 2:
        raise ValueError("cmd0 too short")
    status, payload = data[:2], data[2:]
    _ = status
    # Packed format varies slightly by revision; common layout:
    # [0] expansion, [1] manuf, [2] type, [3] preambles, [4] univ, [5] device rev,
    # [6] sw, [7] hw, [8] flags, [9:12] device id
    if len(payload) < 12:
        raise ValueError(f"cmd0 payload short: {payload.hex()}")
    manuf = payload[1]
    dtype = payload[2]
    univ = payload[4]
    drev = payload[5]
    srev = payload[6]
    dev_id = payload[9:12]
    long_addr = bytes([manuf, dtype]) + dev_id
    return Identity(manuf, dtype, dev_id, univ, drev, srev, long_addr)


def parse_command_1(data: bytes) -> dict:
    """Primary variable."""
    st, p = data[:2], data[2:]
    if len(p) < 5:
        return {"status": st.hex(), "raw": p.hex()}
    units = p[0]
    # IEEE754 float
    import struct

    pv = struct.unpack(">f", p[1:5])[0]
    return {"status": st.hex(), "pv": pv, "units_code": units}


def parse_command_2(data: bytes) -> dict:
    import struct

    st, p = data[:2], data[2:]
    if len(p) < 8:
        return {"status": st.hex(), "raw": p.hex()}
    current = struct.unpack(">f", p[0:4])[0]
    percent = struct.unpack(">f", p[4:8])[0]
    return {"status": st.hex(), "loop_current_mA": current, "percent": percent}


def parse_command_3(data: bytes) -> dict:
    import struct

    st, p = data[:2], data[2:]
    out = {"status": st.hex()}
    if len(p) >= 4:
        out["loop_current_mA"] = struct.unpack(">f", p[0:4])[0]
    names = ("pv", "sv", "tv", "qv")
    i = 4
    vars_ = []
    while i + 5 <= len(p):
        code = p[i]
        val = struct.unpack(">f", p[i + 1 : i + 5])[0]
        vars_.append({"units_code": code, "value": val})
        i += 5
    for n, v in zip(names, vars_):
        out[n] = v
    return out
