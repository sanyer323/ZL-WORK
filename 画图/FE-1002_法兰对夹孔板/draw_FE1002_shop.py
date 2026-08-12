# -*- coding: utf-8 -*-
"""
FE-1002 法兰对夹孔板 — 生产机加 / 装配图（ezdxf）
依据计算书 FE-1002.RO + HG/T20592 PN25 + GB/T2624 / ISO5167-2 法兰取压

图纸内容（模型空间分块，CAD 直接下车间）：
  A 总装配半剖 + 明细 + 技术要求
  B 孔板片机加工图（主视 + 剖视）
  C 取压法兰机加工图（主视半剖 + 密封面视）
  D 取压管机加工图
"""
from __future__ import annotations

import math
from pathlib import Path

import ezdxf
from ezdxf import units, zoom
from ezdxf.enums import TextEntityAlignment

# ===================== 参数区【改尺寸只改这里】 =====================
TAG = "FE-1002"
SERIAL = "26031402"
MODEL = "ROH10×JX25N2"
FLUID = "LNG / LIQUID"
TF_C = -162.0
PF_KPAG = 600.0

DN = 250
PIPE_OD = 273.0
PIPE_WALL = 4.0
METER_ID = 265.0          # D，计算书
BORE_D = 136.18           # d，计算书（20℃）
BETA = 0.5139

# 孔板片（机加）
PLATE_OD = 320.0          # 外径，落于 RF φ335 内、避开螺栓
PLATE_E = 8.0             # 板厚 E（0.005D~0.05D）
PLATE_E_EDGE = 3.0        # 孔口圆柱段厚度 e
BEVEL_DEG = 45.0          # 下游侧倒角
HANDLE_W = 40.0
HANDLE_L = 55.0
HANDLE_T = 8.0
SURF_UP = "Ra1.6"         # 上游面
SURF_BORE = "Ra0.8"       # 孔口

# HG/T20592-2009 PN25 DN250 带颈对焊 RF（系列Ⅰ A=273）
FL_OD = 425.0
FL_PCD = 370.0
FL_HOLE = 30.0
FL_N_BOLT = 12
FL_BOLT = "M27"
FL_C = 32.0               # 法兰厚度 C
FL_RF = 335.0             # 密封面直径
FL_RF_H = 2.0             # 突面高 f
FL_NECK = 298.0           # 颈部外径 N
FL_H = 88.0               # 法兰总高 H
FL_HUB_R = 12.0

# 垫片 / 螺柱
GASKET_OD = 335.0
GASKET_ID = 274.0
GASKET_T = 2.0
STUD = "M27×L≈180"
NUT = "M27"

# 法兰取压（ISO5167-2 / GB/T2624.2）：距孔板端面 25.4±0.8
TAP_OFFSET = 25.4
TAP_TOL = 0.8
TAP_HOLE = 8.0            # 取压孔孔径（<0.13D 且 ≤13）
TAP_PIPE_OD = 21.3        # 1/2" 管外径
TAP_PIPE_WALL = 2.0       # 壁厚（304L 薄壁常用）
TAP_PIPE_L = 90.0         # 取压管伸出长度
TAP_NPS = "DN15(1/2\")"

# 短节（焊端，供法兰对接；非计量直管段）
STUB_L = 100.0

MAT_FL = "F304/F304L"
MAT_PL = "F304/F304L"
MAT_TAP = "F304/F304L"
MAT_STUB = "F304/F304L"
MAT_GST = "缠绕垫 内环304 填料柔性石墨（深冷）"
MAT_FAST = "螺栓螺母 B8M/B8M（或按深冷紧固件规定）"

TEXT_H = 3.5
ARROW = 2.5
OUT_DIR = Path(__file__).resolve().parent
DXF_DIR = OUT_DIR / "DXF"
PNG_DIR = OUT_DIR / "结构图PNG"
# ========================================================================

LW_C = 50
LW_F = 18
LW_H = 13


def _setup_doc():
    doc = ezdxf.new("R2013", setup=True)
    doc.units = units.MM
    doc.header["$INSUNITS"] = 4
    doc.header["$MEASUREMENT"] = 1
    for name, color, lw, lt in [
        ("轮廓", 7, LW_C, "Continuous"),
        ("细实线", 7, LW_F, "Continuous"),
        ("中心线", 1, LW_F, "CENTER"),
        ("虚线", 7, LW_F, "DASHED"),
        ("剖面线", 7, LW_H, "Continuous"),
        ("标注", 3, LW_F, "Continuous"),
        ("文字", 7, LW_F, "Continuous"),
        ("表格", 7, LW_F, "Continuous"),
    ]:
        if name not in doc.layers:
            doc.layers.add(name, color=color, linetype=lt, lineweight=lw)
    if "CENTER" not in doc.linetypes:
        doc.linetypes.add("CENTER", pattern="A,.9,-.05,.09,-.05")
    if "DASHED" not in doc.linetypes:
        doc.linetypes.add("DASHED", pattern="A,.5,-.25")
    if "CN" not in doc.styles:
        doc.styles.add("CN", font="simhei.ttf")
    else:
        doc.styles.get("CN").dxf.font = "simhei.ttf"
    doc.styles.get("Standard").dxf.font = "simhei.ttf"
    if "MECH" not in doc.dimstyles:
        ds = doc.dimstyles.new("MECH")
        ds.dxf.dimtxt = TEXT_H
        ds.dxf.dimasz = ARROW
        ds.dxf.dimexe = 1.5
        ds.dxf.dimexo = 1.0
        ds.dxf.dimgap = 1.0
    return doc


