#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EA10 机电定型计算。改参数后运行：python3 sizing.py"""

from __future__ import annotations

import math
from dataclasses import dataclass, replace


@dataclass
class Worm:
    module_mm: float = 2.5
    starts: int = 1
    wheel_teeth: int = 70
    diameter_quotient: float = 16.0
    mu: float = 0.08
    bearing_eta: float = 0.92

    @property
    def ratio(self) -> float:
        return self.wheel_teeth / self.starts

    @property
    def d1_mm(self) -> float:
        return self.diameter_quotient * self.module_mm

    @property
    def d2_mm(self) -> float:
        return self.module_mm * self.wheel_teeth

    @property
    def center_mm(self) -> float:
        return 0.5 * (self.d1_mm + self.d2_mm)

    @property
    def lead_angle_rad(self) -> float:
        return math.atan(self.starts / self.diameter_quotient)

    @property
    def friction_angle_rad(self) -> float:
        return math.atan(self.mu)

    @property
    def self_locking(self) -> bool:
        return self.lead_angle_rad < self.friction_angle_rad

    @property
    def worm_eta(self) -> float:
        g = self.lead_angle_rad
        p = self.friction_angle_rad
        if g + p <= 0:
            return 0.0
        return math.tan(g) / math.tan(g + p)

    @property
    def eta(self) -> float:
        return self.worm_eta * self.bearing_eta


@dataclass
class Motor:
    poles: int = 4
    freq_hz: float = 50.0
    rated_kw: float = 0.55
    slip: float = 0.067  # 1500 -> ~1400
    start_current_ratio: float = 6.5
    stall_torque_ratio: float = 2.2
    voltage: float = 380.0
    efficiency: float = 0.72
    pf: float = 0.75

    @property
    def sync_rpm(self) -> float:
        return 120.0 * self.freq_hz / self.poles

    @property
    def rated_rpm(self) -> float:
        return self.sync_rpm * (1.0 - self.slip)

    @property
    def rated_current_a(self) -> float:
        return (self.rated_kw * 1000.0) / (
            math.sqrt(3.0) * self.voltage * self.pf * self.efficiency
        )


@dataclass
class Duty:
    rated_nm: float = 100.0
    breakout_factor: float = 1.5
    hammer_deg: float = 12.0
    rotor_inertia: float = 0.0012  # kg·m²
    stem_travel_mm: float = 80.0
    stem_pitch_mm: float = 4.0
    cable_m: float = 80.0
    cable_section_mm2: float = 1.5
    copper_ohm_m_mm2: float = 0.018


@dataclass
class Sizing:
    worm: Worm
    motor: Motor
    duty: Duty

    @property
    def n_out_rpm(self) -> float:
        return self.motor.rated_rpm / self.worm.ratio

    @property
    def omega_out(self) -> float:
        return self.n_out_rpm * 2.0 * math.pi / 60.0

    @property
    def p_out_w(self) -> float:
        return self.duty.rated_nm * self.omega_out

    @property
    def p_motor_w(self) -> float:
        return self.p_out_w / self.worm.eta

    @property
    def t_motor_nm(self) -> float:
        return self.duty.rated_nm / (self.worm.ratio * self.worm.eta)

    @property
    def t_breakout_nm(self) -> float:
        return self.duty.rated_nm * self.duty.breakout_factor

    @property
    def p_breakout_w(self) -> float:
        return self.t_breakout_nm * self.omega_out / self.worm.eta

    @property
    def motor_ok(self) -> bool:
        return self.p_motor_w <= self.motor.rated_kw * 1000.0 * 1.02

    @property
    def stall_ok(self) -> bool:
        t_avail = (self.motor.rated_kw * 1000.0) / (
            self.motor.rated_rpm * 2.0 * math.pi / 60.0
        )
        return t_avail * self.motor.stall_torque_ratio >= self.t_motor_nm * self.duty.breakout_factor

    @property
    def axial_force_n(self) -> float:
        return self.t_motor_nm / (self.worm.d1_mm / 2000.0)

    @property
    def hammer_impact_j(self) -> float:
        # motor reaches ~0.7 sync in lost motion; KE at worm
        w = 0.7 * self.motor.sync_rpm * 2.0 * math.pi / 60.0
        return 0.5 * self.duty.rotor_inertia * w * w

    @property
    def stem_turns(self) -> float:
        return self.duty.stem_travel_mm / self.duty.stem_pitch_mm

    @property
    def stroke_s(self) -> float:
        return 60.0 * self.stem_turns / self.n_out_rpm

    @property
    def start_current_a(self) -> float:
        return self.motor.rated_current_a * self.motor.start_current_ratio

    @property
    def cable_drop_v(self) -> float:
        r = self.duty.copper_ohm_m_mm2 * self.duty.cable_m / self.duty.cable_section_mm2
        # 3-phase line drop ≈ √3 · I · R_one_way  (go-and-return in R of one conductor * length)
        return math.sqrt(3.0) * self.start_current_a * r

    @property
    def drop_ok(self) -> bool:
        return self.cable_drop_v / self.motor.voltage <= 0.10


