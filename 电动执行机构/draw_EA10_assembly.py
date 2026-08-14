# -*- coding: utf-8 -*-
"""
EA10 总成方案图 — 过蜗杆轴/输出轴的半剖（Step 3）
上半外形、下半剖视。单位 mm，DXF R2013。禁止改 Step 2 蜗杆几何。
"""
from __future__ import annotations

import math
from pathlib import Path

import ezdxf
from ezdxf import units, zoom
from ezdxf.enums import TextEntityAlignment

# ===================== 参数区（Step 2 冻结 + 本步仓位） =====================
M, Z1, Z2, Q = 2.5, 1, 70, 16.0
D1 = Q * M                 # 40
D2 = M * Z2                # 175
A = 0.5 * (D1 + D2)        # 107.5
R1, R2 = D1 / 2, D2 / 2    # 20, 87.5
WORM_TIP, WORM_ROOT = R1 + M, R1 - 1.2 * M
WHEEL_TIP, WHEEL_ROOT = R2 + M, R2 - 1.2 * M
WORM_THREAD = 72.0
HAMMER_DEG = 12.0

CASE_X0, CASE_X1 = -118.0, 78.0
CASE_Y0 = -A - 118.0       # -225.5
CASE_Y1 = 46.0
WALL = 12.0

CTRL_X0, CTRL_X1 = -78.0, 70.0
CTRL_Y0, CTRL_Y1 = 46.0, 150.0
TERM_X0, TERM_X1 = -198.0, -78.0
TERM_Y0, TERM_Y1 = 46.0, 138.0
SEAL_T = 8.0               # 双密封隔板厚度

MOTOR_XF0, MOTOR_XF1 = 78.0, 92.0
MOTOR_XB0, MOTOR_XB1 = 92.0, 268.0
MOTOR_FR = 82.5            # 法兰半径 ~165/2
MOTOR_BR = 78.0

HW_CX, HW_R = -208.0, 90.0
CLUTCH_X0, CLUTCH_X1 = -150.0, -118.0

F10_OD, F10_PCD, F10_SPIG, F10_THK = 125.0, 102.0, 70.0, 22.0
STEM_BORE = 20.0           # ISO 5210 F10 型 A 标准通孔；φ32 与 F10 冲突见说明
HOLLOW_OD = 48.0

TEXT_H, ARROW = 3.5, 2.5
OUT = Path(__file__).resolve().parent
DXF_DIR = OUT / "DXF"
# ========================================================================

LW_C, LW_F, LW_H = 50, 18, 13
WC = (0.0, -A)  # 蜗轮中心


def setup():
    doc = ezdxf.new("R2013", setup=True)
    doc.units = units.MM
    doc.header["$INSUNITS"] = 4
    doc.header["$MEASUREMENT"] = 1
    for name, color, lw, lt in [
        ("轮廓", 7, LW_C, "Continuous"),
        ("细实线", 7, LW_F, "Continuous"),
        ("中心线", 1, LW_F, "CENTER"),
        ("虚线", 8, LW_F, "DASHED"),
        ("剖面线", 8, LW_H, "Continuous"),
        ("标注", 3, LW_F, "Continuous"),
        ("文字", 7, LW_F, "Continuous"),
        ("密封", 5, LW_C, "Continuous"),
    ]:
        if name not in doc.layers:
            doc.layers.add(name, color=color, linetype=lt, lineweight=lw)
    if "CENTER" not in doc.linetypes:
        doc.linetypes.add("CENTER", pattern="A,.9,-.05,.09,-.05")
    if "DASHED" not in doc.linetypes:
        doc.linetypes.add("DASHED", pattern="A,.5,-.25")
    if "CN" not in doc.styles:
        doc.styles.add("CN", font="DroidSansFallbackFull.ttf")
    doc.styles.get("CN").dxf.font = "DroidSansFallbackFull.ttf"
    if "MECH" not in doc.dimstyles:
        ds = doc.dimstyles.new("MECH")
        ds.dxf.dimtxt = TEXT_H
        ds.dxf.dimasz = ARROW
    return doc


def txt(msp, s, h, xy, align=TextEntityAlignment.LEFT, layer="文字", rot=0):
    t = msp.add_text(str(s), height=h, dxfattribs={"layer": layer, "style": "CN", "rotation": rot})
    t.set_placement(xy, align=align)
    return t