def _hatch_lines(msp, x0, y0, x1, y1, step=4.0, angle_deg=45.0):
    y0 = min(y0, 0.0)
    y1 = min(y1, 0.0)
    if y1 <= y0:
        return
    ang = math.radians(angle_deg)
    dx, dy = math.cos(ang), math.sin(ang)
    nx, ny = -dy, dx
    corners = [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]
    projs = [c[0] * nx + c[1] * ny for c in corners]
    pmin, pmax = min(projs), max(projs)
    t_span = abs((x1 - x0) * dx) + abs((y1 - y0) * dy) + 80.0

    def clip_seg(p1, p2):
        x_min, x_max = min(x0, x1), max(x0, x1)
        y_min, y_max = min(y0, y1), max(y0, y1)
        dxs, dys = p2[0] - p1[0], p2[1] - p1[1]
        t0, t1 = 0.0, 1.0
        for p, q in (
            (-dxs, p1[0] - x_min),
            (dxs, x_max - p1[0]),
            (-dys, p1[1] - y_min),
            (dys, y_max - p1[1]),
        ):
            if abs(p) < 1e-12:
                if q < 0:
                    return None
                continue
            r = q / p
            if p < 0:
                t0 = max(t0, r)
            else:
                t1 = min(t1, r)
            if t0 > t1:
                return None
        return (p1[0] + t0 * dxs, p1[1] + t0 * dys), (p1[0] + t1 * dxs, p1[1] + t1 * dys)

    p = pmin - step
    while p <= pmax + step:
        cx, cy = nx * p, ny * p
        a = (cx - dx * t_span, cy - dy * t_span)
        b = (cx + dx * t_span, cy + dy * t_span)
        clipped = clip_seg(a, b)
        if clipped:
            msp.add_line(clipped[0], clipped[1], dxfattribs={"layer": "剖面线", "lineweight": LW_H})
        p += step


def _txt(msp, s, h, xy, align=TextEntityAlignment.LEFT, layer="文字", rot=0):
    t = msp.add_text(s, height=h, dxfattribs={"layer": layer, "style": "CN", "rotation": rot})
    t.set_placement(xy, align=align)
    return t


def _balloon(msp, x, y, bx, by, txt, r=5.0):
    msp.add_line((x, y), (bx, by), dxfattribs={"layer": "标注", "lineweight": LW_F})
    msp.add_circle((bx, by), r, dxfattribs={"layer": "轮廓", "lineweight": LW_C})
    _txt(msp, str(txt), 3.5, (bx, by), TextEntityAlignment.MIDDLE_CENTER)


def _arrow_h(msp, tip_x, y, direction):
    s = 3.0
    msp.add_line((tip_x, y), (tip_x - direction * s, y + 1.1), dxfattribs={"layer": "标注", "lineweight": LW_F})
    msp.add_line((tip_x, y), (tip_x - direction * s, y - 1.1), dxfattribs={"layer": "标注", "lineweight": LW_F})


def _dim_h(msp, x0, x1, y, label):
    msp.add_line((x0, y), (x1, y), dxfattribs={"layer": "标注", "lineweight": LW_F})
    for x in (x0, x1):
        msp.add_line((x, y - 2), (x, y + 2), dxfattribs={"layer": "标注", "lineweight": LW_F})
    _arrow_h(msp, x0, y, -1)
    _arrow_h(msp, x1, y, +1)
    _txt(msp, label, TEXT_H, ((x0 + x1) / 2, y + 2.5), TextEntityAlignment.BOTTOM_CENTER)


def _dim_v(msp, x, y0, y1, label, side=-1):
    msp.add_line((x, y0), (x, y1), dxfattribs={"layer": "标注", "lineweight": LW_F})
    for y in (y0, y1):
        msp.add_line((x - 2, y), (x + 2, y), dxfattribs={"layer": "标注", "lineweight": LW_F})
    s = 3.0
    msp.add_line((x, y0), (x - 1.1, y0 + s), dxfattribs={"layer": "标注", "lineweight": LW_F})
    msp.add_line((x, y0), (x + 1.1, y0 + s), dxfattribs={"layer": "标注", "lineweight": LW_F})
    msp.add_line((x, y1), (x - 1.1, y1 - s), dxfattribs={"layer": "标注", "lineweight": LW_F})
    msp.add_line((x, y1), (x + 1.1, y1 - s), dxfattribs={"layer": "标注", "lineweight": LW_F})
    _txt(msp, label, TEXT_H, (x + 6.0 * side, (y0 + y1) / 2), TextEntityAlignment.MIDDLE_CENTER, rot=90)


def _rect(msp, xa, ya, xb, yb, attr):
    msp.add_line((xa, ya), (xb, ya), dxfattribs=attr)
    msp.add_line((xb, ya), (xb, yb), dxfattribs=attr)
    msp.add_line((xb, yb), (xa, yb), dxfattribs=attr)
    msp.add_line((xa, yb), (xa, ya), dxfattribs=attr)


def _frame(msp, x0, y0, x1, y1, title):
    attr = {"layer": "表格", "lineweight": LW_F}
    _rect(msp, x0, y0, x1, y1, attr)
    _txt(msp, title, 5.0, ((x0 + x1) / 2, y1 - 8), TextEntityAlignment.TOP_CENTER)


