#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EA10 Step 5：编码分辨率与力矩垫圈 ADC 校核。"""

from __future__ import annotations

import math


def main() -> None:
    # 位置
    bits_st = 14  # AS5047P
    counts_st = 2**bits_st
    stroke_turns = 200.0  # 首台软件限
    valve_res = 100.0 / (stroke_turns * counts_st)  # % / count
    need_0p1 = 0.1  # %
    mt_bits = 12
    mt_turns = 2**mt_bits
    # 力矩
    fa_rated = 178.0  # N，与 sizing 一致
    fa_bo = fa_rated * 1.5
    fa_fs = 1000.0
    mv_per_v = 2.0
    v_ex = 5.0
    v_fs = (mv_per_v / 1000.0) * v_ex  # 10 mV @ 1 kN
    v_rated = v_fs * (fa_rated / fa_fs)
    pga = 32
    vref = 2.048
    lsb = vref / pga / (2**24)
    counts_rated = v_rated / lsb
    t_lsb = 100.0 / counts_rated  # N·m / LSB at rated mapping
    print("EA10 SENSE")
    print(f"  ST AS5047P {bits_st} bit  {counts_st} c/rev")
    print(f"  stroke {stroke_turns:.0f} turns  LSB={valve_res:.6f} %  0.1%_ok={valve_res < need_0p1}")
    print(f"  MT Wiegand {mt_bits} bit  {mt_turns} turns  cap_ok={mt_turns >= 500}")
    print(f"  Fa rated={fa_rated:.0f} N  breakout={fa_bo:.0f} N  FS={fa_fs:.0f} N")
    print(f"  bridge {v_fs*1000:.1f} mV FS  {v_rated*1000:.2f} mV @ rated")
    print(f"  ADS1220 PGA{pga}  LSB={lsb*1e9:.1f} nV  counts@rated={counts_rated:.0f}")
    print(f"  torque LSB={t_lsb*1000:.3f} mN·m  << 1 N·m set step")
    if valve_res >= need_0p1:
        raise SystemExit("encoder too coarse")
    if mt_turns < 500:
        raise SystemExit("multi-turn range short")
    if fa_bo > fa_fs:
        raise SystemExit("torque washer FS short")
    print("  STEP5_GATE: encoder + washer OK")


if __name__ == "__main__":
    main()