def ea10_baseline() -> Sizing:
    return Sizing(Worm(), Motor(), Duty())


def report(s: Sizing) -> str:
    w, m, d = s.worm, s.motor, s.duty
    g = math.degrees(w.lead_angle_rad)
    p = math.degrees(w.friction_angle_rad)
    lines = [
        "EA10 BASELINE",
        f"  worm  m={w.module_mm} mm  z1={w.starts}  z2={w.wheel_teeth}  q={w.diameter_quotient}",
        f"  d1={w.d1_mm:.1f} mm  d2={w.d2_mm:.1f} mm  a={w.center_mm:.1f} mm  i={w.ratio:.1f}",
        f"  gamma={g:.2f} deg  phi={p:.2f} deg  self_lock={w.self_locking}  eta={w.eta:.3f}",
        f"  motor {m.rated_kw} kW  {m.rated_rpm:.0f} r/min  I_n={m.rated_current_a:.2f} A  I_st={s.start_current_a:.1f} A",
        f"  n_out={s.n_out_rpm:.2f} r/min  T_rated={d.rated_nm:.0f} N·m  T_bo={s.t_breakout_nm:.0f} N·m",
        f"  P_out={s.p_out_w:.0f} W  P_motor={s.p_motor_w:.0f} W  T_motor={s.t_motor_nm:.2f} N·m",
        f"  motor_ok={s.motor_ok}  stall_ok={s.stall_ok}  F_axial={s.axial_force_n:.0f} N",
        f"  hammer={d.hammer_deg:.0f} deg  KE={s.hammer_impact_j:.3f} J",
        f"  stem {d.stem_travel_mm:.0f} mm / {d.stem_pitch_mm:.0f} mm -> {s.stem_turns:.1f} turns  stroke={s.stroke_s:.1f} s",
        f"  cable {d.cable_m:.0f} m x {d.cable_section_mm2} mm2  dV_start={s.cable_drop_v:.1f} V  drop_ok={s.drop_ok}",
        f"  STEP3_GATE: lock={w.self_locking} power={s.motor_ok} stall={s.stall_ok} drop={s.drop_ok}",
    ]
    return "\n".join(lines)


def sweep_mu(base: Sizing | None = None) -> str:
    s0 = base or ea10_baseline()
    rows = ["mu      gamma   phi     lock   eta    P_m_W"]
    for mu in (0.04, 0.06, 0.08, 0.10, 0.12):
        s = replace(s0, worm=replace(s0.worm, mu=mu))
        rows.append(
            f"{mu:4.2f}   {math.degrees(s.worm.lead_angle_rad):5.2f}  "
            f"{math.degrees(s.worm.friction_angle_rad):5.2f}  "
            f"{str(s.worm.self_locking):5}  {s.worm.eta:5.3f}  {s.p_motor_w:6.0f}"
        )
    return "\n".join(rows)


def main() -> None:
    s = ea10_baseline()
    print(report(s))
    print()
    print("MU SWEEP (self-lock vs motor power)")
    print(sweep_mu(s))
    if not (s.worm.self_locking and s.motor_ok and s.stall_ok):
        raise SystemExit("EA10 baseline failed Step-3 gate")


if __name__ == "__main__":
    main()