# ---------- A 总装配 ----------
def draw_assembly(msp, ox, oy):
    thick = {"layer": "轮廓", "lineweight": LW_C}
    thin = {"layer": "细实线", "lineweight": LW_F}
    dash = {"layer": "虚线", "lineweight": LW_F, "linetype": "DASHED"}
    cen = {"layer": "中心线", "lineweight": LW_F, "linetype": "CENTER"}

    pipe_od, pipe_id = PIPE_OD, METER_ID
    fl, tf, tof = FL_OD, FL_H, FL_C  # 装配示意用总高/板侧厚度
    # 布局：短节-法兰颈-法兰盘-垫-孔板-垫-法兰盘-法兰颈-短节
    # 简化：法兰按厚度 C 画盘 + 颈段
    stub = STUB_L
    neck = FL_H - FL_C
    g = GASKET_T
    H = PLATE_E

    x0 = ox
    x_s1r = x0 + stub
    x_neck1 = x_s1r
    x_fl1 = x_neck1 + neck
    x_g1 = x_fl1 + FL_C
    x_pl = x_g1 + g
    x_g2 = x_pl + H
    x_fl2 = x_g2 + g
    x_neck2 = x_fl2 + FL_C
    x_s2l = x_neck2 + neck
    x_end = x_s2l + stub

    def shift(x, y):
        return (x, y + oy)

    # 中心线
    msp.add_line(shift(x0 - 30, 0), shift(x_end + 30, 0), dxfattribs=cen)

    def pipe(xa, xb):
        msp.add_line(shift(xa, pipe_od / 2), shift(xb, pipe_od / 2), dxfattribs=thick)
        msp.add_line(shift(xa, -pipe_od / 2), shift(xb, -pipe_od / 2), dxfattribs=thick)
        msp.add_line(shift(xa, pipe_id / 2), shift(xb, pipe_id / 2), dxfattribs=dash)
        msp.add_line(shift(xa, -pipe_id / 2), shift(xb, -pipe_id / 2), dxfattribs=dash)
        _hatch_lines(msp, xa, oy - pipe_od / 2, xb, oy - pipe_id / 2, step=4.0)

    pipe(x0, x_s1r)
    pipe(x_s2l, x_end)

    def flange_disk(xa, facing=+1):
        """facing=+1 密封面朝右；-1 朝左"""
        xb = xa + FL_C
        _rect(msp, *shift(xa, fl / 2), *shift(xb, -fl / 2), thick)
        # 内孔
        msp.add_line(shift(xa, pipe_id / 2), shift(xb, pipe_id / 2), dxfattribs=thin)
        msp.add_line(shift(xa, -pipe_id / 2), shift(xb, -pipe_id / 2), dxfattribs=thin)
        # RF
        rf_x = xb if facing > 0 else xa
        rf_in = xb - FL_RF_H if facing > 0 else xa + FL_RF_H
        msp.add_line(shift(rf_in, FL_RF / 2), shift(rf_x, FL_RF / 2), dxfattribs=thin)
        msp.add_line(shift(rf_in, -FL_RF / 2), shift(rf_x, -FL_RF / 2), dxfattribs=thin)
        # 螺栓孔示意
        msp.add_circle(shift((xa + xb) / 2, FL_PCD / 2 * 0.92), FL_HOLE / 4, dxfattribs=thin)
        msp.add_circle(shift((xa + xb) / 2, -FL_PCD / 2 * 0.92), FL_HOLE / 4, dxfattribs=dash)
        _hatch_lines(msp, xa, oy - fl / 2, xb, oy - pipe_id / 2, step=6.0)
        # 颈部
        if facing > 0:
            n0, n1 = xa - neck, xa
        else:
            n0, n1 = xb, xb + neck
        msp.add_line(shift(n0, FL_NECK / 2), shift(n1, FL_NECK / 2), dxfattribs=thick)
        msp.add_line(shift(n0, -FL_NECK / 2), shift(n1, -FL_NECK / 2), dxfattribs=thick)
        msp.add_line(shift(n0, pipe_id / 2), shift(n1, pipe_id / 2), dxfattribs=dash)
        msp.add_line(shift(n0, -pipe_id / 2), shift(n1, -pipe_id / 2), dxfattribs=dash)
        _hatch_lines(msp, n0, oy - FL_NECK / 2, n1, oy - pipe_id / 2, step=5.0)

    flange_disk(x_fl1, facing=+1)
    flange_disk(x_fl2, facing=-1)

    # 垫片
    for xa in (x_g1, x_g2):
        _rect(msp, *shift(xa, GASKET_OD / 2), *shift(xa + g, -GASKET_OD / 2), thin)

    # 孔板
    pod = PLATE_OD
    br = BORE_D / 2
    e = PLATE_E_EDGE
    bevel = PLATE_E - e
    _rect(msp, *shift(x_pl, pod / 2), *shift(x_pl + H, -pod / 2), thick)
    _hatch_lines(msp, x_pl, oy - pod / 2, x_pl + H, oy, step=4.0)
    # 孔口：上游直孔 + 下游 45°
    msp.add_line(shift(x_pl, br), shift(x_pl + e, br), dxfattribs=thick)
    msp.add_line(shift(x_pl, -br), shift(x_pl + e, -br), dxfattribs=thick)
    msp.add_line(shift(x_pl + e, br), shift(x_pl + H, br + bevel), dxfattribs=thick)
    msp.add_line(shift(x_pl + e, -br), shift(x_pl + H, -br - bevel), dxfattribs=thick)
    msp.add_line(shift(x_pl + H, br + bevel), shift(x_pl + H, -br - bevel), dxfattribs=thick)
    msp.add_line(shift(x_pl, br), shift(x_pl, -br), dxfattribs=thick)

    # 手柄
    hx = x_pl + H / 2
    msp.add_line(shift(hx, pod / 2), shift(hx, pod / 2 + 28), dxfattribs=thick)
    _rect(msp, *shift(hx - HANDLE_W / 2, pod / 2 + 28), *shift(hx + HANDLE_W / 2, pod / 2 + 28 + HANDLE_L * 0.55), thick)
    _txt(msp, "3", 4.0, shift(hx, pod / 2 + 28 + HANDLE_L * 0.28), TextEntityAlignment.MIDDLE_CENTER)

    # 取压管（上下游各一根，画在法兰外圆上方）
    def tap(fl_face_x, facing):
        # 取压孔轴线距孔板面 25.4 → 距密封面约 25.4 - g
        axis_from_plate = TAP_OFFSET
        if facing > 0:
            # 上游法兰：密封面在 x_g1，孔板上游面在 x_pl；轴线在孔板左侧 axis_from_plate
            ax = x_pl - axis_from_plate
        else:
            ax = x_pl + H + axis_from_plate
        y0 = fl / 2
        y1 = fl / 2 + TAP_PIPE_L
        msp.add_line(shift(ax - TAP_PIPE_OD / 2, y0), shift(ax - TAP_PIPE_OD / 2, y1), dxfattribs=thick)
        msp.add_line(shift(ax + TAP_PIPE_OD / 2, y0), shift(ax + TAP_PIPE_OD / 2, y1), dxfattribs=thick)
        msp.add_line(shift(ax - TAP_PIPE_OD / 2, y1), shift(ax + TAP_PIPE_OD / 2, y1), dxfattribs=thick)
        # 取压孔到内壁虚线
        msp.add_line(shift(ax, y0), shift(ax, pipe_id / 2), dxfattribs=dash)
        return ax, y1

    ax1, ty1 = tap(x_g1, +1)
    ax2, ty2 = tap(x_g2, -1)

    # 螺柱
    def stud(y):
        xa, xb = x_fl1 + 4, x_fl2 + FL_C - 4
        msp.add_line(shift(xa, y), shift(xb, y), dxfattribs=thick)
        for xx in (xa, xb):
            _rect(msp, *shift(xx - 4, y + 5), *shift(xx + 4, y - 5), thick)

    stud(FL_PCD / 2 * 0.88)
    stud(-FL_PCD / 2 * 0.88)

    # 球标
    _balloon(msp, *shift(x_fl1 + FL_C / 2, -fl / 2), *shift(x_fl1 + FL_C / 2 - 10, -fl / 2 - 30), "1")
    _balloon(msp, *shift(x_fl2 + FL_C / 2, -fl / 2), *shift(x_fl2 + FL_C / 2 + 10, -fl / 2 - 30), "2")
    _balloon(msp, *shift(x_pl + H / 2, -pod / 2), *shift(x_pl + H / 2, -fl / 2 - 30), "3")
    _balloon(msp, *shift(ax1, ty1), *shift(ax1 - 25, ty1 + 18), "4")
    _balloon(msp, *shift(ax2, ty2), *shift(ax2 + 25, ty2 + 18), "5")
    _balloon(msp, *shift((x_fl1 + x_fl2 + FL_C) / 2, FL_PCD / 2 * 0.88), *shift((x_fl1 + x_fl2 + FL_C) / 2, fl / 2 + 55), "6")
    _balloon(msp, *shift(x_g1 + g / 2, GASKET_OD / 2), *shift(x_g1 - 20, fl / 2 + 35), "7")
    _balloon(msp, *shift(x0 + stub / 2, pipe_od / 2), *shift(x0 + stub / 2, fl / 2 + 35), "8")

    # 尺寸
    _dim_h(msp, x_fl1, x_fl2 + FL_C, oy - fl / 2 - 52, f"装配长 ≈{int(x_fl2 + FL_C - x_fl1)}")
    _dim_v(msp, x0 - 22, oy - fl / 2, oy + fl / 2, f"Φ{int(FL_OD)}", side=-1)
    _txt(msp, f"Φ{PIPE_OD}×{PIPE_WALL}", TEXT_H, shift((x0 + x_s1r) / 2, pipe_od / 2 + 10), TextEntityAlignment.BOTTOM_CENTER)
    _txt(msp, f"Φ{BORE_D}", TEXT_H, shift(x_pl + H + 16, 0), TextEntityAlignment.MIDDLE_LEFT)
    _txt(msp, f"取压 {TAP_OFFSET}±{TAP_TOL}", 3.0, shift((ax1 + ax2) / 2, fl / 2 + 72), TextEntityAlignment.BOTTOM_CENTER)

    # 流向
    yf = oy - fl / 2 - 72
    msp.add_line((x_fl1 + 20, yf), (x_fl2 + FL_C - 25, yf), dxfattribs=thick)
    msp.add_line((x_fl2 + FL_C - 25, yf), (x_fl2 + FL_C - 36, yf + 4), dxfattribs=thick)
    msp.add_line((x_fl2 + FL_C - 25, yf), (x_fl2 + FL_C - 36, yf - 4), dxfattribs=thick)
    _txt(msp, "介质流向 →（下游侧倒角）", 4.0, ((x_fl1 + x_fl2 + FL_C) / 2, yf - 8), TextEntityAlignment.TOP_CENTER)

    _txt(
        msp,
        f"{TAG} 法兰对夹孔板总装  DN{DN}  HG/T20592 PN25 RF  {MODEL}",
        5.5,
        shift((x0 + x_end) / 2, fl / 2 + 95),
        TextEntityAlignment.BOTTOM_CENTER,
    )
    _txt(
        msp,
        f"D={METER_ID}  d={BORE_D}  β={BETA}  材质{MAT_PL}  Tf={TF_C}℃  Pf={PF_KPAG}kPaG",
        3.8,
        shift((x0 + x_end) / 2, fl / 2 + 82),
        TextEntityAlignment.BOTTOM_CENTER,
    )
    return x0 - 40, oy - fl / 2 - 95, x_end + 40, oy + fl / 2 + 110


