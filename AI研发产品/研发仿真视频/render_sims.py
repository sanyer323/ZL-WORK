# -*- coding: utf-8 -*-
"""
SMAR FY301 研发仿真视频渲染器
依据 FY301ME 手册 + 3D脚本：压电 → 喷嘴挡板 → 先导压 → 膜片放大 → 滑阀 → 霍尔闭环
输出 MP4 到本目录 out/
"""
from __future__ import annotations

import math
import os
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation, FFMpegWriter
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch, Arc, Rectangle, Polygon, Ellipse
import numpy as np

# ---- paths / ffmpeg ----
OUT = Path(__file__).resolve().parent / "out"
OUT.mkdir(exist_ok=True)

try:
    import imageio_ffmpeg

    FF = imageio_ffmpeg.get_ffmpeg_exe()
    plt.rcParams["animation.ffmpeg_path"] = FF
except Exception:
    FF = None

# Chinese font on Windows — force YaHei / SimHei for CJK + monospace panels
from matplotlib import font_manager

_CJK = None
for _name in ("Microsoft YaHei", "SimHei", "Microsoft JhengHei", "Source Han Sans SC"):
    for _f in font_manager.fontManager.ttflist:
        if _f.name == _name:
            _CJK = _name
            break
    if _CJK:
        break
if _CJK is None:
    # fallback: search by filename
    for _f in font_manager.fontManager.ttflist:
        if "msyh" in (_f.fname or "").lower() or "simhei" in (_f.fname or "").lower():
            font_manager.fontManager.addfont(_f.fname)
            _CJK = _f.name
            break
if _CJK:
    plt.rcParams["font.family"] = "sans-serif"
    plt.rcParams["font.sans-serif"] = [_CJK, "DejaVu Sans"]
    plt.rcParams["font.monospace"] = [_CJK, "Consolas", "DejaVu Sans Mono"]
print("CJK font:", _CJK)
plt.rcParams["axes.unicode_minus"] = False

FPS = 20
DPI = 100
BG = "#0b1220"
FG = "#e8eef7"
ACCENT = "#4fc3f7"
WARN = "#ff8a65"
OK = "#81c784"
PIEZO = "#ce93d8"
AIR = "#ffb74d"


def style_ax(ax, title: str):
    ax.set_facecolor(BG)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title(title, color=FG, fontsize=14, pad=10, fontweight="bold")


def save_anim(fig, anim: FuncAnimation, name: str, fps: int = FPS):
    path = OUT / f"{name}.mp4"
    if FF:
        writer = FFMpegWriter(fps=fps, bitrate=2500, metadata={"title": name, "artist": "FY301-RD"})
        print(f"[..] rendering {name} ...", flush=True)
        anim.save(str(path), writer=writer, dpi=DPI)
        print(f"[OK] {path}")
    else:
        gif = OUT / f"{name}.gif"
        anim.save(str(gif), writer="pillow", fps=fps, dpi=DPI)
        print(f"[OK-GIF] {gif}")
    plt.close(fig)