def rect(msp, xa, ya, xb, yb, layer="轮廓", lw=LW_C):
    msp.add_line((xa, ya), (xb, ya), dxfattribs={"layer": layer, "lineweight": lw})
    msp.add_line((xb, ya), (xb, yb), dxfattribs={"layer": layer, "lineweight": lw})
    msp.add_line((xb, yb), (xa, yb), dxfattribs={"layer": layer, "lineweight": lw})
    msp.add_line((xa, yb), (xa, ya), dxfattribs={"layer": layer, "lineweight": lw})


def hatch_rect(msp, x0, y0, x1, y1, step=4.5, angle=45.0):
    """细剖面线，仅 y<=0（下半剖）。"""
    y0, y1 = min(y0, 0.0), min(y1, 0.0)
    if y1 <= y0:
        return
    x0, x1 = min(x0, x1), max(x0, x1)
    ang = math.radians(angle)
    dx, dy = math.cos(ang), math.sin(ang)
    nx, ny = -dy, dx
    corners = [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]
    projs = [c[0] * nx + c[1] * ny for c in corners]
    pmin, pmax = min(projs), max(projs)
    span = abs((x1 - x0) * dx) + abs((y1 - y0) * dy) + 80.0

    def clip(p1, p2):
        xmin, xmax, ymin, ymax = x0, x1, y0, y1
        ddx, ddy = p2[0] - p1[0], p2[1] - p1[1]
        t0, t1 = 0.0, 1.0
        for p, q in (
            (-ddx, p1[0] - xmin),
            (ddx, xmax - p1[0]),
            (-ddy, p1[1] - ymin),
            (ddy, ymax - p1[1]),
        ):
            if abs(p) < 1e-12:
                if q < 0:
                    return None
                continue
            r = q / p
            t0, t1 = (max(t0, r), t1) if p < 0 else (t0, min(t1, r))
            if t0 > t1:
                return None
        return (p1[0] + t0 * ddx, p1[1] + t0 * ddy), (p1[0] + t1 * ddx, p1[1] + t1 * ddy)

    p = pmin - step
    while p <= pmax + step:
        cx, cy = nx * p, ny * p
        a = (cx - dx * span, cy - dy * span)
        b = (cx + dx * span, cy + dy * span)
        c = clip(a, b)
        if c:
            msp.add_line(c[0], c[1], dxfattribs={"layer": "剖面线", "lineweight": LW_H})
        p += step


def hatch_annulus(msp, cx, cy, r_in, r_out, y_max=0.0, step=4.5):
    bbox = (cx - r_out, cy - r_out, cx + r_out, cy + r_out)
    ang = math.radians(45)
    dx, dy = math.cos(ang), math.sin(ang)
    span = 2.5 * r_out + 40
    n = 48
    p = -span
    while p <= span:
        x0 = cx + -dy * p - dx * span
        y0 = cy + dx * p - dy * span
        x1 = cx + -dy * p + dx * span
        y1 = cy + dx * p + dy * span
        pts = []
        for i in range(n + 1):
            t = i / n
            x = x0 + t * (x1 - x0)
            y = y0 + t * (y1 - y0)
            rr = (x - cx) ** 2 + (y - cy) ** 2
            ok = (r_in * r_in <= rr <= r_out * r_out) and y <= y_max
            if i == 0:
                pts.append((x, y, ok))
            else:
                pts.append((x, y, ok))
        run = None
        for i, (x, y, ok) in enumerate(pts):
            if ok and run is None:
                run = (x, y)
            if (not ok or i == len(pts) - 1) and run is not None:
                end = (x, y) if ok else (pts[i - 1][0], pts[i - 1][1])
                if abs(end[0] - run[0]) + abs(end[1] - run[1]) > 1.2:
                    msp.add_line(run, end, dxfattribs={"layer": "剖面线", "lineweight": LW_H})
                run = None
        p += step
        _ = bbox


def balloon(msp, x, y, bx, by, n):
    msp.add_line((x, y), (bx, by), dxfattribs={"layer": "标注", "lineweight": LW_F})
    msp.add_circle((bx, by), 4.5, dxfattribs={"layer": "轮廓", "lineweight": LW_C})
    txt(msp, n, 3.2, (bx, by), TextEntityAlignment.MIDDLE_CENTER)