# ---------- B 孔板片机加 ----------
def draw_plate(msp, ox, oy):
    thick = {"layer": "轮廓", "lineweight": LW_C}
    thin = {"layer": "细实线", "lineweight": LW_F}
    cen = {"layer": "中心线", "lineweight": LW_F, "linetype": "CENTER"}

    # 主视（上游面看）
    cx, cy = ox + 90, oy + 20
    R = PLATE_OD / 2
    r = BORE_D / 2
    msp.add_circle((cx, cy), R, dxfattribs=thick)
    msp.add_circle((cx, cy), r, dxfattribs=thick)
    msp.add_line((cx - R - 18, cy), (cx + R + 18, cy), dxfattribs=cen)
    msp.add_line((cx, cy - R - 18), (cx, cy + R + HANDLE_L + 10), dxfattribs=cen)
    # 手柄
    hw, hl = HANDLE_W / 2, HANDLE_L
    _rect(msp, cx - hw, cy + R, cx + hw, cy + R + hl, thick)
    _txt(msp, f"{TAG}", 3.2, (cx, cy + R + hl * 0.55), TextEntityAlignment.MIDDLE_CENTER)
    _txt(msp, "UPSTREAM", 2.8, (cx, cy + R + hl * 0.25), TextEntityAlignment.MIDDLE_CENTER)
    # 流向箭头刻印示意
    msp.add_line((cx + r + 15, cy - 25), (cx + r + 45, cy - 25), dxfattribs=thin)
    msp.add_line((cx + r + 45, cy - 25), (cx + r + 38, cy - 21), dxfattribs=thin)
    msp.add_line((cx + r + 45, cy - 25), (cx + r + 38, cy - 29), dxfattribs=thin)
    _txt(msp, "流向刻印", 2.8, (cx + r + 30, cy - 32), TextEntityAlignment.TOP_CENTER)

    _dim_h(msp, cx - R, cx + R, cy - R - 28, f"Φ{PLATE_OD}")
    _dim_h(msp, cx - r, cx + r, cy + 12, f"Φ{BORE_D}±0.05")
    _dim_v(msp, cx + R + 22, cy + R, cy + R + hl, f"{HANDLE_L}", side=1)
    _dim_h(msp, cx - hw, cx + hw, cy + R + hl + 8, f"{HANDLE_W}")

    _txt(msp, "孔板片 主视（上游面）", 4.0, (cx, cy + R + hl + 28), TextEntityAlignment.BOTTOM_CENTER)
    _txt(msp, f"上游面 {SURF_UP}  孔口 {SURF_BORE}  锐边无倒圆", 3.0, (cx, cy - R - 45), TextEntityAlignment.TOP_CENTER)

    # 剖视 A-A（侧视放大）
    px = ox + 280
    py = oy + 20
    scale = 1.0
    E, e = PLATE_E * scale, PLATE_E_EDGE * scale
    br = BORE_D / 2 * scale
    pod = PLATE_OD / 2 * scale
    bevel = (PLATE_E - PLATE_E_EDGE) * scale

    # 外形
    _rect(msp, px, py - pod, px + E, py + pod, thick)
    # 孔口轮廓（上半）
    msp.add_line((px, py + br), (px + e, py + br), dxfattribs=thick)
    msp.add_line((px + e, py + br), (px + E, py + br + bevel), dxfattribs=thick)
    msp.add_line((px, py - br), (px + e, py - br), dxfattribs=thick)
    msp.add_line((px + e, py - br), (px + E, py - br - bevel), dxfattribs=thick)
    msp.add_line((px, py + br), (px, py - br), dxfattribs=thick)
    msp.add_line((px + E, py + br + bevel), (px + E, py - br - bevel), dxfattribs=thick)
    _hatch_lines(msp, px, py - pod, px + E, py, step=3.5)
    msp.add_line((px - 15, py), (px + E + 15, py), dxfattribs=cen)

    _dim_h(msp, px, px + E, py - pod - 22, f"E={PLATE_E}")
    _dim_h(msp, px, px + e, py + br + bevel + 18, f"e={PLATE_E_EDGE}")
    _txt(msp, f"{BEVEL_DEG}°", 3.2, (px + e + bevel * 0.55, py + br + bevel * 0.55 + 8), TextEntityAlignment.BOTTOM_CENTER)
    _dim_v(msp, px + E + 18, py - br, py + br, f"Φ{BORE_D}", side=1)
    _dim_v(msp, px - 18, py - pod, py + pod, f"Φ{PLATE_OD}", side=-1)

    _txt(msp, "A-A 剖视（下游侧倒角）", 4.0, (px + E / 2, py + pod + 35), TextEntityAlignment.BOTTOM_CENTER)
    _txt(msp, f"材料 {MAT_PL}  件数 1", 3.2, (px + E / 2, py - pod - 40), TextEntityAlignment.TOP_CENTER)
    _txt(msp, "孔口上游锐边 G≤0.0004d；禁止倒钝", 3.0, (px + E / 2, py - pod - 52), TextEntityAlignment.TOP_CENTER)

    return ox - 20, oy - 90, ox + 360, oy + 160


