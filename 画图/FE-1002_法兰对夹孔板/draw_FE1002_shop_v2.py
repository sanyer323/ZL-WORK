# -*- coding: utf-8 -*-
"""
FE-1002 法兰对夹孔板 — 正式生产机加/装配图（分张）
标准依据：计算书 FE-1002 + HG/T20592 PN25 + GB/T2624.2 / ISO5167-2
输出：DXF R2013 + 矢量多页 PDF（matplotlib PDF，非栅格）
"""
from __future__ import annotations

import math
from pathlib import Path

import ezdxf
from ezdxf import units, zoom
from ezdxf.enums import TextEntityAlignment

# ===================== 参数区 =====================
TAG = "FE-1002"
SERIAL = "26031402"
MODEL = "ROH10×JX25N2"
DWG_NO = "FE-1002-00"
COMPANY = "生产加工图"

DN = 250
PIPE_OD = 273.0
PIPE_WALL = 4.0
METER_ID = 265.0
BORE_D = 136.18
BETA = 0.5139
TF_C = -162.0
PF_KPAG = 600.0
FA = 0.9938

# 孔板片（WIKA/常规：DN200~350 板厚常用 6）
PLATE_OD = 320.0
PLATE_E = 6.0
PLATE_E_EDGE = 2.5
BEVEL = 45.0
HANDLE_W = 36.0
HANDLE_L = 50.0
BORE_TOL = "±0.05"      # 孔径加工公差（机加）
OD_TOL = "0/-0.2"

# HG/T20592-2009 PN25 DN250 WN RF 系列Ⅰ
FL_OD = 425.0
FL_PCD = 370.0
FL_HOLE = 30.0
FL_N = 12
FL_BOLT = "M27"
FL_C = 32.0
FL_RF = 335.0
FL_RF_H = 2.0
FL_NECK = 298.0
FL_H = 88.0

GASKET_T = 2.0
GASKET_OD = 335.0
GASKET_ID = 274.0
STUB_L = 120.0

TAP_OFF = 25.4
TAP_TOL = 0.8
TAP_HOLE = 8.0
TAP_OD = 21.3
TAP_WALL = 2.77       # 1/2" Sch40S 常用
TAP_L = 100.0

MAT = "F304/F304L"
MAT_GST = "缠绕垫 PN25 RF 内环304+柔性石墨(深冷)"
MAT_FAST = "螺柱B8M / 螺母B8M"

TEXT = 3.2
OUT = Path(__file__).resolve().parent
DXF_DIR = OUT / "DXF"
# ==================================================

LW_C, LW_F, LW_H = 50, 18, 13
A3W, A3H = 420.0, 297.0


def setup_doc():
    doc = ezdxf.new("R2013", setup=True)
    doc.units = units.MM
    doc.header["$INSUNITS"] = 4
    doc.header["$MEASUREMENT"] = 1
    for n, c, lw, lt in [
        ("轮廓", 7, LW_C, "Continuous"),
        ("细实线", 7, LW_F, "Continuous"),
        ("中心线", 1, LW_F, "CENTER"),
        ("虚线", 7, LW_F, "DASHED"),
        ("剖面线", 7, LW_H, "Continuous"),
        ("标注", 3, LW_F, "Continuous"),
        ("文字", 7, LW_F, "Continuous"),
        ("图框", 7, LW_F, "Continuous"),
        ("表格", 7, LW_F, "Continuous"),
    ]:
        if n not in doc.layers:
            doc.layers.add(n, color=c, linetype=lt, lineweight=lw)
    if "CENTER" not in doc.linetypes:
        doc.linetypes.add("CENTER", pattern="A,.9,-.05,.09,-.05")
    if "DASHED" not in doc.linetypes:
        doc.linetypes.add("DASHED", pattern="A,.5,-.25")
    if "CN" not in doc.styles:
        doc.styles.add("CN", font="simhei.ttf")
    else:
        doc.styles.get("CN").dxf.font = "simhei.ttf"
    doc.styles.get("Standard").dxf.font = "simhei.ttf"
    return doc


def T(msp, s, h, xy, align=TextEntityAlignment.LEFT, layer="文字", rot=0):
    t = msp.add_text(str(s), height=h, dxfattribs={"layer": layer, "style": "CN", "rotation": rot})
    t.set_placement(xy, align=align)
    return t


def L(msp, a, b, layer="轮廓", lw=LW_C, lt="Continuous"):
    msp.add_line(a, b, dxfattribs={"layer": layer, "lineweight": lw, "linetype": lt})


def C(msp, c, r, layer="轮廓", lw=LW_C, lt="Continuous"):
    msp.add_circle(c, r, dxfattribs={"layer": layer, "lineweight": lw, "linetype": lt})


def rect(msp, x0, y0, x1, y1, layer="轮廓", lw=LW_C):
    L(msp, (x0, y0), (x1, y0), layer, lw)
    L(msp, (x1, y0), (x1, y1), layer, lw)
    L(msp, (x1, y1), (x0, y1), layer, lw)
    L(msp, (x0, y1), (x0, y0), layer, lw)


def hatch(msp, x0, y0, x1, y1, step=3.8, ang=45.0):
    """下半剖面线（相对局部原点，y<=0 部分）"""
    y0 = min(y0, 0.0)
    y1 = min(y1, 0.0)
    if y1 <= y0:
        return
    a = math.radians(ang)
    dx, dy = math.cos(a), math.sin(a)
    nx, ny = -dy, dx
    corners = [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]
    ps = [p[0] * nx + p[1] * ny for p in corners]
    pmin, pmax = min(ps), max(ps)
    span = abs((x1 - x0) * dx) + abs((y1 - y0) * dy) + 60

    def clip(p1, p2):
        xmin, xmax = min(x0, x1), max(x0, x1)
        ymin, ymax = min(y0, y1), max(y0, y1)
        dxs, dys = p2[0] - p1[0], p2[1] - p1[1]
        t0, t1 = 0.0, 1.0
        for p, q in ((-dxs, p1[0] - xmin), (dxs, xmax - p1[0]), (-dys, p1[1] - ymin), (dys, ymax - p1[1])):
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
        seg = clip((cx - dx * span, cy - dy * span), (cx + dx * span, cy + dy * span))
        if seg:
            L(msp, seg[0], seg[1], "剖面线", LW_H)
        p += step