def dim_h(msp, x0, x1, y, label):
    msp.add_line((x0, y), (x1, y), dxfattribs={"layer": "标注", "lineweight": LW_F})
    for x in (x0, x1):
        msp.add_line((x, y - 2.2), (x, y + 2.2), dxfattribs={"layer": "标注", "lineweight": LW_F})
    s = 3.0
    msp.add_line((x0, y), (x0 + s, y + 1.1), dxfattribs={"layer": "标注", "lineweight": LW_F})
    msp.add_line((x0, y), (x0 + s, y - 1.1), dxfattribs={"layer": "标注", "lineweight": LW_F})
    msp.add_line((x1, y), (x1 - s, y + 1.1), dxfattribs={"layer": "标注", "lineweight": LW_F})
    msp.add_line((x1, y), (x1 - s, y - 1.1), dxfattribs={"layer": "标注", "lineweight": LW_F})
    txt(msp, label, TEXT_H, ((x0 + x1) / 2, y + 2.4), TextEntityAlignment.BOTTOM_CENTER, layer="标注")


def dim_v(msp, x, y0, y1, label, side=-1):
    msp.add_line((x, y0), (x, y1), dxfattribs={"layer": "标注", "lineweight": LW_F})
    for y in (y0, y1):
        msp.add_line((x - 2.2, y), (x + 2.2, y), dxfattribs={"layer": "标注", "lineweight": LW_F})
    txt(
        msp,
        label,
        TEXT_H,
        (x + 6.5 * side, (y0 + y1) / 2),
        TextEntityAlignment.MIDDLE_CENTER,
        layer="标注",
        rot=90,
    )