# ---------- C 取压法兰机加 ----------
def draw_orifice_flange(msp, ox, oy):
    thick = {"layer": "轮廓", "lineweight": LW_C}
    thin = {"layer": "细实线", "lineweight": LW_F}
    dash = {"layer": "虚线", "lineweight": LW_F, "linetype": "DASHED"}
    cen = {"layer": "中心线", "lineweight": LW_F, "linetype": "CENTER"}

    # 左：半剖主视（轴线水平）
    x0 = ox
    y0 = oy
    # 法兰盘
    _rect(msp, x0, y0 - FL_OD / 2, x0 + FL_C, y0 + FL_OD / 2, thick)
    msp.add_line((x0, y0 + METER_ID / 2), (x0 + FL_C, y0 + METER_ID / 2), dxfattribs=thin)
    msp.add_line((x0, y0 - METER_ID / 2), (x0 + FL_C, y0 - METER_ID / 2), dxfattribs=thin)
    # RF（右端面）
    msp.add_line((x0 + FL_C - FL_RF_H, y0 + FL_RF / 2), (x0 + FL_C, y0 + FL_RF / 2), dxfattribs=thin)
    msp.add_line((x0 + FL_C - FL_RF_H, y0 - FL_RF / 2), (x0 + FL_C, y0 - FL_RF / 2), dxfattribs=thin)
    # 颈
    neck_l = FL_H - FL_C
    msp.add_line((x0 - neck_l, y0 + FL_NECK / 2), (x0, y0 + FL_NECK / 2), dxfattribs=thick)
    msp.add_line((x0 - neck_l, y0 - FL_NECK / 2), (x0, y0 - FL_NECK / 2), dxfattribs=thick)
    msp.add_line((x0 - neck_l, y0 + METER_ID / 2), (x0, y0 + METER_ID / 2), dxfattribs=dash)
    msp.add_line((x0 - neck_l, y0 - METER_ID / 2), (x0, y0 - METER_ID / 2), dxfattribs=dash)
    # 焊端外径
    msp.add_line((x0 - neck_l, y0 + PIPE_OD / 2), (x0 - neck_l - 8, y0 + PIPE_OD / 2), dxfattribs=thick)
    msp.add_line((x0 - neck_l, y0 - PIPE_OD / 2), (x0 - neck_l - 8, y0 - PIPE_OD / 2), dxfattribs=thick)
    _hatch_lines(msp, x0 - neck_l, y0 - FL_NECK / 2, x0 + FL_C, y0 - METER_ID / 2, step=5.5)

    # 取压孔：距密封面（孔板侧）约 TAP_OFFSET - GASKET_T（装配后对孔板面 25.4）
    # 机加标注：密封面到孔轴线 = TAP_OFFSET - GASKET_T（按垫厚修正），图注说明
    tap_from_rf = TAP_OFFSET - GASKET_T  # 23.4，使装配后距孔板面≈25.4
    ax = x0 + FL_C - tap_from_rf
    # 竖直取压孔 + 接管
    msp.add_line((ax, y0 + METER_ID / 2), (ax, y0 + FL_OD / 2), dxfattribs=dash)
    msp.add_line((ax - TAP_HOLE / 2, y0 + METER_ID / 2), (ax - TAP_HOLE / 2, y0 + FL_OD / 2 + 5), dxfattribs=thin)
    msp.add_line((ax + TAP_HOLE / 2, y0 + METER_ID / 2), (ax + TAP_HOLE / 2, y0 + FL_OD / 2 + 5), dxfattribs=thin)
    # 取压管焊于法兰外圆
    ty0 = y0 + FL_OD / 2
    ty1 = ty0 + TAP_PIPE_L
    _rect(msp, ax - TAP_PIPE_OD / 2, ty0, ax + TAP_PIPE_OD / 2, ty1, thick)
    msp.add_line((ax - TAP_PIPE_OD / 2 + TAP_PIPE_WALL, ty0), (ax - TAP_PIPE_OD / 2 + TAP_PIPE_WALL, ty1), dxfattribs=dash)
    msp.add_line((ax + TAP_PIPE_OD / 2 - TAP_PIPE_WALL, ty0), (ax + TAP_PIPE_OD / 2 - TAP_PIPE_WALL, ty1), dxfattribs=dash)

    msp.add_line((x0 - neck_l - 25, y0), (x0 + FL_C + 25, y0), dxfattribs=cen)

    # 尺寸
    _dim_h(msp, x0, x0 + FL_C, y0 - FL_OD / 2 - 28, f"C={FL_C}")
    _dim_h(msp, x0 - neck_l, x0 + FL_C, y0 - FL_OD / 2 - 48, f"H={FL_H}")
    _dim_h(msp, ax, x0 + FL_C, y0 + FL_OD / 2 + TAP_PIPE_L + 18, f"{tap_from_rf:.1f}（机加）")
    _dim_v(msp, x0 + FL_C + 22, y0 - FL_OD / 2, y0 + FL_OD / 2, f"Φ{int(FL_OD)}", side=1)
    _dim_v(msp, x0 - neck_l - 20, y0 - PIPE_OD / 2, y0 + PIPE_OD / 2, f"Φ{PIPE_OD}", side=-1)
    _txt(msp, f"取压孔 Φ{TAP_HOLE}", 3.0, (ax + 14, y0 + FL_OD / 4), TextEntityAlignment.LEFT)
    _txt(msp, f"装配后距孔板面 {TAP_OFFSET}±{TAP_TOL}", 3.0, (ax, ty1 + 12), TextEntityAlignment.BOTTOM_CENTER)

    _txt(
        msp,
        f"取压法兰 WN RF  HG/T20592 PN25 DN{DN}  材料{MAT_FL}  2件（上/下游各1，镜像）",
        3.8,
        (x0 + FL_C / 2, y0 + FL_OD / 2 + TAP_PIPE_L + 40),
        TextEntityAlignment.BOTTOM_CENTER,
    )
    _txt(
        msp,
        f"螺栓圆 Φ{int(FL_PCD)}  {FL_N_BOLT}×Φ{int(FL_HOLE)}  螺栓{FL_BOLT}  RF Φ{int(FL_RF)}×{FL_RF_H}",
        3.2,
        (x0 + FL_C / 2, y0 + FL_OD / 2 + TAP_PIPE_L + 28),
        TextEntityAlignment.BOTTOM_CENTER,
    )

    # 右：密封面视（法兰面）
    cx = ox + 320
    cy = y0
    msp.add_circle((cx, cy), FL_OD / 2, dxfattribs=thick)
    msp.add_circle((cx, cy), FL_RF / 2, dxfattribs=thin)
    msp.add_circle((cx, cy), METER_ID / 2, dxfattribs=thick)
    msp.add_circle((cx, cy), FL_PCD / 2, dxfattribs=cen)
    for i in range(FL_N_BOLT):
        ang = math.radians(90 + i * 360 / FL_N_BOLT)
        bx = cx + FL_PCD / 2 * math.cos(ang)
        by = cy + FL_PCD / 2 * math.sin(ang)
        msp.add_circle((bx, by), FL_HOLE / 2, dxfattribs=thin)
    # 取压孔位置（顶部）
    msp.add_circle((cx, cy + (METER_ID + FL_OD) / 4), TAP_HOLE / 2, dxfattribs=thick)
    msp.add_line((cx - FL_OD / 2 - 15, cy), (cx + FL_OD / 2 + 15, cy), dxfattribs=cen)
    msp.add_line((cx, cy - FL_OD / 2 - 15), (cx, cy + FL_OD / 2 + 15), dxfattribs=cen)
    _dim_h(msp, cx - FL_PCD / 2, cx + FL_PCD / 2, cy - FL_OD / 2 - 25, f"Φ{int(FL_PCD)}")
    _txt(msp, "密封面视", 4.0, (cx, cy + FL_OD / 2 + 22), TextEntityAlignment.BOTTOM_CENTER)
    _txt(msp, "取压口朝上（或按配管）", 3.0, (cx, cy - FL_OD / 2 - 42), TextEntityAlignment.TOP_CENTER)

    return ox - 50, oy - FL_OD / 2 - 70, ox + 420, oy + FL_OD / 2 + TAP_PIPE_L + 55