def dim_h(msp, x0, x1, y, label, off=2.2):
    L(msp, (x0, y), (x1, y), "标注", LW_F)
    for x in (x0, x1):
        L(msp, (x, y - 1.8), (x, y + 1.8), "标注", LW_F)
    s = 2.6
    L(msp, (x0, y), (x0 + s, y + 0.9), "标注", LW_F)
    L(msp, (x0, y), (x0 + s, y - 0.9), "标注", LW_F)
    L(msp, (x1, y), (x1 - s, y + 0.9), "标注", LW_F)
    L(msp, (x1, y), (x1 - s, y - 0.9), "标注", LW_F)
    T(msp, label, TEXT, ((x0 + x1) / 2, y + off), TextEntityAlignment.BOTTOM_CENTER, "标注")


def dim_v(msp, x, y0, y1, label, side=-1):
    L(msp, (x, y0), (x, y1), "标注", LW_F)
    for y in (y0, y1):
        L(msp, (x - 1.8, y), (x + 1.8, y), "标注", LW_F)
    s = 2.6
    L(msp, (x, y0), (x - 0.9, y0 + s), "标注", LW_F)
    L(msp, (x, y0), (x + 0.9, y0 + s), "标注", LW_F)
    L(msp, (x, y1), (x - 0.9, y1 - s), "标注", LW_F)
    L(msp, (x, y1), (x + 0.9, y1 - s), "标注", LW_F)
    T(msp, label, TEXT, (x + 5.5 * side, (y0 + y1) / 2), TextEntityAlignment.MIDDLE_CENTER, "标注", 90)


def balloon(msp, x, y, bx, by, n, r=4.5):
    L(msp, (x, y), (bx, by), "标注", LW_F)
    C(msp, (bx, by), r, "轮廓", LW_C)
    T(msp, str(n), 3.2, (bx, by), TextEntityAlignment.MIDDLE_CENTER)


def roughness(msp, x, y, ra="Ra1.6", rot=0):
    """简易表面粗糙度符号"""
    s = 3.5
    L(msp, (x, y), (x - s * 0.5, y + s), "标注", LW_F)
    L(msp, (x, y), (x + s * 0.5, y + s), "标注", LW_F)
    L(msp, (x - s * 0.5, y + s), (x + s * 0.35, y + s), "标注", LW_F)
    T(msp, ra, 2.4, (x + s * 0.7, y + s * 0.55), TextEntityAlignment.LEFT, "标注", rot)


def title_block(msp, ox, oy, sheet, total, title, scale, part_no):
    """A3 图框 + 标题栏（右下）"""
    # 外边框 / 内边框
    rect(msp, ox, oy, ox + A3W, oy + A3H, "图框", LW_C)
    m = 10.0
    rect(msp, ox + m, oy + m, ox + A3W - m, oy + A3H - m, "图框", LW_F)
    # 标题栏 180×56
    tw, th = 180.0, 56.0
    tx0 = ox + A3W - m - tw
    ty0 = oy + m
    rows = [16, 12, 12, 16]
    cols = [50, 70, 30, 30]
    # outer
    rect(msp, tx0, ty0, tx0 + tw, ty0 + th, "图框", LW_C)
    y = ty0
    for h in rows:
        y += h
        L(msp, (tx0, y), (tx0 + tw, y), "图框", LW_F)
    x = tx0
    for w in cols[:-1]:
        x += w
        L(msp, (x, ty0), (x, ty0 + th), "图框", LW_F)
    # 合并区文字
    T(msp, COMPANY, 3.5, (tx0 + 25, ty0 + 48), TextEntityAlignment.MIDDLE_CENTER)
    T(msp, title, 4.0, (tx0 + 85, ty0 + 48), TextEntityAlignment.MIDDLE_CENTER)
    T(msp, f"材料\n{MAT}", 2.6, (tx0 + 135, ty0 + 48), TextEntityAlignment.MIDDLE_CENTER)
    T(msp, f"比例 {scale}", 2.8, (tx0 + 165, ty0 + 48), TextEntityAlignment.MIDDLE_CENTER)

    T(msp, f"位号 {TAG}", 3.0, (tx0 + 25, ty0 + 28), TextEntityAlignment.MIDDLE_CENTER)
    T(msp, f"图号 {part_no}", 3.0, (tx0 + 85, ty0 + 28), TextEntityAlignment.MIDDLE_CENTER)
    T(msp, f"共{total}张", 2.6, (tx0 + 135, ty0 + 28), TextEntityAlignment.MIDDLE_CENTER)
    T(msp, f"第{sheet}张", 2.6, (tx0 + 165, ty0 + 28), TextEntityAlignment.MIDDLE_CENTER)

    T(msp, f"出厂号 {SERIAL}", 2.6, (tx0 + 25, ty0 + 16), TextEntityAlignment.MIDDLE_CENTER)
    T(msp, f"型号 {MODEL}", 2.6, (tx0 + 85, ty0 + 16), TextEntityAlignment.MIDDLE_CENTER)
    T(msp, "单位 mm", 2.6, (tx0 + 135, ty0 + 16), TextEntityAlignment.MIDDLE_CENTER)
    T(msp, "R2013", 2.4, (tx0 + 165, ty0 + 16), TextEntityAlignment.MIDDLE_CENTER)

    T(msp, "设计", 2.4, (tx0 + 12, ty0 + 6), TextEntityAlignment.MIDDLE_CENTER)
    T(msp, "校核", 2.4, (tx0 + 40, ty0 + 6), TextEntityAlignment.MIDDLE_CENTER)
    T(msp, "审核", 2.4, (tx0 + 70, ty0 + 6), TextEntityAlignment.MIDDLE_CENTER)
    T(msp, f"DN{DN} PN25 HG/T20592 RF 法兰取压", 2.6, (tx0 + 130, ty0 + 6), TextEntityAlignment.MIDDLE_CENTER)

    # 左上图名条
    T(msp, f"{TAG}  {title}", 5.0, (ox + m + 4, oy + A3H - m - 8), TextEntityAlignment.LEFT)


def sheet_origin(i: int):
    """每张 A3 在模型空间横向排列，间距 40"""
    return i * (A3W + 40.0), 0.0