def draw():
    doc = setup()
    msp = doc.modelspace()
    thick = {"layer": "轮廓", "lineweight": LW_C}
    thin = {"layer": "细实线", "lineweight": LW_F}
    dash = {"layer": "虚线", "lineweight": LW_F, "linetype": "DASHED"}
    cen = {"layer": "中心线", "lineweight": LW_F, "linetype": "CENTER"}
    seal = {"layer": "密封", "lineweight": LW_C}

    # 中心线：蜗杆轴、输出轴
    msp.add_line((-300, 0), (300, 0), dxfattribs=cen)
    msp.add_line((0, 175), (0, CASE_Y0 - 55), dxfattribs=cen)

    # ---- 齿轮箱壳体 ----
    rect(msp, CASE_X0, CASE_Y0, CASE_X1, CASE_Y1)
    # 内壁（下半可见）
    msp.add_line((CASE_X0 + WALL, min(0, CASE_Y1 - 8)), (CASE_X0 + WALL, CASE_Y0 + WALL), dxfattribs=thin)
    msp.add_line((CASE_X1 - WALL, min(0, CASE_Y1 - 8)), (CASE_X1 - WALL, CASE_Y0 + WALL), dxfattribs=thin)
    msp.add_line((CASE_X0 + WALL, CASE_Y0 + WALL), (CASE_X1 - WALL, CASE_Y0 + WALL), dxfattribs=thin)
    hatch_rect(msp, CASE_X0, CASE_Y0, CASE_X0 + WALL, 0, step=4.0)
    hatch_rect(msp, CASE_X1 - WALL, CASE_Y0, CASE_X1, 0, step=4.0)
    hatch_rect(msp, CASE_X0, CASE_Y0, CASE_X1, CASE_Y0 + WALL, step=4.0)

    # 油面
    oil_y = -A + 18
    msp.add_line((CASE_X0 + WALL + 2, oil_y), (CASE_X1 - WALL - 2, oil_y), dxfattribs=dash)
    txt(msp, "油面", 3.0, (CASE_X0 + WALL + 8, oil_y + 2), layer="文字")

    # ---- 蜗轮 ----
    cx, cy = WC
    msp.add_circle((cx, cy), WHEEL_TIP, dxfattribs=thick)
    msp.add_circle((cx, cy), R2, dxfattribs={**thin, "linetype": "CENTER"})
    msp.add_circle((cx, cy), WHEEL_ROOT, dxfattribs=thin)
    msp.add_circle((cx, cy), HOLLOW_OD / 2, dxfattribs=thick)
    hatch_annulus(msp, cx, cy, HOLLOW_OD / 2 + 1, WHEEL_ROOT, y_max=0.0, step=5.0)
    hatch_annulus(msp, cx, cy, WHEEL_ROOT, WHEEL_TIP, y_max=0.0, step=3.8)
    # 齿示意（下半）
    for k in range(8):
        ang = math.radians(-20 - k * 18)
        x0 = cx + WHEEL_ROOT * math.cos(ang)
        y0 = cy + WHEEL_ROOT * math.sin(ang)
        x1 = cx + WHEEL_TIP * math.cos(ang)
        y1 = cy + WHEEL_TIP * math.sin(ang)
        if y1 <= 2:
            msp.add_line((x0, y0), (x1, y1), dxfattribs=thin)

    # ---- 蜗杆（纵剖）----
    xt0, xt1 = -WORM_THREAD / 2, WORM_THREAD / 2
    msp.add_line((xt0, WORM_TIP), (xt1, WORM_TIP), dxfattribs=thick)
    msp.add_line((xt0, -WORM_TIP), (xt1, -WORM_TIP), dxfattribs=thick)
    msp.add_line((xt0, WORM_ROOT), (xt1, WORM_ROOT), dxfattribs=thin)
    msp.add_line((xt0, -WORM_ROOT), (xt1, -WORM_ROOT), dxfattribs=thin)
    msp.add_line((xt0, WORM_TIP), (xt0, -WORM_TIP), dxfattribs=thin)
    msp.add_line((xt1, WORM_TIP), (xt1, -WORM_TIP), dxfattribs=thin)
    hatch_rect(msp, xt0, -WORM_ROOT, xt1, 0, step=3.2)
    # 螺纹示意
    x = xt0 + 4
    while x < xt1 - 2:
        msp.add_line((x, WORM_TIP), (x + 5, WORM_ROOT), dxfattribs=thin)
        msp.add_line((x, -WORM_TIP), (x + 5, -WORM_ROOT), dxfattribs=thin)
        x += 7
    # 锤击间隙标注在啮合点
    msp.add_arc((0, -R1), 14, 240, 300, dxfattribs={"layer": "标注", "lineweight": LW_F})
    txt(msp, f"锤击 {HAMMER_DEG:.0f}°", 3.0, (22, -R1 - 18), layer="标注")

    # 蜗杆轴伸向电机 / 手轮
    msp.add_line((xt1, 8), (MOTOR_XF0, 8), dxfattribs=thick)
    msp.add_line((xt1, -8), (MOTOR_XF0, -8), dxfattribs=thick)
    hatch_rect(msp, xt1, -8, MOTOR_XF0, 0, step=3.0)
    msp.add_line((xt0, 8), (CLUTCH_X1, 8), dxfattribs=thick)
    msp.add_line((xt0, -8), (CLUTCH_X1, -8), dxfattribs=thick)
    hatch_rect(msp, CLUTCH_X1, -8, xt0, 0, step=3.0)

    # 轴承示意
    for xa in (-52.0, 48.0):
        rect(msp, xa - 7, -16, xa + 7, 16, layer="细实线", lw=LW_F)
        hatch_rect(msp, xa - 7, -16, xa + 7, 0, step=2.8)

    # 力矩垫圈（蜗杆左轴承外侧，承受轴向力）
    rect(msp, -68.0, -18, -60.0, 18, layer="轮廓", lw=LW_C)
    hatch_rect(msp, -68.0, -18, -60.0, 0, step=2.4)

    # ---- 空心输出轴 + 编码器 ----
    msp.add_line((-HOLLOW_OD / 2, 28), (-HOLLOW_OD / 2, CASE_Y0), dxfattribs=thick)
    msp.add_line((HOLLOW_OD / 2, 28), (HOLLOW_OD / 2, CASE_Y0), dxfattribs=thick)
    msp.add_line((-STEM_BORE / 2, 28), (-STEM_BORE / 2, CASE_Y0 - F10_THK - 8), dxfattribs=dash)
    msp.add_line((STEM_BORE / 2, 28), (STEM_BORE / 2, CASE_Y0 - F10_THK - 8), dxfattribs=dash)
    # 编码器盘（输出轴上端，控制仓下方、齿轮箱内）
    rect(msp, -22, 18, 22, 36)
    txt(msp, "ABS", 2.8, (0, 27), TextEntityAlignment.MIDDLE_CENTER)

    # ---- 手轮 + 离合器 ----
    rect(msp, CLUTCH_X0, -28, CLUTCH_X1, 28)
    hatch_rect(msp, CLUTCH_X0, -28, CLUTCH_X1, 0, step=3.5)
    msp.add_circle((HW_CX, 0), HW_R, dxfattribs=thick)
    msp.add_circle((HW_CX, 0), HW_R - 14, dxfattribs=thin)
    msp.add_line((HW_CX - HW_R, 0), (CLUTCH_X0, 0), dxfattribs=thick)
    # 轮辐
    for ang in (35, 90, 145, 215, 270, 325):
        r0, r1 = 18, HW_R - 14
        a = math.radians(ang)
        msp.add_line(
            (HW_CX + r0 * math.cos(a), r0 * math.sin(a)),
            (HW_CX + r1 * math.cos(a), r1 * math.sin(a)),
            dxfattribs=thin,
        )
    # 离合拨杆
    msp.add_line((CLUTCH_X0 + 8, 28), (CLUTCH_X0 + 8, 58), dxfattribs=thick)
    rect(msp, CLUTCH_X0 - 4, 58, CLUTCH_X0 + 20, 70)

    # ---- 电机（可拆法兰）----
    rect(msp, MOTOR_XF0, -MOTOR_FR, MOTOR_XF1, MOTOR_FR)
    rect(msp, MOTOR_XB0, -MOTOR_BR, MOTOR_XB1, MOTOR_BR)
    hatch_rect(msp, MOTOR_XF0, -MOTOR_FR, MOTOR_XF1, 0, step=4.0)
    hatch_rect(msp, MOTOR_XB0, -MOTOR_BR, MOTOR_XB1, 0, step=5.0)
    # 绕组示意
    rect(msp, MOTOR_XB0 + 18, -52, MOTOR_XB1 - 22, 52, layer="细实线", lw=LW_F)
    hatch_rect(msp, MOTOR_XB0 + 18, -52, MOTOR_XB1 - 22, 0, step=3.2)
    msp.add_circle((MOTOR_XB1 - 10, 0), 9, dxfattribs=thin)
    txt(msp, "0.55 kW", 3.2, ((MOTOR_XB0 + MOTOR_XB1) / 2, MOTOR_BR + 8), TextEntityAlignment.BOTTOM_CENTER)

    # ---- 控制仓（上半外形）----
    rect(msp, CTRL_X0, CTRL_Y0, CTRL_X1, CTRL_Y1)
    # 显示窗
    rect(msp, -28, CTRL_Y1 - 28, 28, CTRL_Y1 - 8, layer="细实线", lw=LW_F)
    txt(msp, "LCD", 3.0, (0, CTRL_Y1 - 18), TextEntityAlignment.MIDDLE_CENTER)
    # 磁耦合旋钮
    msp.add_circle((-50, CTRL_Y1 - 18), 8, dxfattribs=thin)
    msp.add_circle((50, CTRL_Y1 - 18), 8, dxfattribs=thin)
    # 电子板示意
    rect(msp, CTRL_X0 + 10, CTRL_Y0 + 10, CTRL_X1 - 10, CTRL_Y1 - 36, layer="细实线", lw=LW_F)
    txt(msp, "电子 / 加热器", 3.0, ((CTRL_X0 + CTRL_X1) / 2, CTRL_Y0 + 28), TextEntityAlignment.MIDDLE_CENTER)

    # ---- 端子舱 + 双密封隔板 ----
    rect(msp, TERM_X0, TERM_Y0, TERM_X1, TERM_Y1)
    # 隔板（密封环 2）
    rect(msp, TERM_X1 - SEAL_T, TERM_Y0, TERM_X1, TERM_Y1, layer="密封", lw=LW_C)
    # 端子盖（密封环 1）
    msp.add_line((TERM_X0, TERM_Y0), (TERM_X0, TERM_Y1), dxfattribs=seal)
    msp.add_line((TERM_X0 - 3, TERM_Y0 + 8), (TERM_X0 - 3, TERM_Y1 - 8), dxfattribs=seal)
    # 格兰
    rect(msp, TERM_X0 - 18, TERM_Y0 + 18, TERM_X0, TERM_Y0 + 32, layer="细实线", lw=LW_F)
    rect(msp, TERM_X0 - 18, TERM_Y0 + 48, TERM_X0, TERM_Y0 + 62, layer="细实线", lw=LW_F)
    txt(msp, "端子舱", 3.2, ((TERM_X0 + TERM_X1) / 2 - 4, (TERM_Y0 + TERM_Y1) / 2), TextEntityAlignment.MIDDLE_CENTER)
    # 密封环 3：控制仓 / 齿轮箱分型
    msp.add_line((CASE_X0, CTRL_Y0), (CASE_X1, CTRL_Y0), dxfattribs=seal)

    # ---- F10 推力底座 ----
    by0 = CASE_Y0
    by1 = CASE_Y0 - F10_THK
    rect(msp, -F10_OD / 2, by1, F10_OD / 2, by0)
    hatch_rect(msp, -F10_OD / 2, by1, F10_OD / 2, min(0, by0), step=3.5)
    # 止口
    rect(msp, -F10_SPIG / 2, by1 - 3, F10_SPIG / 2, by1, layer="细实线", lw=LW_F)
    # 螺栓孔
    for sgn in (-1, 1):
        msp.add_circle((sgn * F10_PCD / 2, (by0 + by1) / 2), 5.5, dxfattribs=thin)
    # 阀杆螺母
    rect(msp, -16, by1 + 2, 16, by0 - 2, layer="细实线", lw=LW_F)
    hatch_rect(msp, -16, by1 + 2, 16, min(0, by0 - 2), step=2.6)

    # ---- 球标 ----
    balloon(msp, (CTRL_X0 + CTRL_X1) / 2, CTRL_Y1, 95, 188, "1")
    balloon(msp, TERM_X1 - 4, TERM_Y1 - 10, -70, 188, "2")
    balloon(msp, (TERM_X0 + TERM_X1) / 2, TERM_Y1, -160, 188, "3")
    balloon(msp, MOTOR_XB1 - 20, MOTOR_BR, 250, 120, "4")
    balloon(msp, 10, WORM_TIP, 95, 70, "5")
    balloon(msp, -64, -18, -64, -78, "6")
    balloon(msp, WHEEL_TIP * 0.7, cy - 20, 130, cy - 20, "7")
    balloon(msp, 8, -R1 - 6, 55, -55, "8")
    balloon(msp, 22, 28, 95, 28, "9")
    balloon(msp, HW_CX, HW_R, HW_CX, 130, "10")
    balloon(msp, CASE_X0 + 6, -80, CASE_X0 - 36, -80, "11")
    balloon(msp, F10_OD / 2, by1 + 4, 95, by1 - 18, "12")
    balloon(msp, 0, by1 + 8, -95, by1 - 18, "13")

    # ---- 关键尺寸 ----
    dim_v(msp, 42, 0, -A, f"a={A:.1f}", side=1)
    dim_h(msp, HW_CX - HW_R, MOTOR_XB1, CASE_Y0 - 48, f"L={MOTOR_XB1 - (HW_CX - HW_R):.0f}")
    dim_v(msp, HW_CX - HW_R - 28, CASE_Y0 - F10_THK - 3, CTRL_Y1, f"H={CTRL_Y1 - (CASE_Y0 - F10_THK - 3):.0f}", side=-1)
    dim_h(msp, -F10_OD / 2, F10_OD / 2, CASE_Y0 - 72, f"F10 dia {F10_OD:.0f}")
    txt(msp, f"d1={D1:.0f}  d2={D2:.0f}  m={M}  z1={Z1}  z2={Z2}  q={Q:.0f}", 3.2, (0, 168), TextEntityAlignment.BOTTOM_CENTER)
    txt(msp, f"ISO 5210 F10  bore {STEM_BORE:.0f} (type A)  100 Nm", 3.2, (0, 160), TextEntityAlignment.BOTTOM_CENTER)

    # 标题
    txt(msp, "EA10 智能电动执行机构  总成半剖方案图", 6.0, (0, 210), TextEntityAlignment.BOTTOM_CENTER)
    txt(
        msp,
        "Step 3  比例 1:1  上半外形 / 下半剖视（蜗杆轴线以下）  三道密封环见件2及分型面  公差不在本步",
        3.2,
        (0, 200),
        TextEntityAlignment.BOTTOM_CENTER,
    )

    # 明细
    bom = [
        "1 控制仓（电子/显示/加热器）",
        "2 双密封隔板（端子舱|电子仓）",
        "3 端子舱（格兰可漏，水停本舱）",
        "4 可拆电机 0.55 kW 四极 S2",
        "5 蜗杆 m=2.5 z1=1 钢",
        "6 力矩传感垫圈（蜗杆轴向力）",
        "7 蜗轮 z2=70 锡青铜",
        "8 锤击齿侧间隙 12°",
        "9 绝对编码器（输出轴，失电保持）",
        "10 手轮及离合器（可挂锁）",
        "11 油浴齿轮箱",
        "12 可拆推力底座 ISO 5210 F10",
        "13 阀杆螺母 型A",
    ]
    bx, by = 310, 190
    txt(msp, "明细表", 4.0, (bx, by + 12), layer="文字")
    rect(msp, bx - 8, by - 12 * len(bom) - 8, bx + 168, by + 20, layer="细实线", lw=LW_F)
    for i, line in enumerate(bom):
        txt(msp, line, 3.0, (bx, by - i * 12))

    notes = [
        "说明：",
        "1. 三道密封必须各自成环：端子盖、隔板(件2)、控制仓/齿轮箱分型。",
        "2. 电机法兰、推力底座可拆；控制电子与阀同体（一体化）。",
        "3. 产品定义稿 φ32 通孔超出 F10 型A（标准 Φ20），Step 4 在 F10/F14 中二选一。",
        "4. 本图不定公差、粗糙度、轴承型号；Step 4 再拆蜗杆/轴承/离合器。",
    ]
    ny = CASE_Y0 - 95
    for i, line in enumerate(notes):
        txt(msp, line, 3.0, (HW_CX - HW_R, ny - i * 8))

    zoom.extents(msp)
    DXF_DIR.mkdir(parents=True, exist_ok=True)
    dxf_path = DXF_DIR / "EA10_总成半剖.dxf"
    doc.saveas(dxf_path)
    return dxf_path