# ---------- D 取压管 ----------
def draw_tap_pipe(msp, ox, oy):
    thick = {"layer": "轮廓", "lineweight": LW_C}
    dash = {"layer": "虚线", "lineweight": LW_F, "linetype": "DASHED"}
    cen = {"layer": "中心线", "lineweight": LW_F, "linetype": "CENTER"}

    L = TAP_PIPE_L
    od, w = TAP_PIPE_OD, TAP_PIPE_WALL
    id_ = od - 2 * w
    # 放大 2 倍画
    s = 2.5
    x0, y0 = ox, oy
    _rect(msp, x0, y0 - od * s / 2, x0 + L * s, y0 + od * s / 2, thick)
    msp.add_line((x0, y0 - id_ * s / 2), (x0 + L * s, y0 - id_ * s / 2), dxfattribs=dash)
    msp.add_line((x0, y0 + id_ * s / 2), (x0 + L * s, y0 + id_ * s / 2), dxfattribs=dash)
    msp.add_line((x0 - 10, y0), (x0 + L * s + 10, y0), dxfattribs=cen)
    # 坡口示意（两端 BW）
    for x in (x0, x0 + L * s):
        msp.add_line((x, y0 - od * s / 2), (x + (6 if x == x0 else -6), y0 - id_ * s / 2), dxfattribs=thick)
        msp.add_line((x, y0 + od * s / 2), (x + (6 if x == x0 else -6), y0 + id_ * s / 2), dxfattribs=thick)

    _dim_h(msp, x0, x0 + L * s, y0 - od * s / 2 - 18, f"L={TAP_PIPE_L}")
    _dim_v(msp, x0 + L * s + 16, y0 - od * s / 2, y0 + od * s / 2, f"Φ{TAP_PIPE_OD}×{TAP_PIPE_WALL}", side=1)
    _txt(
        msp,
        f"取压管 {TAP_NPS} BW  材料{MAT_TAP}  件数 2  （一端焊法兰，一端接仪表阀/管件）",
        3.5,
        (x0 + L * s / 2, y0 + od * s / 2 + 22),
        TextEntityAlignment.BOTTOM_CENTER,
    )
    _txt(msp, "坡口按 GB/T 985.1；深冷焊后酸洗钝化", 3.0, (x0 + L * s / 2, y0 - od * s / 2 - 35), TextEntityAlignment.TOP_CENTER)
    return ox - 20, oy - 60, ox + L * s + 80, oy + 50