# ---------- 第1张：总装 ----------
def draw_sheet1(msp):
    ox, oy = sheet_origin(0)
    title_block(msp, ox, oy, 1, 4, "法兰对夹孔板 总装配图", "1:2.5", f"{DWG_NO}-A")

    # 绘图区原点（图框内）
    bx, by = ox + 30, oy + 95
    sc = 1 / 2.5  # 显示比例

    def S(x, y):
        return (bx + x * sc, by + y * sc)

    thick, thin = LW_C, LW_F
    pipe_od, pipe_id = PIPE_OD, METER_ID
    neck = FL_H - FL_C
    g, H = GASKET_T, PLATE_E
    stub = STUB_L

    x0 = 0.0
    xs1 = stub
    xfl1 = xs1 + neck
    xg1 = xfl1 + FL_C
    xpl = xg1 + g
    xg2 = xpl + H
    xfl2 = xg2 + g
    xn2 = xfl2 + FL_C
    xs2 = xn2 + neck
    xend = xs2 + stub

    # 中心线
    L(msp, S(x0 - 20, 0), S(xend + 20, 0), "中心线", LW_F, "CENTER")

    def pipe(xa, xb):
        L(msp, S(xa, pipe_od / 2), S(xb, pipe_od / 2), "轮廓", thick)
        L(msp, S(xa, -pipe_od / 2), S(xb, -pipe_od / 2), "轮廓", thick)
        L(msp, S(xa, pipe_id / 2), S(xb, pipe_id / 2), "虚线", thin, "DASHED")
        L(msp, S(xa, -pipe_id / 2), S(xb, -pipe_id / 2), "虚线", thin, "DASHED")

    pipe(x0, xs1)
    pipe(xs2, xend)

    def fl(xa, face):
        xb = xa + FL_C
        # 盘
        pts = [S(xa, FL_OD / 2), S(xb, FL_OD / 2), S(xb, -FL_OD / 2), S(xa, -FL_OD / 2)]
        for a, b in zip(pts, pts[1:] + pts[:1]):
            L(msp, a, b, "轮廓", thick)
        L(msp, S(xa, pipe_id / 2), S(xb, pipe_id / 2), "细实线", thin)
        L(msp, S(xa, -pipe_id / 2), S(xb, -pipe_id / 2), "细实线", thin)
        # RF
        if face > 0:
            L(msp, S(xb - FL_RF_H, FL_RF / 2), S(xb, FL_RF / 2), "细实线", thin)
            L(msp, S(xb - FL_RF_H, -FL_RF / 2), S(xb, -FL_RF / 2), "细实线", thin)
            n0, n1 = xa - neck, xa
        else:
            L(msp, S(xa, FL_RF / 2), S(xa + FL_RF_H, FL_RF / 2), "细实线", thin)
            L(msp, S(xa, -FL_RF / 2), S(xa + FL_RF_H, -FL_RF / 2), "细实线", thin)
            n0, n1 = xb, xb + neck
        L(msp, S(n0, FL_NECK / 2), S(n1, FL_NECK / 2), "轮廓", thick)
        L(msp, S(n0, -FL_NECK / 2), S(n1, -FL_NECK / 2), "轮廓", thick)
        L(msp, S(n0, pipe_id / 2), S(n1, pipe_id / 2), "虚线", thin, "DASHED")
        L(msp, S(n0, -pipe_id / 2), S(n1, -pipe_id / 2), "虚线", thin, "DASHED")
        # 螺栓孔
        C(msp, S((xa + xb) / 2, FL_PCD / 2 * 0.9), 3.5, "细实线", thin)
        C(msp, S((xa + xb) / 2, -FL_PCD / 2 * 0.9), 3.5, "虚线", thin, "DASHED")
        # 剖面（模型坐标下半）
        # hatch in real coords then... use scaled hatch via converting
        # 简化：在显示坐标画剖面
        sx0, sy0 = S(xa, 0)[0], S(0, -FL_OD / 2)[1]
        sx1, sy1 = S(xb, 0)[0], S(0, -pipe_id / 2)[1]
        # 直接用局部 hatch：转到 by 基准
        _hatch_abs(msp, S(xa, -FL_OD / 2)[0], S(xa, -FL_OD / 2)[1], S(xb, -pipe_id / 2)[0], S(xb, -pipe_id / 2)[1])

    def _hatch_abs(msp, x0, y0, x1, y1, step=4.5):
        if y1 > y0:
            y0, y1 = y1, y0
        # only below centerline by
        y0 = min(y0, by)
        y1 = min(y1, by)
        if y1 >= y0:
            return
        a = math.radians(45)
        dx, dy = math.cos(a), math.sin(a)
        nx, ny = -dy, dx
        corners = [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]
        ps = [p[0] * nx + p[1] * ny for p in corners]
        pmin, pmax = min(ps), max(ps)
        span = abs((x1 - x0) * dx) + abs((y1 - y0) * dy) + 80
        p = pmin - step
        while p <= pmax + step:
            cx, cy = nx * p, ny * p
            p1 = (cx - dx * span, cy - dy * span)
            p2 = (cx + dx * span, cy + dy * span)
            # Liang-Barsky
            xmin, xmax = min(x0, x1), max(x0, x1)
            ymin, ymax = min(y0, y1), max(y0, y1)
            dxs, dys = p2[0] - p1[0], p2[1] - p1[1]
            t0, t1 = 0.0, 1.0
            ok = True
            for pp, q in ((-dxs, p1[0] - xmin), (dxs, xmax - p1[0]), (-dys, p1[1] - ymin), (dys, ymax - p1[1])):
                if abs(pp) < 1e-12:
                    if q < 0:
                        ok = False
                        break
                    continue
                r = q / pp
                if pp < 0:
                    t0 = max(t0, r)
                else:
                    t1 = min(t1, r)
                if t0 > t1:
                    ok = False
                    break
            if ok:
                L(msp, (p1[0] + t0 * dxs, p1[1] + t0 * dys), (p1[0] + t1 * dxs, p1[1] + t1 * dys), "剖面线", LW_H)
            p += step

    fl(xfl1, +1)
    fl(xfl2, -1)

    # 垫片
    for xa in (xg1, xg2):
        x0s, y0s = S(xa, -GASKET_OD / 2)
        x1s, y1s = S(xa + g, GASKET_OD / 2)
        rect(msp, x0s, y0s, x1s, y1s, "细实线", thin)

    # 孔板
    br, pod = BORE_D / 2, PLATE_OD / 2
    e = PLATE_E_EDGE
    bev = PLATE_E - e
    x0s, y0s = S(xpl, -pod)
    x1s, y1s = S(xpl + H, pod)
    rect(msp, x0s, y0s, x1s, y1s, "轮廓", thick)
    _hatch_abs(msp, S(xpl, -pod)[0], S(xpl, -pod)[1], S(xpl + H, 0)[0], S(xpl + H, 0)[1], 3.5)
    # 孔口
    L(msp, S(xpl, br), S(xpl + e, br), "轮廓", thick)
    L(msp, S(xpl, -br), S(xpl + e, -br), "轮廓", thick)
    L(msp, S(xpl + e, br), S(xpl + H, br + bev), "轮廓", thick)
    L(msp, S(xpl + e, -br), S(xpl + H, -br - bev), "轮廓", thick)
    L(msp, S(xpl + H, br + bev), S(xpl + H, -br - bev), "轮廓", thick)
    L(msp, S(xpl, br), S(xpl, -br), "轮廓", thick)

    # 手柄
    hx = xpl + H / 2
    L(msp, S(hx, pod), S(hx, pod + 25), "轮廓", thick)
    rect(msp, S(hx - HANDLE_W / 2, pod + 25)[0], S(hx - HANDLE_W / 2, pod + 25)[1],
         S(hx + HANDLE_W / 2, pod + 25 + 28)[0], S(hx + HANDLE_W / 2, pod + 25 + 28)[1], "轮廓", thick)

    # 取压管
    def tap(face):
        if face > 0:
            ax = xpl - TAP_OFF
        else:
            ax = xpl + H + TAP_OFF
        L(msp, S(ax - TAP_OD / 2, FL_OD / 2), S(ax - TAP_OD / 2, FL_OD / 2 + TAP_L), "轮廓", thick)
        L(msp, S(ax + TAP_OD / 2, FL_OD / 2), S(ax + TAP_OD / 2, FL_OD / 2 + TAP_L), "轮廓", thick)
        L(msp, S(ax - TAP_OD / 2, FL_OD / 2 + TAP_L), S(ax + TAP_OD / 2, FL_OD / 2 + TAP_L), "轮廓", thick)
        L(msp, S(ax, FL_OD / 2), S(ax, pipe_id / 2), "虚线", thin, "DASHED")
        return ax

    ax1 = tap(+1)
    ax2 = tap(-1)

    # 螺柱
    for yy in (FL_PCD / 2 * 0.88, -FL_PCD / 2 * 0.88):
        L(msp, S(xfl1 + 5, yy), S(xfl2 + FL_C - 5, yy), "轮廓", thick)
        for xx in (xfl1 + 5, xfl2 + FL_C - 5):
            rect(msp, S(xx - 5, yy - 6)[0], S(xx - 5, yy - 6)[1], S(xx + 5, yy + 6)[0], S(xx + 5, yy + 6)[1], "轮廓", thick)

    # 球标（显示坐标）
    balloon(msp, *S(xfl1 + FL_C / 2, -FL_OD / 2), *S(xfl1 - 15, -FL_OD / 2 - 55), "1")
    balloon(msp, *S(xfl2 + FL_C / 2, -FL_OD / 2), *S(xfl2 + 40, -FL_OD / 2 - 55), "2")
    balloon(msp, *S(xpl + H / 2, -pod), *S(xpl + H / 2, -FL_OD / 2 - 55), "3")
    balloon(msp, *S(ax1, FL_OD / 2 + TAP_L), *S(ax1 - 35, FL_OD / 2 + TAP_L + 25), "4")
    balloon(msp, *S(ax2, FL_OD / 2 + TAP_L), *S(ax2 + 35, FL_OD / 2 + TAP_L + 25), "5")
    balloon(msp, *S((xfl1 + xfl2) / 2, FL_PCD / 2 * 0.88), *S((xfl1 + xfl2) / 2, FL_OD / 2 + 80), "6")
    balloon(msp, *S(xg1 + g / 2, GASKET_OD / 2), *S(xg1 - 30, FL_OD / 2 + 55), "7")
    balloon(msp, *S(stub / 2, pipe_od / 2), *S(stub / 2, FL_OD / 2 + 55), "8")

    # 尺寸（按显示坐标）
    dim_h(msp, S(xfl1, 0)[0], S(xfl2 + FL_C, 0)[0], S(0, -FL_OD / 2 - 70)[1], f"≈{int(xfl2 + FL_C - xfl1)}")
    dim_v(msp, S(x0 - 25, 0)[0], S(0, -FL_OD / 2)[1], S(0, FL_OD / 2)[1], f"Φ{int(FL_OD)}", -1)
    T(msp, f"Φ{PIPE_OD}×{PIPE_WALL}", 3.0, S(stub / 2, pipe_od / 2 + 12), TextEntityAlignment.BOTTOM_CENTER, "标注")
    T(msp, f"d=Φ{BORE_D}", 3.0, S(xpl + H + 20, 0), TextEntityAlignment.MIDDLE_LEFT, "标注")
    T(msp, f"取压距孔板面 {TAP_OFF}±{TAP_TOL}", 2.8, S((ax1 + ax2) / 2, FL_OD / 2 + TAP_L + 40), TextEntityAlignment.BOTTOM_CENTER, "标注")

    # 流向
    yf = S(0, -FL_OD / 2 - 95)[1]
    L(msp, (S(xfl1, 0)[0], yf), (S(xfl2 + FL_C - 30, 0)[0], yf), "标注", LW_F)
    L(msp, (S(xfl2 + FL_C - 30, 0)[0], yf), (S(xfl2 + FL_C - 42, 0)[0], yf + 4), "标注", LW_F)
    L(msp, (S(xfl2 + FL_C - 30, 0)[0], yf), (S(xfl2 + FL_C - 42, 0)[0], yf - 4), "标注", LW_F)
    T(msp, "介质流向（下游侧倒角）", 3.5, (S((xfl1 + xfl2) / 2, 0)[0], yf - 8), TextEntityAlignment.TOP_CENTER)

    # 明细表
    bom = [
        ("序号", "代号", "名称", "规格及材料", "数量", "备注"),
        ("1", f"{DWG_NO}-1", "上游取压法兰", f"WN RF DN{DN} PN25 {MAT}", "1", "HG/T20592"),
        ("2", f"{DWG_NO}-2", "下游取压法兰", f"WN RF DN{DN} PN25 {MAT}", "1", "与1对称"),
        ("3", f"{DWG_NO}-3", "孔板片", f"Φ{PLATE_OD}×{PLATE_E} 孔Φ{BORE_D} {MAT}", "1", TAG),
        ("4", f"{DWG_NO}-4", "上游取压管", f"DN15 Φ{TAP_OD}×{TAP_WALL} L={TAP_L} {MAT}", "1", "BW"),
        ("5", f"{DWG_NO}-4", "下游取压管", f"DN15 Φ{TAP_OD}×{TAP_WALL} L={TAP_L} {MAT}", "1", "BW"),
        ("6", "-", "螺柱/螺母", f"M27 全螺纹  {MAT_FAST}", f"{FL_N}", "含垫圈"),
        ("7", "-", "缠绕垫", f"DN{DN} PN25  {MAT_GST}", "2", "深冷"),
        ("8", f"{DWG_NO}-5", "短节", f"Φ{PIPE_OD}×{PIPE_WALL} L={STUB_L} {MAT}", "2", "BW"),
    ]
    tw = [18, 42, 48, 130, 22, 40]
    tx = ox + 30
    ty = oy + 78
    T(msp, "明细表", 3.5, (tx + sum(tw) / 2, ty + 3), TextEntityAlignment.BOTTOM_CENTER)
    rh = 7.5
    for i, row in enumerate(bom):
        yy = ty - i * rh
        xx = tx
        for j, cell in enumerate(row):
            rect(msp, xx, yy - rh, xx + tw[j], yy, "表格", LW_F)
            T(msp, cell, 2.2 if i else 2.4, (xx + 1.2, yy - rh / 2), TextEntityAlignment.MIDDLE_LEFT, "表格")
            xx += tw[j]

    notes = [
        "技术要求",
        f"1. 按 GB/T2624.2 / ISO5167-2 法兰取压；孔径 d={BORE_D}（20℃），深冷按 Fa={FA} 复核。",
        f"2. 取压孔轴线距孔板上/下游端面 {TAP_OFF}±{TAP_TOL}；取压孔径 Φ{TAP_HOLE}（≤13 且 <0.13D）。",
        "3. 孔板上游迎流，下游 45° 倒角；入口锐边不得倒钝；装配时手柄朝上。",
        f"4. 介质 LNG，Tf={TF_C}℃，Pf={PF_KPAG} kPaG；材料 {MAT}；深冷焊接及酸洗钝化按批复 WPS。",
        "5. 紧固对角均匀；禁止磕碰孔口；强度/密封试验按管道试验规程，取压管口封闭。",
        "6. 未注公差 IT12；未注形位公差 GB/T1184-K级。详见零件图。",
    ]
    nx, ny = ox + 30, oy + A3H - 25
    for i, line in enumerate(notes):
        T(msp, line, 2.6 if i else 3.2, (nx, ny - i * 7.2), TextEntityAlignment.TOP_LEFT)