# ============================================================
# 01 压电陶瓷：逆压电效应 + 电容低功耗 + FY301挡板弯曲
# ============================================================
def render_01_piezo():
    fig = plt.figure(figsize=(12.8, 7.2), facecolor=BG)
    # 2x2 layout via gridspec-like axes
    ax_lat = fig.add_axes([0.04, 0.52, 0.45, 0.40], facecolor=BG)
    ax_disk = fig.add_axes([0.52, 0.52, 0.45, 0.40], facecolor=BG)
    ax_elec = fig.add_axes([0.04, 0.08, 0.45, 0.38], facecolor=BG)
    ax_param = fig.add_axes([0.52, 0.08, 0.45, 0.38], facecolor=BG)
    for ax, t in (
        (ax_lat, "① 晶格：逆压电效应（电场→形变）"),
        (ax_disk, "② 压电盘弯曲（FY301 挡板）"),
        (ax_elec, "③ 电气等效：电容（稳态近零功耗）"),
        (ax_param, "④ FY301 工程参数（手册）"),
    ):
        ax.set_title(t, color=FG, fontsize=11, pad=6)
        ax.tick_params(colors=FG)
        for sp in ax.spines.values():
            sp.set_color("#334155")

    n = 120  # 6s @20fps

    # lattice artists
    ax_lat.set_xlim(-1.2, 1.2)
    ax_lat.set_ylim(-1.2, 1.2)
    ax_lat.set_aspect("equal")
    ax_lat.axis("off")
    dots = []
    base = []
    for i in range(-2, 3):
        for j in range(-2, 3):
            (d,) = ax_lat.plot([i * 0.35], [j * 0.35], "o", color=ACCENT, markersize=10)
            dots.append(d)
            base.append((i * 0.35, j * 0.35))
    e_arrow = FancyArrowPatch((-0.9, -1.0), (-0.9, 1.0), arrowstyle="->", color=WARN, mutation_scale=14, lw=2)
    ax_lat.add_patch(e_arrow)
    ax_lat.text(-1.05, 0, "E", color=WARN, fontsize=12, ha="right", va="center")
    lat_txt = ax_lat.text(0, -1.1, "V = 0 V", color=FG, ha="center", fontsize=11)

    # disk artists
    ax_disk.set_xlim(-2.2, 2.2)
    ax_disk.set_ylim(-1.4, 1.6)
    ax_disk.set_aspect("equal")
    ax_disk.axis("off")
    (disk_line,) = ax_disk.plot([], [], color=PIEZO, lw=4)
    ax_disk.plot([-1.8, 1.8], [-0.55, -0.55], color="#64748b", lw=2)  # support plane
    # nozzle sketch
    nozzle = patches.FancyBboxPatch((-0.18, -1.15), 0.36, 0.55, boxstyle="round,pad=0.02", linewidth=1.5, edgecolor=AIR, facecolor="#1e293b")
    ax_disk.add_patch(nozzle)
    ax_disk.text(0, -1.25, "喷嘴", color=AIR, ha="center", fontsize=9)
    gap_txt = ax_disk.text(0.9, 0.2, "间隙 δ", color=FG, fontsize=10)
    disk_v = ax_disk.text(0, 1.35, "V = 0 V", color=PIEZO, ha="center", fontsize=11)

    # electrical
    ax_elec.set_xlim(0, 10)
    ax_elec.set_ylim(-0.2, 1.3)
    ax_elec.set_xlabel("时间 t", color=FG)
    ax_elec.set_ylabel("电流 / 电压(归一化)", color=FG)
    (i_line,) = ax_elec.plot([], [], color=WARN, lw=2, label="充电电流 i")
    (v_line,) = ax_elec.plot([], [], color=ACCENT, lw=2, label="电压 V")
    ax_elec.legend(loc="upper right", facecolor="#1e293b", edgecolor="#334155", labelcolor=FG, fontsize=8)
    ax_elec.set_facecolor("#111827")

    # params panel
    ax_param.axis("off")
    ax_param.set_xlim(0, 1)
    ax_param.set_ylim(0, 1)
    param_box = ax_param.text(
        0.02,
        0.95,
        "",
        color=FG,
        fontsize=10,
        va="top",
        linespacing=1.45,
    )
    fig.suptitle("FY301 研发仿真 · 压电陶瓷工作原理", color=FG, fontsize=16, fontweight="bold", y=0.98)

    def frame(k):
        t = k / n
        # voltage cycle: 0 → 100 → 0 → hold mid
        if t < 0.35:
            V = 100 * (t / 0.35)
        elif t < 0.55:
            V = 100
        elif t < 0.85:
            V = 100 * (1 - (t - 0.55) / 0.30)
        else:
            V = 50
        # strain factor 0..1
        s = V / 100.0

        # lattice stretch along E (y), compress x
        sx, sy = 1 - 0.18 * s, 1 + 0.28 * s
        for d, (x0, y0) in zip(dots, base):
            d.set_data([x0 * sx], [y0 * sy])
        lat_txt.set_text(f"V = {V:.0f} V   ε_y↑  ε_x↓")

        # disk bend (parabolic, fixed ends)
        xs = np.linspace(-1.6, 1.6, 80)
        bend = 0.55 * s * (1 - (xs / 1.6) ** 2)
        disk_line.set_data(xs, bend)
        # gap from nozzle tip y=-0.6 to disk center
        delta = 0.55 - bend[len(xs) // 2] + 0.05
        gap_txt.set_text(f"间隙 δ ≈ {delta * 100:.1f} (相对单位)")
        gap_txt.set_position((0.95, bend[len(xs) // 2] + 0.15))
        disk_v.set_text(f"V = {V:.0f} V  |  运行区约 30–70 V")

        # capacitor charge transient when voltage ramps
        tt = np.linspace(0, 1, 200)
        # approximate: V(t) schedule
        Vs = []
        Is = []
        for u in tt:
            if u < 0.35:
                vv = 100 * (u / 0.35)
                ii = 1.0  # charging
            elif u < 0.55:
                vv = 100
                ii = 0.02
            elif u < 0.85:
                vv = 100 * (1 - (u - 0.55) / 0.30)
                ii = -0.8  # discharge
            else:
                vv = 50
                ii = 0.02
            Vs.append(vv / 100)
            Is.append(ii * math.exp(-((u % 0.35) * 12)) if abs(ii) > 0.1 else ii * 0.05)
        # update only up to current time
        m = max(2, int(t * 200))
        v_line.set_data(tt[:m] * 10, Vs[:m])
        i_line.set_data(tt[:m] * 10, np.clip(Is[:m], -0.2, 1.2))

        # FYCAL mapping @ 20 psi supply (handbook)
        # 0V→≤2psi, 50V→5.8-6.2, 100V→12-13
        if V < 50:
            Pp = 2 + (V / 50) * (6.0 - 2)
        else:
            Pp = 6.0 + ((V - 50) / 50) * (12.5 - 6.0)
        param_box.set_text(
            "FY301 压电驱动要点（手册）\n"
            "─────────────────────────────────\n"
            f"驱动电压 V_piezo     = {V:5.1f} V\n"
            f"典型监控区间         = 30 – 70 V\n"
            f"FYCAL 校准点         = 0 / 50 / 100 V\n"
            f"先导压 P_pilot(@20psi供气) ≈ {Pp:4.1f} psi\n"
            "电气模型               ≈ 电容 C\n"
            "稳态电流               ≈ 0（仅充放电瞬态）\n"
            "回路最低工作电流       = 3.8 mA\n"
            "─────────────────────────────────\n"
            "链路：V↑ → 盘弯曲 → 挡板靠近喷嘴\n"
            "      → 先导室压力↑ → 伺服放大 → 滑阀"
        )
        return ()

    anim = FuncAnimation(fig, frame, frames=n, interval=1000 / FPS, blit=False)
    save_anim(fig, anim, "01_压电陶瓷原理", fps=FPS)


# ============================================================
# 02 喷嘴挡板 → 先导压力（节流孔分流）
# ============================================================
def render_02_nozzle():
    fig, axes = plt.subplots(1, 2, figsize=(12.8, 7.2), facecolor=BG)
    ax, ax2 = axes
    for a in axes:
        a.set_facecolor(BG)
    fig.suptitle("FY301 研发仿真 · 喷嘴挡板先导级", color=FG, fontsize=16, fontweight="bold")

    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.axis("off")
    ax.set_title("剖面：节流孔 → 喷嘴 → 压电挡板 → 先导室", color=FG, fontsize=11)

    # static geometry
    # supply manifold
    ax.add_patch(FancyBboxPatch((0.4, 2.8), 1.4, 1.6, boxstyle="round,pad=0.05", facecolor="#1e293b", edgecolor=AIR, lw=2))
    ax.text(1.1, 4.6, "IN 供气", color=AIR, ha="center", fontsize=10)
    # restriction
    ax.add_patch(Rectangle((2.0, 3.4), 1.2, 0.35, facecolor="#334155", edgecolor=FG, lw=1.5))
    ax.text(2.6, 4.0, "节流孔 R", color=FG, ha="center", fontsize=9)
    # pilot chamber
    chamber = FancyBboxPatch((3.6, 2.2), 3.2, 2.8, boxstyle="round,pad=0.05", facecolor="#122033", edgecolor=ACCENT, lw=2)
    ax.add_patch(chamber)
    ax.text(5.2, 4.85, "先导室", color=ACCENT, ha="center", fontsize=10)
    # nozzle
    nozzle_body = Polygon([[4.9, 2.2], [5.5, 2.2], [5.35, 1.35], [5.05, 1.35]], closed=True, facecolor="#475569", edgecolor=AIR, lw=1.5)
    ax.add_patch(nozzle_body)
    ax.text(5.2, 0.95, "喷嘴", color=AIR, ha="center", fontsize=9)
    # exhaust
    ax.annotate("排气", xy=(5.2, 0.7), xytext=(6.5, 0.4), color="#94a3b8", arrowprops=dict(arrowstyle="->", color="#94a3b8"))

    # piezo disk (animated)
    (piezo_line,) = ax.plot([], [], color=PIEZO, lw=5)
    ax.text(7.5, 1.55, "压电盘挡板", color=PIEZO, fontsize=10)
    # pressure fill
    press_fill = FancyBboxPatch((3.7, 2.3), 3.0, 0.1, boxstyle="round,pad=0.02", facecolor=ACCENT, alpha=0.35, edgecolor="none")
    ax.add_patch(press_fill)
    p_txt = ax.text(5.2, 3.5, "", color=FG, ha="center", fontsize=12, fontweight="bold")
    state_txt = ax.text(5.2, 6.5, "", color=WARN, ha="center", fontsize=12)

    # particles
    n_part = 18
    parts = ax.scatter(np.zeros(n_part), np.zeros(n_part), c=AIR, s=28, alpha=0.85)

    # right: P vs V curve
    ax2.set_facecolor("#111827")
    ax2.set_title("FYCAL 标定关系（供气 20 psi）", color=FG, fontsize=11)
    ax2.set_xlabel("压电电压 V", color=FG)
    ax2.set_ylabel("先导压力 P (psi)", color=FG)
    ax2.tick_params(colors=FG)
    for sp in ax2.spines.values():
        sp.set_color("#334155")
    # calibration points
    ax2.scatter([0, 50, 100], [2, 6, 12.5], c=WARN, s=60, zorder=5)
    ax2.plot([0, 50, 100], [2, 6, 12.5], "--", color="#64748b", lw=1)
    ax2.set_xlim(-5, 105)
    ax2.set_ylim(0, 15)
    (dot,) = ax2.plot([0], [2], "o", color=OK, markersize=12)
    ax2.text(0, 2.6, "0V≤2", color=FG, fontsize=8, ha="center")
    ax2.text(50, 6.8, "50V≈6", color=FG, fontsize=8, ha="center")
    ax2.text(100, 13.2, "100V≈12–13", color=FG, fontsize=8, ha="center")
    ax2.grid(True, alpha=0.2, color=FG)

    n = 100

    def pilot_from_V(V):
        if V < 50:
            return 2 + (V / 50) * 4.0
        return 6 + ((V - 50) / 50) * 6.5

    def frame(k):
        t = k / n
        # sweep 0-100-0
        phase = math.sin(t * 2 * math.pi) * 0.5 + 0.5
        V = 100 * phase
        P = pilot_from_V(V)
        s = V / 100.0
        # disk position: y rises when voltage high (closes nozzle)
        xs = np.linspace(4.2, 7.8, 60)
        y0 = 1.05 - 0.35 * s  # closer to nozzle tip ~1.35 when high V → use lower y to approach
        # nozzle tip at y=1.35; disk above it
        y_center = 1.55 - 0.42 * s
        bend = y_center + 0.08 * s * (1 - ((xs - 6.0) / 1.8) ** 2)
        piezo_line.set_data(xs, bend)
        # pressure fill height
        h = 0.3 + 2.2 * (P / 13.0)
        press_fill.set_height(h)
        press_fill.set_facecolor(plt.cm.coolwarm(P / 13.0))
        p_txt.set_text(f"P_pilot ≈ {P:.1f} psi\nV = {V:.0f} V")
        if s > 0.6:
            state_txt.set_text("挡板靠近喷嘴 → 排气受阻 → 先导压升高")
        elif s < 0.3:
            state_txt.set_text("挡板远离喷嘴 → 气流排出 → 先导压降低")
        else:
            state_txt.set_text("过渡区：间隙调制压力分流比")

        # particles along path IN→R→chamber→nozzle or trapped
        rng = np.random.default_rng(k)
        xs_p = []
        ys_p = []
        for i in range(n_part):
            u = (i / n_part + t * (1.2 + 0.8 * (1 - s))) % 1.0
            if u < 0.25:
                xs_p.append(0.6 + u / 0.25 * 1.5)
                ys_p.append(3.55)
            elif u < 0.45:
                xs_p.append(2.1 + (u - 0.25) / 0.20 * 1.5)
                ys_p.append(3.55)
            elif u < 0.70:
                xs_p.append(4.0 + (u - 0.45) / 0.25 * 2.0)
                ys_p.append(3.2 + 0.3 * math.sin(10 * u + k * 0.2))
            else:
                # exit through nozzle if gap open
                if s < 0.55:
                    xs_p.append(5.2 + 0.1 * rng.normal())
                    ys_p.append(2.0 - (u - 0.70) / 0.30 * 1.4)
                else:
                    # trapped recirculate in chamber
                    xs_p.append(4.2 + 2.2 * ((u - 0.70) / 0.30))
                    ys_p.append(3.0 + 0.6 * math.sin(8 * u))
        parts.set_offsets(np.c_[xs_p, ys_p])
        col = plt.cm.plasma(0.2 + 0.7 * s)
        parts.set_color([col] * n_part)

        dot.set_data([V], [P])
        return ()

    anim = FuncAnimation(fig, frame, frames=n, interval=1000 / FPS, blit=False)
    save_anim(fig, anim, "02_喷嘴挡板先导级", fps=FPS)


# ============================================================
# 03 膜片放大 + 滑阀 OUT1/OUT2
# ============================================================
def render_03_servo_spool():
    fig = plt.figure(figsize=(12.8, 7.2), facecolor=BG)
    ax = fig.add_axes([0.05, 0.08, 0.58, 0.82], facecolor=BG)
    axp = fig.add_axes([0.66, 0.12, 0.30, 0.76], facecolor="#111827")
    fig.suptitle("FY301 研发仿真 · 膜片伺服放大 + 滑阀输出", color=FG, fontsize=16, fontweight="bold")

    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis("off")

    # large diaphragm (pilot)
    big = Ellipse((5, 6.2), 4.2, 0.55, facecolor="#1e3a5f", edgecolor=ACCENT, lw=2)
    ax.add_patch(big)
    ax.text(5, 6.85, "大膜片（先导室）A_large", color=ACCENT, ha="center", fontsize=10)
    # small diaphragm
    small = Ellipse((5, 3.6), 1.6, 0.4, facecolor="#3e2723", edgecolor=WARN, lw=2)
    ax.add_patch(small)
    ax.text(5, 4.15, "小膜片（滑阀室）A_small", color=WARN, ha="center", fontsize=9)
    # link
    (link,) = ax.plot([5, 5], [5.9, 3.8], color=FG, lw=3)
    # spool body
    sleeve = FancyBboxPatch((3.8, 0.6), 2.4, 2.4, boxstyle="round,pad=0.04", facecolor="#1e293b", edgecolor="#94a3b8", lw=2)
    ax.add_patch(sleeve)
    spool = FancyBboxPatch((4.15, 1.4), 1.7, 1.0, boxstyle="round,pad=0.02", facecolor="#78909c", edgecolor=FG, lw=1.5)
    ax.add_patch(spool)
    ax.text(2.2, 2.5, "IN", color=AIR, fontsize=11, fontweight="bold")
    ax.text(8.0, 2.8, "OUT1", color=OK, fontsize=11, fontweight="bold")
    ax.text(8.0, 1.4, "OUT2", color=WARN, fontsize=11, fontweight="bold")
    ax.annotate("", xy=(3.8, 2.2), xytext=(2.6, 2.2), arrowprops=dict(arrowstyle="->", color=AIR, lw=2))
    out1_arr = FancyArrowPatch((6.2, 2.6), (7.7, 2.8), arrowstyle="->", color=OK, mutation_scale=12, lw=2)
    out2_arr = FancyArrowPatch((6.2, 1.5), (7.7, 1.4), arrowstyle="->", color=WARN, mutation_scale=12, lw=2)
    ax.add_patch(out1_arr)
    ax.add_patch(out2_arr)
    force_txt = ax.text(5, 7.5, "", color=FG, ha="center", fontsize=11)
    mode_txt = ax.text(5, 0.25, "", color=FG, ha="center", fontsize=11)

    # failsafe note
    ax.text(
        0.2,
        7.7,
        "失电：OUT1→0，OUT2→供气压力（故障安全）",
        color="#f87171",
        fontsize=9,
        ha="left",
    )

    axp.set_title("力平衡 & 输出压力", color=FG, fontsize=11)
    axp.set_xlim(0, 1)
    axp.set_ylim(0, 1)
    axp.axis("off")
    info = axp.text(0.05, 0.95, "", color=FG, fontsize=10, va="top", linespacing=1.5)

    n = 100

    def frame(k):
        t = k / n
        # pilot pressure oscillates then failsafe pulse
        if t < 0.8:
            Pp = 2 + 10 * (0.5 + 0.5 * math.sin(t * 2 * math.pi * 1.5))
        else:
            Pp = 0.5  # power loss → low pilot
        # area ratio approx
        Ar = 6.0
        F_large = Pp * Ar
        # equilibrium spool position -1..1
        x = np.clip((Pp - 6.5) / 6.5, -1, 1)
        if t >= 0.8:
            x = -1  # failsafe
        y_big = 6.2 + 0.15 * x
        y_small = 3.6 + 0.15 * x
        big.center = (5, y_big)
        small.center = (5, y_small)
        link.set_data([5, 5], [y_big - 0.25, y_small + 0.2])
        spool.set_y(1.4 + 0.55 * x)

        # OUT pressures
        if t >= 0.8:
            P1, P2 = 0.0, 20.0
            mode = "故障安全：失电/低先导 → OUT1=0, OUT2=供气"
            out1_arr.set_color("#64748b")
            out2_arr.set_color(WARN)
        else:
            P1 = 10 + 10 * x
            P2 = 10 - 10 * x
            if x > 0.2:
                mode = "先导↑ → 滑阀上移 → OUT1 供气↑ / OUT2 排气"
                out1_arr.set_color(OK)
                out2_arr.set_color("#64748b")
            elif x < -0.2:
                mode = "先导↓ → 滑阀下移 → OUT1 排气 / OUT2 供气↑"
                out1_arr.set_color("#64748b")
                out2_arr.set_color(WARN)
            else:
                mode = "近平衡：滑阀中位，微小泄漏维持"
                out1_arr.set_color("#94a3b8")
                out2_arr.set_color("#94a3b8")

        force_txt.set_text(f"F_large = P_pilot x A_large ≈ {F_large:.1f} (相对)  |  A_large >> A_small → 力放大")
        mode_txt.set_text(mode)
        info.set_text(
            "伺服平衡方程\n"
            "────────────────\n"
            "P_pilot · A_large\n"
            "   ≈ P_spool · A_small\n"
            "────────────────\n"
            f"P_pilot   = {Pp:5.1f} psi\n"
            f"面积比 Ar  ≈ {Ar:.1f}\n"
            f"滑阀行程 x = {x:+.2f}\n"
            f"OUT1      = {P1:5.1f} psi\n"
            f"OUT2      = {P2:5.1f} psi\n"
            "────────────────\n"
            "双作用：OUT1⊥OUT2\n"
            "单作用：只用 OUT1，\n"
            "        堵塞 OUT2\n"
            "供气 1.4–7.0 bar\n"
            "输出能力 13.6 Nm³/h\n"
            "@5.6 bar"
        )
        return ()

    anim = FuncAnimation(fig, frame, frames=n, interval=1000 / FPS, blit=False)
    save_anim(fig, anim, "03_膜片放大与滑阀", fps=FPS)


# ============================================================
# 04 霍尔反馈 + 闭环
# ============================================================
def render_04_hall_loop():
    fig = plt.figure(figsize=(12.8, 7.2), facecolor=BG)
    ax = fig.add_axes([0.05, 0.45, 0.55, 0.48], facecolor=BG)
    axl = fig.add_axes([0.63, 0.45, 0.33, 0.48], facecolor="#111827")
    axb = fig.add_axes([0.08, 0.08, 0.84, 0.30], facecolor="#111827")
    fig.suptitle("FY301 研发仿真 · 霍尔非接触反馈 + 闭环定位", color=FG, fontsize=16, fontweight="bold")

    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    ax.axis("off")
    ax.set_title("霍尔传感器 与 阀杆磁铁（间隙 2-4 mm）", color=FG, fontsize=11)

    # sensor
    ax.add_patch(FancyBboxPatch((1.5, 1.8), 1.8, 1.4, boxstyle="round,pad=0.05", facecolor="#14532d", edgecolor=OK, lw=2))
    ax.text(2.4, 3.4, "Hall IC", color=OK, ha="center", fontsize=10)
    # magnet
    mag = FancyBboxPatch((5.5, 2.1), 1.2, 0.9, boxstyle="round,pad=0.04", facecolor="#7f1d1d", edgecolor=WARN, lw=2)
    ax.add_patch(mag)
    ax.text(6.1, 3.2, "磁铁", color=WARN, ha="center", fontsize=10)
    # stem
    (stem,) = ax.plot([6.1, 6.1], [0.4, 2.1], color="#94a3b8", lw=6)
    gap_line = ax.annotate("", xy=(3.3, 2.5), xytext=(5.5, 2.5), arrowprops=dict(arrowstyle="<->", color=ACCENT, lw=2))
    gap_txt = ax.text(4.4, 2.85, "2–4 mm", color=ACCENT, ha="center", fontsize=10)
    field_txt = ax.text(5, 4.5, "", color=FG, ha="center", fontsize=11)

    # block diagram
    axl.axis("off")
    axl.set_xlim(0, 1)
    axl.set_ylim(0, 1)
    boxes = [
        (0.1, 0.75, "SP 设定\n4–20mA"),
        (0.1, 0.45, "PID\nKP / TR"),
        (0.1, 0.15, "压电 V"),
        (0.55, 0.15, "执行器"),
        (0.55, 0.45, "阀位 PV"),
        (0.55, 0.75, "Hall"),
    ]
    for x, y, lab in boxes:
        axl.add_patch(FancyBboxPatch((x, y), 0.32, 0.18, boxstyle="round,pad=0.02", facecolor="#1e293b", edgecolor=ACCENT, lw=1.5))
        axl.text(x + 0.16, y + 0.09, lab, color=FG, ha="center", va="center", fontsize=8)
    # arrows
    for a, b in [((0.26, 0.75), (0.26, 0.63)), ((0.26, 0.45), (0.26, 0.33)), ((0.42, 0.24), (0.55, 0.24)), ((0.71, 0.33), (0.71, 0.45)), ((0.71, 0.63), (0.71, 0.75)), ((0.55, 0.84), (0.42, 0.84))]:
        axl.annotate("", xy=b, xytext=a, arrowprops=dict(arrowstyle="->", color=AIR, lw=1.5))
    axl.text(0.5, 0.02, "闭环：误差 e=SP−PV → 修正 V_piezo", color=FG, ha="center", fontsize=8)

    # time series
    axb.set_title("阶跃响应：SP / PV / V_piezo / 误差", color=FG, fontsize=10)
    axb.set_xlim(0, 1)
    axb.set_ylim(-0.2, 1.2)
    axb.tick_params(colors=FG)
    for sp in axb.spines.values():
        sp.set_color("#334155")
    (sp_l,) = axb.plot([], [], color=ACCENT, lw=2, label="SP")
    (pv_l,) = axb.plot([], [], color=OK, lw=2, label="PV")
    (v_l,) = axb.plot([], [], color=PIEZO, lw=1.5, label="V_piezo(归一)")
    (e_l,) = axb.plot([], [], color=WARN, lw=1.2, label="误差 e")
    axb.legend(loc="upper right", facecolor="#1e293b", edgecolor="#334155", labelcolor=FG, fontsize=8, ncol=4)
    axb.grid(True, alpha=0.2, color=FG)

    n = 120
    # precompute simple 2nd-order-ish plant + PI
    dt = 1 / n
    SP = np.zeros(n)
    SP[int(0.15 * n) :] = 0.7
    PV = np.zeros(n)
    Vp = np.zeros(n)
    integ = 0.0
    vel = 0.0
    for i in range(1, n):
        e = SP[i - 1] - PV[i - 1]
        integ += e * dt
        u = np.clip(2.2 * e + 0.9 * integ, 0, 1)
        Vp[i] = u
        # plant: piezo-pressure-actuator lag
        acc = 18 * (u - PV[i - 1]) - 6 * vel
        vel += acc * dt
        PV[i] = np.clip(PV[i - 1] + vel * dt, 0, 1)

    def frame(k):
        pos = PV[k]
        # magnet moves with valve
        mag.set_x(4.8 + 2.5 * pos)
        stem.set_data([4.8 + 2.5 * pos + 0.6, 4.8 + 2.5 * pos + 0.6], [0.4, 2.1])
        gap = 2 + 2 * abs(0.5 - pos)  # illustrative mm
        gap_txt.set_text(f"间隙 ≈ {gap:.1f} mm（安装目标 2–4 mm）")
        field_txt.set_text(f"B → V_hall  ∝ 位置   |   PV = {pos * 100:.1f}%   SP = {SP[k] * 100:.0f}%")

        tt = np.linspace(0, 1, k + 1)
        sp_l.set_data(tt, SP[: k + 1])
        pv_l.set_data(tt, PV[: k + 1])
        v_l.set_data(tt, Vp[: k + 1])
        e_l.set_data(tt, SP[: k + 1] - PV[: k + 1])
        return ()

    anim = FuncAnimation(fig, frame, frames=n, interval=1000 / FPS, blit=False)
    save_anim(fig, anim, "04_霍尔反馈与闭环", fps=FPS)


# ============================================================
# 05 全系统信号流
# ============================================================
def render_05_system():
    fig, ax = plt.subplots(figsize=(12.8, 7.2), facecolor=BG)
    ax.set_facecolor(BG)
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8)
    ax.axis("off")
    fig.suptitle("FY301 研发仿真 · 全系统电–气–机闭环", color=FG, fontsize=16, fontweight="bold")

    nodes = [
        (1, 6.5, "4–20mA\nHART", ACCENT),
        (3.5, 6.5, "A/D\nCPU", ACCENT),
        (6, 6.5, "D/A\n隔离驱动", ACCENT),
        (8.5, 6.5, "压电盘\n30–70V", PIEZO),
        (11, 6.5, "喷嘴\n挡板", AIR),
        (11, 4.2, "先导室\n压力", AIR),
        (8.5, 4.2, "大小\n膜片", WARN),
        (6, 4.2, "滑阀\nSpool", WARN),
        (3.5, 4.2, "OUT1/\nOUT2", OK),
        (1, 4.2, "执行器\n阀门", OK),
        (1, 1.8, "磁铁", OK),
        (3.5, 1.8, "Hall", OK),
        (6, 1.8, "位置 PV", ACCENT),
    ]
    rects = []
    for x, y, lab, c in nodes:
        r = FancyBboxPatch((x - 0.9, y - 0.55), 1.8, 1.1, boxstyle="round,pad=0.04", facecolor="#1e293b", edgecolor=c, lw=2)
        ax.add_patch(r)
        ax.text(x, y, lab, color=FG, ha="center", va="center", fontsize=9)
        rects.append((x, y, c))

    # forward path arrows
    fwd = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (11, 12)]
    # feedback to CPU
    fb = (12, 1)

    pulse = ax.scatter([], [], s=80, c=AIR, zorder=10)
    status = ax.text(7, 0.5, "", color=FG, ha="center", fontsize=12)
    ax.text(7, 7.6, "蓝/紫=电信号链路　橙=气路先导　绿=机械阀位反馈", color="#94a3b8", ha="center", fontsize=10)

    n = 100

    def frame(k):
        t = (k / n) * len(fwd)
        idx = int(t) % len(fwd)
        frac = t - int(t)
        i0, i1 = fwd[idx]
        x0, y0, c0 = rects[i0][0], rects[i0][1], rects[i0][2]
        x1, y1, c1 = rects[i1][0], rects[i1][1], rects[i1][2]
        x = x0 + (x1 - x0) * frac
        y = y0 + (y1 - y0) * frac
        # also show feedback particle half duty
        if (k // 20) % 2 == 0:
            xf0, yf0 = rects[fb[0]][0], rects[fb[0]][1]
            xf1, yf1 = rects[fb[1]][0], rects[fb[1]][1]
            # curved feedback via right then up — simplify linear via mid
            mid = (7, 2.8)
            u = (k % 20) / 20
            if u < 0.5:
                xx = xf0 + (mid[0] - xf0) * (u / 0.5)
                yy = yf0 + (mid[1] - yf0) * (u / 0.5)
            else:
                xx = mid[0] + (xf1 - mid[0]) * ((u - 0.5) / 0.5)
                yy = mid[1] + (yf1 - mid[1]) * ((u - 0.5) / 0.5)
            pulse.set_offsets([[x, y], [xx, yy]])
            pulse.set_color([c1, ACCENT])
        else:
            pulse.set_offsets([[x, y]])
            pulse.set_color([c1])

        stage = [
            "输入电流数字化",
            "CPU 计算偏差/PID",
            "高压驱动压电",
            "盘弯曲调制间隙",
            "先导压力建立",
            "膜片力放大",
            "滑阀分配气量",
            "OUT 驱动执行器",
            "阀门位移",
            "磁铁跟随",
            "Hall 读位置",
            "PV 回馈 CPU",
        ][idx]
        status.set_text(f"当前环节：{stage}")
        return ()

    # draw static arrows
    for i0, i1 in fwd:
        x0, y0, _ = rects[i0]
        x1, y1, c = rects[i1]
        ax.annotate("", xy=(x1 - 0.95 if x1 > x0 else x1, y1 if abs(y1 - y0) < 0.1 else (y1 + 0.55 * np.sign(y0 - y1))), xytext=(x0 + 0.95 if x1 > x0 else x0, y0 if abs(y1 - y0) < 0.1 else (y0 - 0.55 * np.sign(y0 - y1))), arrowprops=dict(arrowstyle="->", color="#475569", lw=1.2))
    ax.annotate("反馈", xy=(3.5, 6.0), xytext=(6, 1.8), color=ACCENT, fontsize=9, arrowprops=dict(arrowstyle="->", color=ACCENT, connectionstyle="arc3,rad=0.3", lw=1.5))

    anim = FuncAnimation(fig, frame, frames=n, interval=1000 / FPS, blit=False)
    save_anim(fig, anim, "05_全系统闭环信号流", fps=FPS)


def main():
    print("ffmpeg:", FF)
    print("out:", OUT)
    render_01_piezo()
    render_02_nozzle()
    render_03_servo_spool()
    render_04_hall_loop()
    render_05_system()
    print("ALL DONE")


if __name__ == "__main__":
    main()