# ---------- 明细表 + 技术要求 ----------
def draw_bom_notes(msp, ox, oy):
    rows = [
        ("序号", "名称", "规格/材料", "数量", "备注"),
        ("1", "上游取压法兰", f"WN RF DN{DN} PN25 {MAT_FL}", "1", "HG/T20592"),
        ("2", "下游取压法兰", f"WN RF DN{DN} PN25 {MAT_FL}", "1", "与1镜像，下游"),
        ("3", "孔板片", f"Φ{PLATE_OD}×{PLATE_E} 孔Φ{BORE_D} {MAT_PL}", "1", f"{TAG}"),
        ("4", "上游取压管", f"{TAP_NPS} Φ{TAP_PIPE_OD}×{TAP_PIPE_WALL} {MAT_TAP}", "1", "BW"),
        ("5", "下游取压管", f"{TAP_NPS} Φ{TAP_PIPE_OD}×{TAP_PIPE_WALL} {MAT_TAP}", "1", "BW"),
        ("6", "全螺纹螺柱+螺母", f"{STUD} / {NUT}  {MAT_FAST}", f"{FL_N_BOLT}", "含垫圈"),
        ("7", "金属缠绕垫", f"DN{DN} PN25 RF  {MAT_GST}", "2", "深冷适用"),
        ("8", "短节", f"Φ{PIPE_OD}×{PIPE_WALL} L={STUB_L} {MAT_STUB}", "2", "BW两端"),
    ]
    col_w = [28, 70, 200, 36, 70]
    row_h = 14
    x = ox
    y = oy
    # header bar
    total_w = sum(col_w)
    _txt(msp, "明细表", 4.5, (x + total_w / 2, y + 8), TextEntityAlignment.BOTTOM_CENTER)
    for i, row in enumerate(rows):
        yy = y - i * row_h
        xx = x
        for j, cell in enumerate(row):
            _rect(msp, xx, yy - row_h, xx + col_w[j], yy, {"layer": "表格", "lineweight": LW_F})
            _txt(msp, cell, 2.8 if i else 3.0, (xx + 2, yy - row_h / 2), TextEntityAlignment.MIDDLE_LEFT)
            xx += col_w[j]

    notes = [
        "技术要求：",
        f"1. 本图按计算书 {TAG}（S/N {SERIAL}）及 GB/T2624.2 / ISO5167-2 法兰取压执行。",
        f"2. 孔径 d={BORE_D} mm 为 20℃ 值；深冷工况按 Fa 膨胀修正（计算书 Fa=0.9938）复核实流孔径。",
        f"3. 取压方式：法兰取压；取压孔轴线距孔板上/下游端面 {TAP_OFFSET}±{TAP_TOL} mm；孔径 Φ{TAP_HOLE}（≤13 且 <0.13D）。",
        "4. 孔板上游面平面度、粗糙度及入口锐边按 GB/T2624.2；下游 45° 倒角，孔口圆柱段厚度 e 如图。",
        f"5. 法兰标准 HG/T20592 PN25 RF 带颈对焊；密封面、螺栓孔加工按标准公差；配对法兰同批配钻。",
        f"6. 介质 LNG，设计温度 {TF_C}℃；材料 {MAT_FL}/{MAT_PL}；焊接 WPS 按深冷不锈钢，焊后酸洗钝化。",
        "7. 焊缝：法兰颈与短节 BW；取压管与法兰角焊缝/安放焊按批复 WPS；RT/PT 按业主规格书。",
        "8. 装配：孔板手柄朝上，上游面迎流；垫片对中；螺柱对角均匀紧固；禁止损伤孔口锐边。",
        "9. 试压：强度/密封按管道试验压力；取压管口盲死。洁净度按仪表管线要求。",
        "10. 未注线性尺寸公差 IT12；未注形位公差按 GB/T 1184 K；单位 mm。",
    ]
    ny = y - len(rows) * row_h - 20
    for i, line in enumerate(notes):
        _txt(msp, line, 3.0 if i else 3.8, (x, ny - i * 11), TextEntityAlignment.TOP_LEFT)

    return x, ny - len(notes) * 11 - 10, x + total_w + 20, y + 20