# ---------- 第2张：孔板片 ----------
def draw_sheet2(msp):
    ox, oy = sheet_origin(1)
    title_block(msp, ox, oy, 2, 4, "孔板片 机加工图", "1:2 / 剖视2:1", f"{DWG_NO}-3")

    # 主视 1:2
    sc = 0.5
    cx = ox + 130
    cy = oy + 155

    def P(x, y):
        return (cx + x * sc, cy + y * sc)

    R, r = PLATE_OD / 2, BORE_D / 2
    C(msp, (cx, cy), R * sc, "轮廓", LW_C)
    C(msp, (cx, cy), r * sc, "轮廓", LW_C)
    L(msp, P(-R - 15, 0), P(R + 15, 0), "中心线", LW_F, "CENTER")
    L(msp, P(0, -R - 15), P(0, R + HANDLE_L + 5), "中心线", LW_F, "CENTER")
    # 手柄
    rect(msp, P(-HANDLE_W / 2, R)[0], P(-HANDLE_W / 2, R)[1], P(HANDLE_W / 2, R + HANDLE_L)[0], P(HANDLE_W / 2, R + HANDLE_L)[1], "轮廓", LW_C)
    T(msp, TAG, 3.0, P(0, R + HANDLE_L * 0.62), TextEntityAlignment.MIDDLE_CENTER)
    T(msp, "UP", 2.5, P(0, R + HANDLE_L * 0.32), TextEntityAlignment.MIDDLE_CENTER)
    T(msp, f"d={BORE_D}", 2.4, P(0, R + HANDLE_L * 0.12), TextEntityAlignment.MIDDLE_CENTER)

    # 流向箭头
    L(msp, P(r + 12, -20), P(r + 40, -20), "标注", LW_F)
    L(msp, P(r + 40, -20), P(r + 34, -16), "标注", LW_F)
    L(msp, P(r + 40, -20), P(r + 34, -24), "标注", LW_F)
    T(msp, "流向刻印→", 2.5, P(r + 26, -28), TextEntityAlignment.TOP_CENTER, "标注")

    dim_h(msp, P(-R, 0)[0], P(R, 0)[0], P(0, -R)[1] - 18, f"Φ{PLATE_OD} {OD_TOL}")
    dim_h(msp, P(-r, 0)[0], P(r, 0)[0], cy + 8, f"Φ{BORE_D} {BORE_TOL}")
    dim_v(msp, P(R, 0)[0] + 16, P(0, R)[1], P(0, R + HANDLE_L)[1], f"{HANDLE_L}", 1)
    dim_h(msp, P(-HANDLE_W / 2, 0)[0], P(HANDLE_W / 2, 0)[0], P(0, R + HANDLE_L)[1] + 8, f"{HANDLE_W}")

    roughness(msp, P(-R * 0.7, R * 0.55)[0], P(-R * 0.7, R * 0.55)[1], "Ra1.6")
    T(msp, "上游面（迎流）", 3.5, (cx, cy + R * sc + HANDLE_L * sc + 28), TextEntityAlignment.BOTTOM_CENTER)
    T(msp, "主视 比例 1:2", 2.8, (cx, oy + 78), TextEntityAlignment.BOTTOM_CENTER)

    # A-A 剖视 2:1
    sc2 = 2.0
    px = ox + 300
    py = oy + 155

    def Q(x, y):
        return (px + x * sc2, py + y * sc2)

    E, e = PLATE_E, PLATE_E_EDGE
    bev = E - e
    # 板外形（只画中心附近高度）
    hshow = 90.0
    rect(msp, Q(0, -hshow)[0], Q(0, -hshow)[1], Q(E, hshow)[0], Q(E, hshow)[1], "轮廓", LW_C)
    # 孔
    L(msp, Q(0, r), Q(e, r), "轮廓", LW_C)
    L(msp, Q(0, -r), Q(e, -r), "轮廓", LW_C)
    L(msp, Q(e, r), Q(E, r + bev), "轮廓", LW_C)
    L(msp, Q(e, -r), Q(E, -r - bev), "轮廓", LW_C)
    L(msp, Q(E, r + bev), Q(E, -r - bev), "轮廓", LW_C)
    L(msp, Q(0, r), Q(0, -r), "轮廓", LW_C)
    L(msp, Q(-8, 0), Q(E + 8, 0), "中心线", LW_F, "CENTER")
    # 剖面线（下半）
    x0, y0 = Q(0, -hshow)
    x1, y1 = Q(E, 0)
    # simple hatch
    yy = y1
    while yy > y0:
        L(msp, (x0, yy), (x1, yy - (x1 - x0)), "剖面线", LW_H)
        yy -= 4.0

    dim_h(msp, Q(0, 0)[0], Q(E, 0)[0], Q(0, -hshow)[1] - 14, f"E={E}")
    dim_h(msp, Q(0, 0)[0], Q(e, 0)[0], Q(0, r)[1] + 18, f"e={e}")
    T(msp, f"{BEVEL}°", 3.0, Q(e + bev * 0.5, r + bev + 6), TextEntityAlignment.BOTTOM_CENTER, "标注")
    dim_v(msp, Q(E, 0)[0] + 14, Q(0, -r)[1], Q(0, r)[1], f"Φ{BORE_D}", 1)
    roughness(msp, Q(-6, r + 8)[0], Q(-6, r + 8)[1], "Ra0.8")
    T(msp, "A—A  比例 2:1（下游倒角）", 3.2, (px + E * sc2 / 2, py + hshow * sc2 + 20), TextEntityAlignment.BOTTOM_CENTER)
    T(msp, "入口锐边 G≤0.0004d，禁止倒钝/倒圆", 2.6, (px + E * sc2 / 2, oy + 88), TextEntityAlignment.BOTTOM_CENTER)

    # 技术要求（本零件）
    req = [
        "零件技术要求：",
        f"1. 材料 {MAT}，板材或锻件，交货态固溶。",
        f"2. 孔径 Φ{BORE_D}{BORE_TOL}（20℃）；外径 Φ{PLATE_OD}{OD_TOL}。",
        "3. 上游面平面度 0.01；粗糙度如图。孔口圆柱度 0.01。",
        "4. 下游倒角 45°，孔口圆柱段厚度 e 如图；锐边保持。",
        f"5. 手柄刻印：{TAG} / DN{DN} / UP / d={BORE_D} / 流向箭头。",
        "6. 去毛刺，锐边倒钝除外；清洗洁净度按仪表管线。",
        "7. 件数：1。",
    ]
    for i, line in enumerate(req):
        T(msp, line, 2.5 if i else 3.0, (ox + 20, oy + 70 - i * 6.5), TextEntityAlignment.TOP_LEFT)


