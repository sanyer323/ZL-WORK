#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EA10 Step 4：F10 型 A 阀杆推力、螺纹、轴承校核。"""

from __future__ import annotations

import math
from dataclasses import dataclass


@dataclass
class F10:
    d1: float = 125.0
    pcd: float = 102.0
    spigot: float = 70.0
    holes: int = 4
    hole: float = 11.0
    bolt: str = "M10"
    h_spigot: float = 3.0
    stem_max: float = 20.0


@dataclass
class StemNut:
    """Tr20x4 梯形螺纹阀杆螺母（F10 型 A 上限）。"""

    d: float = 20.0
    pitch: float = 4.0
    dm: float = 18.0
    mu: float = 0.12
    length: float = 100.0
    torque_nm: float = 100.0
    breakout_nm: float = 150.0
    bronze_limit_mpa: float = 32.0  # ZCuAl10Fe3 短时

    @property
    def lead_angle_rad(self) -> float:
        return math.atan(self.pitch / (math.pi * self.dm))

    @property
    def friction_angle_rad(self) -> float:
        return math.atan(self.mu)

    def thrust_n(self, torque_nm: float) -> float:
        # 旋转螺母、阀杆升降：T = F*(dm/2)*tan(α+ρ)
        return torque_nm / ((self.dm / 2000.0) * math.tan(self.lead_angle_rad + self.friction_angle_rad))

    @property
    def engaged_turns(self) -> float:
        return self.length / self.pitch

    def thread_pressure_mpa(self, torque_nm: float) -> float:
        # 近似投影：π dm (0.5 p) z
        z = self.engaged_turns
        area = math.pi * self.dm * (0.5 * self.pitch) * z
        return self.thrust_n(torque_nm) / area


@dataclass
class WormMesh:
    m: float = 2.5
    d2: float = 175.0
    face: float = 28.0
    torque_nm: float = 100.0

    @property
    def ft_n(self) -> float:
        return 2.0 * self.torque_nm / (self.d2 / 1000.0)

    @property
    def pressure_mpa(self) -> float:
        return self.ft_n / (self.face * 2.0 * self.m)


def main() -> None:
    f10 = F10()
    nut = StemNut()
    mesh = WormMesh()
    t_r, t_b = nut.torque_nm, nut.breakout_nm
    f_r, f_b = nut.thrust_n(t_r), nut.thrust_n(t_b)
    print("EA10 DRIVE  F10 TYPE A")
    print(f"  flange d1={f10.d1:.0f}  PCD={f10.pcd:.0f}  spigot={f10.spigot:.0f}  4x{f10.bolt}  stem_max={f10.stem_max:.0f}")
    print(
        f"  nut Tr{nut.d:.0f}x{nut.pitch:.0f}  dm={nut.dm:.0f}  "
        f"alpha={math.degrees(nut.lead_angle_rad):.2f} deg  rho={math.degrees(nut.friction_angle_rad):.2f} deg"
    )
    print(f"  F_stem rated={f_r/1000:.1f} kN  breakout={f_b/1000:.1f} kN")
    print(f"  thread p={nut.thread_pressure_mpa(t_r):.1f} MPa rated / {nut.thread_pressure_mpa(t_b):.1f} MPa breakout (Al-bronze ~{nut.bronze_limit_mpa:.0f})")
    print(f"  worm Ft={mesh.ft_n:.0f} N  p={mesh.pressure_mpa:.1f} MPa (tin-bronze S2 limit ~12 MPa)")
    print("  worm bearings: 7204 AC pair   C~14 kN  >> Fr=Fa~0.18 kN")
    print("  output radial: 6010 x2        50x80x16")
    print("  output thrust: 81210          50x78x22  C0~120 kN")
    if nut.thread_pressure_mpa(t_b) > nut.bronze_limit_mpa:
        raise SystemExit("nut pressure too high")
    if mesh.pressure_mpa > 12:
        raise SystemExit("worm mesh pressure too high")
    if f_b > 120_000:
        raise SystemExit("81210 static capacity short")
    print("  STEP4_GATE: F10 + Tr20x4 L100 + 81210 OK")


if __name__ == "__main__":
    main()