def build():
    doc = _setup_doc()
    msp = doc.modelspace()

    # 布局坐标（单位 mm，模型空间拼大图）
    # A 总装
    draw_assembly(msp, 0, 0)
    _frame(msp, -60, -320, 620, 360, "")
    _txt(msp, "A  总装配图（半剖）", 6.0, (280, 340), TextEntityAlignment.BOTTOM_CENTER)

    # B 孔板
    draw_plate(msp, 700, 80)
    _txt(msp, "B  孔板片机加工图", 6.0, (880, 260), TextEntityAlignment.BOTTOM_CENTER)

    # C 取压法兰
    draw_orifice_flange(msp, 0, -650)
    _txt(msp, "C  取压法兰机加工图", 6.0, (200, -380), TextEntityAlignment.BOTTOM_CENTER)

    # D 取压管
    draw_tap_pipe(msp, 700, -550)
    _txt(msp, "D  取压管机加工图", 6.0, (820, -470), TextEntityAlignment.BOTTOM_CENTER)

    # 明细 + 技术要求
    draw_bom_notes(msp, 700, -650)

    # 图框标题栏简要
    _txt(
        msp,
        f"位号 {TAG}  |  出厂号 {SERIAL}  |  {MODEL}  |  DN{DN} PN25 法兰对夹孔板 生产机加装配图",
        5.0,
        (500, -1000),
        TextEntityAlignment.BOTTOM_CENTER,
    )
    _txt(
        msp,
        "比例 示意（以标注尺寸为准）  |  DXF R2013 单位 mm  |  可直接下发机加/装配",
        3.5,
        (500, -1018),
        TextEntityAlignment.BOTTOM_CENTER,
    )

    zoom.extents(msp)
    DXF_DIR.mkdir(parents=True, exist_ok=True)
    PNG_DIR.mkdir(parents=True, exist_ok=True)
    dxf_path = DXF_DIR / f"{TAG}_法兰对夹孔板_机加装配图.dxf"
    doc.saveas(dxf_path)
    return dxf_path


def render_png(dxf_path: Path, png_path: Path):
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from ezdxf.addons.drawing import RenderContext, Frontend
    from ezdxf.addons.drawing.matplotlib import MatplotlibBackend
    from ezdxf.addons.drawing.config import Configuration, ColorPolicy, BackgroundPolicy
    from ezdxf.addons.drawing.properties import LayoutProperties

    plt.rcParams["font.sans-serif"] = ["SimHei", "Microsoft YaHei", "SimSun"]
    plt.rcParams["axes.unicode_minus"] = False

    doc = ezdxf.readfile(dxf_path)
    msp = doc.modelspace()
    fig = plt.figure(figsize=(18, 14), dpi=200)
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
    fig.savefig(png_path, dpi=200, facecolor="white", bbox_inches="tight", pad_inches=0.15)
    plt.close(fig)


def main():
    dxf = build()
    png = PNG_DIR / f"{TAG}_法兰对夹孔板_机加装配图.png"
    render_png(dxf, png)
    preview = OUT_DIR / f"预览_{TAG}_机加装配图.png"
    from shutil import copy2

    copy2(png, preview)
    print("OK", dxf)
    print("PNG", png)
    print("PREVIEW", preview)


if __name__ == "__main__":
    main()