# ---------- 第3张：取压法兰 ----------
def draw_sheet3(msp):
    ox, oy = sheet_origin(2)
    title_block(msp, ox, oy, 3, 4, "取压法兰 机加工图", "1:3", f"{DWG_NO}-1/2")

    sc = 1 / 3.0
    bx = ox + 40
    by = oy + 150

    def S(x, y):
        return (bx + x * sc, by + y * sc)

    neck = FL_H - FL_C
    # 半剖主视
    # 法兰盘
    rect(msp, S(0, -FL_OD / 2)[0], S(0, -FL_OD / 2)[1], S(FL_C, FL_OD / 2)[0], S(FL_C, FL_OD / 2)[1], "轮廓", LW_C)
    L(msp, S(0, METER_ID / 2), S(FL_C, METER_ID / 2), "细实线", LW_F)
    L(msp, S(0, -METER_ID / 2), S(FL_C, -METER_ID / 2), "细实线", LW_F)
    L(msp, S(FL_C - FL_RF_H, FL_RF / 2), S(FL_C, FL_RF / 2), "细实线", LW_F)
    L(msp, S(FL_C - FL_RF_H, -FL_RF / 2), S(FL_C, -FL_RF / 2), "细实线", LW_F)
    # 颈
    L(msp, S(-neck, FL_NECK / 2), S(0, FL_NECK / 2), "轮廓", LW_C)
    L(msp, S(-neck, -FL_NECK / 2), S(0, -FL_NECK / 2), "轮廓", LW_C)
    L(msp, S(-neck, METER_ID / 2), S(0, METER_ID / 2), "虚线", LW_F, "DASHED")
    L(msp, S(-neck, -METER_ID / 2), S(0, -METER_ID / 2), "虚线", LW_F, "DASHED")
    L(msp, S(-neck, PIPE_OD / 2), S(-neck - 10, PIPE_OD / 2), "轮廓", LW_C)
    L(msp, S(-neck, -PIPE_OD / 2), S(-neck - 10, -PIPE_OD / 2), "轮廓", LW_C)
    L(msp, S(-neck - 15, 0), S(FL_C + 20, 0), "中心线", LW_F, "CENTER")

    # 取压孔
    tap_from_rf = TAP_OFF - GASKET_T
    ax = FL_C - tap_from_rf
    L(msp, S(ax, METER_ID / 2), S(ax, FL_OD / 2), "虚线", LW_F, "DASHED")
    L(msp, S(ax - TAP_HOLE / 2, METER_ID / 2), S(ax - TAP_HOLE / 2, FL_OD / 2 + 3), "细实线", LW_F)
    L(msp, S(ax + TAP_HOLE / 2, METER_ID / 2), S(ax + TAP_HOLE / 2, FL_OD / 2 + 3), "细实线", LW_F)
    # 取压管
    rect(msp, S(ax - TAP_OD / 2, FL_OD / 2)[0], S(ax - TAP_OD / 2, FL_OD / 2)[1],
         S(ax + TAP_OD / 2, FL_OD / 2 + TAP_L)[0], S(ax + TAP_OD / 2, FL_OD / 2 + TAP_L)[1], "轮廓", LW_C)

    dim_h(msp, S(0, 0)[0], S(FL_C, 0)[0], S(0, -FL_OD / 2)[1] - 16, f"C={FL_C}")
    dim_h(msp, S(-neck, 0)[0], S(FL_C, 0)[0], S(0, -FL_OD / 2)[1] - 32, f"H={FL_H}")
    dim_h(msp, S(ax, 0)[0], S(FL_C, 0)[0], S(0, FL_OD / 2 + TAP_L)[1] + 12, f"{tap_from_rf:.1f}")
    dim_v(msp, S(FL_C, 0)[0] + 14, S(0, -FL_OD / 2)[1], S(0, FL_OD / 2)[1], f"Φ{int(FL_OD)}", 1)
    dim_v(msp, S(-neck, 0)[0] - 12, S(0, -PIPE_OD / 2)[1], S(0, PIPE_OD / 2)[1], f"Φ{PIPE_OD}", -1)
    T(msp, f"取压孔Φ{TAP_HOLE}", 2.6, S(ax + 12, FL_OD / 4), TextEntityAlignment.LEFT, "标注")
    T(msp, f"装配后距孔板面{TAP_OFF}±{TAP_TOL}", 2.5, S(ax, FL_OD / 2 + TAP_L + 22), TextEntityAlignment.BOTTOM_CENTER, "标注")
    T(msp, "半剖主视（密封面朝右=孔板侧）", 3.0, (S(FL_C / 2, 0)[0], oy + 78), TextEntityAlignment.BOTTOM_CENTER)

    # 密封面视
    cx = ox + 300
    cy = oy + 155
    scf = 1 / 3.5
    C(msp, (cx, cy), FL_OD / 2 * scf, "轮廓", LW_C)
    C(msp, (cx, cy), FL_RF / 2 * scf, "细实线", LW_F)
    C(msp, (cx, cy), METER_ID / 2 * scf, "轮廓", LW_C)
    C(msp, (cx, cy), FL_PCD / 2 * scf, "中心线", LW_F, "CENTER")
    for i in range(FL_N):
        ang = math.radians(90 + i * 360 / FL_N)
        C(msp, (cx + FL_PCD / 2 * scf * math.cos(ang), cy + FL_PCD / 2 * scf * math.sin(ang)), FL_HOLE / 2 * scf, "细实线", LW_F)
    C(msp, (cx, cy + (METER_ID + FL_OD) / 4 * scf), TAP_HOLE / 2 * scf + 1.2, "轮廓", LW_C)
    L(msp, (cx - FL_OD / 2 * scf - 10, cy), (cx + FL_OD / 2 * scf + 10, cy), "中心线", LW_F, "CENTER")
    L(msp, (cx, cy - FL_OD / 2 * scf - 10), (cx, cy + FL_OD / 2 * scf + 10), "中心线", LW_F, "CENTER")
    dim_h(msp, cx - FL_PCD / 2 * scf, cx + FL_PCD / 2 * scf, cy - FL_OD / 2 * scf - 16, f"Φ{int(FL_PCD)}")
    T(msp, f"{FL_N}×Φ{int(FL_HOLE)}  螺栓{FL_BOLT}", 2.6, (cx, cy - FL_OD / 2 * scf - 28), TextEntityAlignment.TOP_CENTER, "标注")
    T(msp, f"RF Φ{int(FL_RF)}×{FL_RF_H}", 2.6, (cx, cy + FL_OD / 2 * scf + 14), TextEntityAlignment.BOTTOM_CENTER, "标注")
    T(msp, "密封面视", 3.0, (cx, oy + 78), TextEntityAlignment.BOTTOM_CENTER)

    req = [
        "零件技术要求：",
        f"1. 法兰按 HG/T20592-2009 PN25 DN{DN} 带颈对焊 RF；材料 {MAT}。",
        f"2. 颈部内径与管道内径对齐 D={METER_ID}；焊端 Φ{PIPE_OD}×{PIPE_WALL}。",
        f"3. 法兰取压：孔轴线距密封面 {tap_from_rf:.1f}（垫片{GASKET_T}），保证装后距孔板面 {TAP_OFF}±{TAP_TOL}。",
        f"4. 取压管 DN15 Φ{TAP_OD}×{TAP_WALL} 与法兰外圆焊接，坡口/焊脚按 WPS；内孔与取压孔贯通无毛刺。",
        "5. 上/下游法兰各 1 件，取压方位对称；螺栓孔可配钻。",
        "6. RF 密封面粗糙度 Ra3.2；其余非加工面保留。",
        "7. 件数：上游1 + 下游1。",
    ]
    for i, line in enumerate(req):
        T(msp, line, 2.4 if i else 3.0, (ox + 18, oy + 68 - i * 6.2), TextEntityAlignment.TOP_LEFT)