def render_png(dxf_path: Path, png_path: Path):
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from ezdxf.addons.drawing import Frontend, RenderContext
    from ezdxf.addons.drawing.config import BackgroundPolicy, ColorPolicy, Configuration
    from ezdxf.addons.drawing.matplotlib import MatplotlibBackend
    from ezdxf.addons.drawing.properties import LayoutProperties

    plt.rcParams["font.sans-serif"] = ["WenQuanYi Micro Hei", "Droid Sans Fallback", "SimHei"]
    plt.rcParams["axes.unicode_minus"] = False
    from matplotlib import font_manager

    for fp in (
        "/usr/share/fonts/truetype/wqy/wqy-microhei.ttc",
        "/usr/share/fonts/truetype/droid/DroidSansFallbackFull.ttf",
    ):
        if Path(fp).exists():
            font_manager.fontManager.addfont(fp)
    doc = ezdxf.readfile(dxf_path)
    msp = doc.modelspace()
    fig = plt.figure(figsize=(16.5, 10.5), dpi=180)
    ax = fig.add_axes([0.01, 0.01, 0.98, 0.98])
    ctx = RenderContext(doc)
    cfg = Configuration.defaults().with_changes(
        lineweight_scaling=0.85,
        min_lineweight=0.18,
        color_policy=ColorPolicy.BLACK,
        background_policy=BackgroundPolicy.WHITE,
    )
    props = LayoutProperties.from_layout(msp)
    props.set_colors("#FFFFFF", "#000000")
    Frontend(ctx, MatplotlibBackend(ax), config=cfg).draw_layout(
        msp, finalize=True, layout_properties=props
    )
    ax.set_aspect("equal")
    fig.savefig(png_path, dpi=180, facecolor="white", bbox_inches="tight", pad_inches=0.12)
    plt.close(fig)


def main():
    dxf = draw()
    png = OUT / "EA10_总成半剖.png"
    render_png(dxf, png)
    print("OK", dxf, png, png.stat().st_size)


if __name__ == "__main__":
    main()