# ---------- 第4张：取压管 + 短节 ----------
def draw_sheet4(msp):
    ox, oy = sheet_origin(3)
    title_block(msp, ox, oy, 4, 4, "取压管 / 短节 机加工图", "2:1 / 1:2", f"{DWG_NO}-4/5")

    # 取压管 2:1
    sc = 2.0
    x0, y0 = ox + 50, oy + 180
    tap_len = TAP_L
    od, w = TAP_OD, TAP_WALL
    id_ = od - 2 * w
    rect(msp, x0, y0 - od * sc / 2, x0 + tap_len * sc, y0 + od * sc / 2, "轮廓", LW_C)
    L(msp, (x0, y0 - id_ * sc / 2), (x0 + tap_len * sc, y0 - id_ * sc / 2), "虚线", LW_F, "DASHED")
    L(msp, (x0, y0 + id_ * sc / 2), (x0 + tap_len * sc, y0 + id_ * sc / 2), "虚线", LW_F, "DASHED")
    L(msp, (x0 - 8, y0), (x0 + tap_len * sc + 8, y0), "中心线", LW_F, "CENTER")
    # 坡口
    for x, sgn in ((x0, 1), (x0 + tap_len * sc, -1)):
        L(msp, (x, y0 - od * sc / 2), (x + sgn * 5, y0 - id_ * sc / 2), "轮廓", LW_C)
        L(msp, (x, y0 + od * sc / 2), (x + sgn * 5, y0 + id_ * sc / 2), "轮廓", LW_C)
    dim_h(msp, x0, x0 + tap_len * sc, y0 - od * sc / 2 - 14, f"L={TAP_L}")
    dim_v(msp, x0 + tap_len * sc + 12, y0 - od * sc / 2, y0 + od * sc / 2, f"Φ{TAP_OD}×{TAP_WALL}", 1)
    T(msp, f"取压管  DN15(1/2\")  BW  {MAT}  件数2  比例2:1", 3.2, (x0 + tap_len * sc / 2, y0 + od * sc / 2 + 18), TextEntityAlignment.BOTTOM_CENTER)
    T(msp, "一端焊法兰，一端接仪表阀/管件；坡口 GB/T985.1", 2.5, (x0 + tap_len * sc / 2, y0 - od * sc / 2 - 28), TextEntityAlignment.TOP_CENTER)

    # 短节 1:2
    sc2 = 0.5
    x1, y1 = ox + 50, oy + 100
    rect(msp, x1, y1 - PIPE_OD * sc2 / 2, x1 + STUB_L * sc2, y1 + PIPE_OD * sc2 / 2, "轮廓", LW_C)
    L(msp, (x1, y1 - METER_ID * sc2 / 2), (x1 + STUB_L * sc2, y1 - METER_ID * sc2 / 2), "虚线", LW_F, "DASHED")
    L(msp, (x1, y1 + METER_ID * sc2 / 2), (x1 + STUB_L * sc2, y1 + METER_ID * sc2 / 2), "虚线", LW_F, "DASHED")
    L(msp, (x1 - 10, y1), (x1 + STUB_L * sc2 + 10, y1), "中心线", LW_F, "CENTER")
    dim_h(msp, x1, x1 + STUB_L * sc2, y1 - PIPE_OD * sc2 / 2 - 14, f"L={STUB_L}")
    dim_v(msp, x1 + STUB_L * sc2 + 14, y1 - PIPE_OD * sc2 / 2, y1 + PIPE_OD * sc2 / 2, f"Φ{PIPE_OD}×{PIPE_WALL}", 1)
    T(msp, f"短节  {MAT}  件数2  比例1:2  （两端 BW 接法兰颈/工艺管线）", 3.2, (x1 + STUB_L * sc2 / 2, y1 + PIPE_OD * sc2 / 2 + 16), TextEntityAlignment.BOTTOM_CENTER)

    req = [
        "说明：",
        "1. 取压管、短节材料与法兰同炉号/同牌号为宜。",
        "2. 深冷不锈钢焊后酸洗钝化；焊缝 PT/RT 按业主规格。",
        "3. 本套装置为流量测量孔板（非限流孔板），孔径与锐边按计量标准执行。",
        f"4. 配套计算书：{TAG}.RO  S/N {SERIAL}  β={BETA}  D={METER_ID}。",
    ]
    for i, line in enumerate(req):
        T(msp, line, 2.5 if i else 3.0, (ox + 20, oy + 55 - i * 7), TextEntityAlignment.TOP_LEFT)


def build_dxf() -> Path:
    doc = setup_doc()
    msp = doc.modelspace()
    draw_sheet1(msp)
    draw_sheet2(msp)
    draw_sheet3(msp)
    draw_sheet4(msp)
    zoom.extents(msp)
    DXF_DIR.mkdir(parents=True, exist_ok=True)
    path = DXF_DIR / f"{TAG}_生产机加装配图_分张.dxf"
    doc.saveas(path)
    return path


def export_vector_pdf(dxf_path: Path, pdf_path: Path):
    """每张 A3 单独渲染为矢量 PDF 页（非 PNG 转 PDF）"""
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_pdf import PdfPages
    from ezdxf.addons.drawing import RenderContext, Frontend
    from ezdxf.addons.drawing.matplotlib import MatplotlibBackend
    from ezdxf.addons.drawing.config import Configuration, ColorPolicy, BackgroundPolicy
    from ezdxf.addons.drawing.properties import LayoutProperties

    plt.rcParams["font.sans-serif"] = ["SimHei", "Microsoft YaHei", "SimSun"]
    plt.rcParams["axes.unicode_minus"] = False

    doc = ezdxf.readfile(dxf_path)
    msp = doc.modelspace()
    ctx = RenderContext(doc)
    cfg = Configuration.defaults().with_changes(
        lineweight_scaling=0.9,
        min_lineweight=0.15,
        color_policy=ColorPolicy.BLACK,
        background_policy=BackgroundPolicy.WHITE,
    )

    with PdfPages(pdf_path) as pdf:
        for i in range(4):
            ox, oy = sheet_origin(i)
            fig = plt.figure(figsize=(16.54, 11.69))  # A3 inch
            ax = fig.add_axes([0, 0, 1, 1])
            props = LayoutProperties.from_layout(msp)
            props.set_colors("#FFFFFF", "#000000")
            Frontend(ctx, MatplotlibBackend(ax), config=cfg).draw_layout(
                msp, finalize=False, layout_properties=props
            )
            ax.set_xlim(ox - 2, ox + A3W + 2)
            ax.set_ylim(oy - 2, oy + A3H + 2)
            ax.set_aspect("equal")
            ax.set_axis_off()
            # 矢量 PDF（线条/文字以向量写入）
            pdf.savefig(fig, facecolor="white")
            plt.close(fig)
            print("page", i + 1)

    # 同步导出整卷预览 PNG（仅预览用）
    fig = plt.figure(figsize=(24, 6), dpi=160)
    ax = fig.add_axes([0.01, 0.01, 0.98, 0.98])
    props = LayoutProperties.from_layout(msp)
    props.set_colors("#FFFFFF", "#000000")
    Frontend(ctx, MatplotlibBackend(ax), config=cfg).draw_layout(
        msp, finalize=True, layout_properties=props
    )
    ax.set_aspect("equal")
    preview = OUT / f"预览_{TAG}_分张总览.png"
    fig.savefig(preview, dpi=160, facecolor="white", bbox_inches="tight")
    plt.close(fig)
    print("preview", preview)


def main():
    dxf = build_dxf()
    print("DXF", dxf)
    pdf = OUT / f"{TAG}_生产机加装配图.pdf"
    export_vector_pdf(dxf, pdf)
    print("PDF", pdf.resolve(), pdf.stat().st_size)


if __name__ == "__main__":
    main()
