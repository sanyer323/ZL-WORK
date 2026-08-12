# -*- coding: utf-8 -*-
"""
FE-1002 清洁版出图 — 严格分区，禁止叠字
A3 横图安全区约定（每张独立）：
  图框内边距 10
  标题栏：右下 190×50，任何几何/表格不得进入
  图形区：y >= oy+78
  表格区：仅左侧 x < ox+220，且 y 在 [oy+78, oy+120]
"""
from __future__ import annotations

import math
from pathlib import Path

import ezdxf
from ezdxf import units, zoom
from ezdxf.enums import TextEntityAlignment

TAG = "FE-1002"
SERIAL = "26031402"
MODEL = "ROH10xJX25N2"
DWG = "FE-1002-GA"
MAT = "F304/F304L"

DN, PIPE_OD, WALL = 250, 273.0, 4.0
D, d = 265.0, 136.18
BETA, FA = 0.5139, 0.9938
TF, PF = -162.0, 600.0

PL_OD, PL_E, PL_e = 320.0, 6.0, 2.5
HW, HL = 36.0, 50.0

FL_OD, PCD, HOLE_N, HOLE_D = 425.0, 370.0, 12, 30.0
FL_C, FL_H, FL_RF, FL_RF_H, FL_NECK = 32.0, 88.0, 335.0, 2.0, 298.0
BOLT = "M27"
GST, STUB, TAP_OFF, TAP_L = 2.0, 120.0, 25.4, 80.0
TAP_OD, TAP_W, TAP_HOLE = 21.3, 2.77, 8.0

OUT = Path(__file__).resolve().parent
DXF_DIR = OUT / "DXF"
A3W, A3H = 420.0, 297.0
M = 10.0
TB_W, TB_H = 190.0, 50.0
# 内容不得低于此 y（标题栏顶 + 间隙）
Y_MIN = M + TB_H + 8.0  # 68
LW_C, LW_F, LW_H = 50, 18, 13


def setup():
    doc = ezdxf.new("R2013", setup=True)
    doc.units = units.MM
    doc.header["$INSUNITS"] = 4
    for n, c, lw, lt in [
        ("轮廓", 7, LW_C, "Continuous"),
        ("细实线", 7, LW_F, "Continuous"),
        ("中心线", 1, LW_F, "CENTER"),
        ("虚线", 8, LW_F, "DASHED"),
        ("剖面线", 8, LW_H, "Continuous"),
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
    doc.styles.get("CN").dxf.font = "simhei.ttf"
    return doc


def T(msp, s, h, xy, align=TextEntityAlignment.LEFT, layer="文字"):
    t = msp.add_text(str(s), height=h, dxfattribs={"layer": layer, "style": "CN"})
    t.set_placement(xy, align=align)
    return t


def L(msp, a, b, layer="轮廓", lw=LW_C, lt="Continuous"):
    msp.add_line(a, b, dxfattribs={"layer": layer, "lineweight": lw, "linetype": lt})


def C(msp, c, r, layer="轮廓", lw=LW_C, lt="Continuous"):
    msp.add_circle(c, r, dxfattribs={"layer": layer, "lineweight": lw, "linetype": lt})


def box(msp, x0, y0, x1, y1, layer="轮廓", lw=LW_C):
    L(msp, (x0, y0), (x1, y0), layer, lw)
    L(msp, (x1, y0), (x1, y1), layer, lw)
    L(msp, (x1, y1), (x0, y1), layer, lw)
    L(msp, (x0, y1), (x0, y0), layer, lw)


def hatch(msp, x0, y0, x1, y1, step=3.5):
    if x0 > x1:
        x0, x1 = x1, x0
    if y0 > y1:
        y0, y1 = y1, y0
    if y1 - y0 < 0.5 or x1 - x0 < 0.5:
        return
    y = y0
    while y <= y1:
        # 45度短划：在水平扫描线上画斜线
        x = x0
        while x <= x1:
            x2 = min(x + step, x1)
            y2 = min(y + step, y1)
            L(msp, (x, y), (x2, y2), "剖面线", LW_H)
            x += step
        y += step


def dim_h(msp, x0, x1, y, label):
    L(msp, (x0, y), (x1, y), "标注", LW_F)
    for x in (x0, x1):
        L(msp, (x, y - 1.5), (x, y + 1.5), "标注", LW_F)
    T(msp, label, 2.2, ((x0 + x1) / 2, y + 2.0), TextEntityAlignment.BOTTOM_CENTER, "标注")


def dim_v(msp, x, y0, y1, label, side=-1):
    L(msp, (x, y0), (x, y1), "标注", LW_F)
    for y in (y0, y1):
        L(msp, (x - 1.5, y), (x + 1.5, y), "标注", LW_F)
    # 竖向尺寸用横排文字，避免旋转字体叠字
    T(msp, label, 2.0, (x + 5.0 * side, (y0 + y1) / 2), TextEntityAlignment.MIDDLE_CENTER, "标注")


def balloon(msp, x, y, bx, by, n):
    L(msp, (x, y), (bx, by), "标注", LW_F)
    C(msp, (bx, by), 3.8, "轮廓", LW_C)
    T(msp, str(n), 2.5, (bx, by), TextEntityAlignment.MIDDLE_CENTER)


def ox_of(i):
    return i * (A3W + 40.0)


def titleblock(msp, ox, oy, sheet, total, title, scale, dwg):
    """简洁标题栏：短字段，左对齐，防溢出"""
    box(msp, ox, oy, ox + A3W, oy + A3H, "图框", LW_C)
    box(msp, ox + M, oy + M, ox + A3W - M, oy + A3H - M, "图框", LW_F)

    tx0 = ox + A3W - M - TB_W
    ty0 = oy + M
    box(msp, tx0, ty0, tx0 + TB_W, ty0 + TB_H, "图框", LW_C)
    # 3 行
    L(msp, (tx0, ty0 + 16), (tx0 + TB_W, ty0 + 16), "图框", LW_F)
    L(msp, (tx0, ty0 + 33), (tx0 + TB_W, ty0 + 33), "图框", LW_F)
    L(msp, (tx0 + 70, ty0), (tx0 + 70, ty0 + TB_H), "图框", LW_F)
    L(msp, (tx0 + 130, ty0), (tx0 + 130, ty0 + TB_H), "图框", LW_F)

    # 全部 LEFT，短文本（中文）
    T(msp, "图名", 1.6, (tx0 + 2, ty0 + 45), TextEntityAlignment.LEFT, "图框")
    T(msp, title[:12], 2.4, (tx0 + 2, ty0 + 38), TextEntityAlignment.LEFT, "图框")
    T(msp, "比例", 1.6, (tx0 + 72, ty0 + 45), TextEntityAlignment.LEFT, "图框")
    T(msp, scale[:12], 2.2, (tx0 + 72, ty0 + 38), TextEntityAlignment.LEFT, "图框")
    T(msp, "张次", 1.6, (tx0 + 132, ty0 + 45), TextEntityAlignment.LEFT, "图框")
    T(msp, f"第{sheet}/{total}张", 2.2, (tx0 + 132, ty0 + 38), TextEntityAlignment.LEFT, "图框")

    T(msp, "图号", 1.6, (tx0 + 2, ty0 + 28), TextEntityAlignment.LEFT, "图框")
    T(msp, dwg[:18], 2.2, (tx0 + 2, ty0 + 21), TextEntityAlignment.LEFT, "图框")
    T(msp, "材料", 1.6, (tx0 + 72, ty0 + 28), TextEntityAlignment.LEFT, "图框")
    T(msp, MAT, 2.2, (tx0 + 72, ty0 + 21), TextEntityAlignment.LEFT, "图框")
    T(msp, "幅面", 1.6, (tx0 + 132, ty0 + 28), TextEntityAlignment.LEFT, "图框")
    T(msp, "A3", 2.2, (tx0 + 132, ty0 + 21), TextEntityAlignment.LEFT, "图框")

    T(msp, f"位号{TAG} 出厂号{SERIAL}", 1.9, (tx0 + 2, ty0 + 10), TextEntityAlignment.LEFT, "图框")
    T(msp, f"DN{DN} PN25", 2.0, (tx0 + 72, ty0 + 10), TextEntityAlignment.LEFT, "图框")
    T(msp, "单位mm", 1.9, (tx0 + 132, ty0 + 10), TextEntityAlignment.LEFT, "图框")
    T(msp, "设计", 1.6, (tx0 + 2, ty0 + 3), TextEntityAlignment.LEFT, "图框")
    T(msp, "校核", 1.6, (tx0 + 72, ty0 + 3), TextEntityAlignment.LEFT, "图框")

    T(msp, f"{TAG}  {title}", 3.8, (ox + M + 2, oy + A3H - M - 6), TextEntityAlignment.LEFT)
    return oy + Y_MIN  # 内容下限


def simple_table(msp, x, y_top, headers, rows, widths, row_h=6.0, fs=1.8):
    """表格向下画；单元格文字截断，左对齐+内边距"""
    data = [headers] + rows
    yy = y_top
    for i, row in enumerate(data):
        xx = x
        for j, cell in enumerate(row):
            w = widths[j]
            box(msp, xx, yy - row_h, xx + w, yy, "表格", LW_F)
            # 按列宽估算可容纳字符（约 1.7mm/字符 @fs1.8）
            maxlen = max(3, int(w / (fs * 1.15)) - 1)
            txt = str(cell)[:maxlen]
            T(msp, txt, fs if i else fs + 0.15, (xx + 1.5, yy - row_h / 2), TextEntityAlignment.MIDDLE_LEFT, "表格")
            xx += w
        yy -= row_h
    return yy


# ---------- Sheet 1：总装（稀疏） ----------
def sheet1(msp):
    ox, oy = ox_of(0), 0.0
    y_floor = titleblock(msp, ox, oy, 1, 3, "总装配图", "1:4", f"{DWG}-01")

    # 图形只在上半：中心约 y=190，比例 1:4，法兰半高 212 → 显示半高 53，底部约 137 > 68 OK
    sc = 0.25
    bx, by = ox + 30, oy + 195

    def S(X, Y):
        return (bx + X * sc, by + Y * sc)

    neck = FL_H - FL_C
    g, H = GST, PL_E
    stub = STUB

    # X 链（真实）
    x0 = 0.0
    x_s1 = stub
    x_hub1 = x_s1
    x_back1 = x_hub1 + neck
    x_face1 = x_back1 + FL_C
    x_pl = x_face1 + g
    x_face2 = x_pl + H + g
    x_back2 = x_face2 + FL_C
    x_hub2 = x_back2 + neck
    x_end = x_hub2 + stub

    L(msp, S(x0 - 20, 0), S(x_end + 20, 0), "中心线", LW_F, "CENTER")

    def pipe(a, b):
        L(msp, S(a, PIPE_OD / 2), S(b, PIPE_OD / 2), "轮廓", LW_C)
        L(msp, S(a, -PIPE_OD / 2), S(b, -PIPE_OD / 2), "轮廓", LW_C)
        L(msp, S(a, D / 2), S(b, D / 2), "虚线", LW_F, "DASHED")
        L(msp, S(a, -D / 2), S(b, -D / 2), "虚线", LW_F, "DASHED")
        hatch(msp, S(a, -PIPE_OD / 2)[0], S(a, -PIPE_OD / 2)[1], S(b, -D / 2)[0], S(b, -D / 2)[1], 4)

    pipe(x0, x_s1)
    pipe(x_hub2, x_end)

    def fl(x_face, facing):
        s = 1 if facing > 0 else -1
        x_back = x_face - s * FL_C
        x_hub = x_back - s * neck
        # 上半折线
        pts = [
            S(x_face, FL_RF / 2),
            S(x_face, FL_OD / 2),
            S(x_back, FL_OD / 2),
            S(x_back, FL_NECK / 2),
            S(x_hub + s * 15, FL_NECK / 2),
            S(x_hub, PIPE_OD / 2),
        ]
        for a, b in zip(pts, pts[1:]):
            L(msp, a, b, "轮廓", LW_C)
        pts = [
            S(x_face, -FL_RF / 2),
            S(x_face, -FL_OD / 2),
            S(x_back, -FL_OD / 2),
            S(x_back, -FL_NECK / 2),
            S(x_hub + s * 15, -FL_NECK / 2),
            S(x_hub, -PIPE_OD / 2),
        ]
        for a, b in zip(pts, pts[1:]):
            L(msp, a, b, "轮廓", LW_C)
        L(msp, S(x_face, FL_RF / 2), S(x_face, -FL_RF / 2), "轮廓", LW_C)
        L(msp, S(x_hub, D / 2), S(x_face, D / 2), "细实线", LW_F)
        L(msp, S(x_hub, -D / 2), S(x_face, -D / 2), "细实线", LW_F)
        xa = min(S(x_face, 0)[0], S(x_back, 0)[0])
        xb = max(S(x_face, 0)[0], S(x_back, 0)[0])
        hatch(msp, xa, S(0, -FL_OD / 2)[1], xb, S(0, -D / 2)[1], 4)

    fl(x_face1, +1)
    fl(x_face2, -1)

    # 垫片+孔板
    for xa in (x_face1, x_face2 - g):
        box(msp, S(xa, -FL_RF / 2)[0], S(xa, -FL_RF / 2)[1], S(xa + g, FL_RF / 2)[0], S(xa + g, FL_RF / 2)[1], "细实线", LW_F)
    box(msp, S(x_pl, -PL_OD / 2)[0], S(x_pl, -PL_OD / 2)[1], S(x_pl + H, PL_OD / 2)[0], S(x_pl + H, PL_OD / 2)[1], "轮廓", LW_C)
    br = d / 2
    L(msp, S(x_pl, br), S(x_pl + PL_e, br), "轮廓", LW_C)
    L(msp, S(x_pl, -br), S(x_pl + PL_e, -br), "轮廓", LW_C)
    L(msp, S(x_pl + PL_e, br), S(x_pl + H, br + (PL_E - PL_e)), "轮廓", LW_C)
    L(msp, S(x_pl + PL_e, -br), S(x_pl + H, -br - (PL_E - PL_e)), "轮廓", LW_C)
    L(msp, S(x_pl + H, br + (PL_E - PL_e)), S(x_pl + H, -br - (PL_E - PL_e)), "轮廓", LW_C)
    hatch(msp, S(x_pl, -PL_OD / 2)[0], S(x_pl, -PL_OD / 2)[1], S(x_pl + H, 0)[0], by - 1, 3)

    # 手柄（短）
    hx = x_pl + H / 2
    L(msp, S(hx, PL_OD / 2), S(hx, PL_OD / 2 + 18), "轮廓", LW_C)
    box(
        msp,
        S(hx - HW / 2, PL_OD / 2 + 18)[0],
        S(hx - HW / 2, PL_OD / 2 + 18)[1],
        S(hx + HW / 2, PL_OD / 2 + 40)[0],
        S(hx + HW / 2, PL_OD / 2 + 40)[1],
        "轮廓",
        LW_C,
    )

    # 取压管（短）
    for ax in (x_pl - TAP_OFF, x_pl + H + TAP_OFF):
        L(msp, S(ax - TAP_OD / 2, FL_OD / 2), S(ax - TAP_OD / 2, FL_OD / 2 + TAP_L), "轮廓", LW_C)
        L(msp, S(ax + TAP_OD / 2, FL_OD / 2), S(ax + TAP_OD / 2, FL_OD / 2 + TAP_L), "轮廓", LW_C)
        L(msp, S(ax - TAP_OD / 2, FL_OD / 2 + TAP_L), S(ax + TAP_OD / 2, FL_OD / 2 + TAP_L), "轮廓", LW_C)
        L(msp, S(ax, FL_OD / 2), S(ax, D / 2), "虚线", LW_F, "DASHED")

    # 螺柱示意
    yb = PCD / 2 * 0.85
    L(msp, S(x_face1 - FL_C + 5, yb), S(x_face2 + FL_C - 5, yb), "轮廓", LW_C)
    L(msp, S(x_face1 - FL_C + 5, -yb), S(x_face2 + FL_C - 5, -yb), "细实线", LW_F)

    # 少量尺寸（图形下方空白，y 仍 > floor）
    dim_v(msp, S(x0 - 18, 0)[0], S(0, -FL_OD / 2)[1], S(0, FL_OD / 2)[1], f"Φ{int(FL_OD)}", -1)
    T(msp, f"Φ{PIPE_OD}×{WALL}", 2.0, S((x0 + x_s1) / 2, PIPE_OD / 2 + 8), TextEntityAlignment.BOTTOM_CENTER, "标注")
    T(msp, f"d=Φ{d}", 2.0, S(x_pl + H + 14, 40), TextEntityAlignment.LEFT, "标注")
    T(msp, "介质流向 →", 2.2, S((x_face1 + x_face2) / 2, -FL_OD / 2 - 18), TextEntityAlignment.TOP_CENTER, "标注")
    T(msp, "剖视（上半外形 / 下半剖视）", 2.0, (bx + (x_end * sc) / 2, by + FL_OD / 2 * sc + 28), TextEntityAlignment.BOTTOM_CENTER)

    # 球标分散，避免引线交叉
    balloon(msp, *S(x_face1 - FL_C / 2, -FL_OD / 2), ox + 255, oy + 155, "1")
    balloon(msp, *S(x_face2 + FL_C / 2, -FL_OD / 2), ox + 285, oy + 155, "2")
    balloon(msp, *S(x_pl + H / 2, PL_OD / 2), ox + 270, oy + 250, "3")
    balloon(msp, *S(x_pl - TAP_OFF, FL_OD / 2 + TAP_L), ox + 230, oy + 250, "4")
    balloon(msp, *S(x_pl + H + TAP_OFF, FL_OD / 2 + TAP_L), ox + 300, oy + 250, "5")

    # 右侧说明（短行，不进标题栏）
    rx, ry = ox + 300, oy + 250
    T(msp, "技术要求", 2.4, (rx, ry), TextEntityAlignment.LEFT)
    notes = [
        f"1. 标准 GB/T2624.2 法兰取压",
        f"2. 取压距孔板面 {TAP_OFF}±0.8",
        f"3. 介质 LNG {TF}℃ / {PF} kPaG",
        f"4. β={BETA}  膨胀系数Fa={FA}",
        f"5. 型号 {MODEL}",
    ]
    for i, s in enumerate(notes):
        T(msp, s, 1.9, (rx, ry - 12 - i * 8), TextEntityAlignment.LEFT)

    # 明细表：左侧，全部在 y_floor 以上
    simple_table(
        msp,
        ox + 12,
        oy + 115,
        ["序号", "数量", "名称及规格", "材料", "备注"],
        [
            ["1", "1", "上游取压法兰 WN RF PN25", MAT, "HG/T20592"],
            ["2", "1", "下游取压法兰 WN RF", MAT, "镜像"],
            ["3", "1", f"孔板片 Φ{PL_OD}×{PL_E}", MAT, f"d={d}"],
            ["4", "2", f"取压管 DN15 L={TAP_L}", MAT, "对焊"],
            ["5", f"{HOLE_N}", f"螺柱{BOLT}+螺母", "B8M", "-"],
            ["6", "2", "缠绕垫 PN25 RF", "304+石墨", "深冷"],
            ["7", "2", f"短节 Φ{PIPE_OD}×{WALL}", MAT, f"L={STUB}"],
        ],
        [16, 16, 95, 32, 40],
        row_h=5.5,
        fs=1.7,
    )
    T(msp, "明细表", 2.2, (ox + 12, oy + 118), TextEntityAlignment.LEFT)


# ---------- Sheet 2：孔板 ----------
def sheet2(msp):
    ox, oy = ox_of(1), 0.0
    y_floor = titleblock(msp, ox, oy, 2, 3, "孔板片", "1:2", f"{DWG}-02")

    # 主视 1:2，中心高位
    sc = 0.45
    cx, cy = ox + 130, oy + 185

    def P(x, y):
        return (cx + x * sc, cy + y * sc)

    R, r = PL_OD / 2, d / 2
    C(msp, (cx, cy), R * sc, "轮廓", LW_C)
    C(msp, (cx, cy), r * sc, "轮廓", LW_C)
    L(msp, P(-R - 10, 0), P(R + 10, 0), "中心线", LW_F, "CENTER")
    L(msp, P(0, -R - 10), P(0, R + HL + 2), "中心线", LW_F, "CENTER")
    box(msp, P(-HW / 2, R)[0], P(-HW / 2, R)[1], P(HW / 2, R + HL)[0], P(HW / 2, R + HL)[1], "轮廓", LW_C)
    T(msp, TAG, 2.2, P(0, R + HL * 0.55), TextEntityAlignment.MIDDLE_CENTER)
    T(msp, "上游", 1.8, P(0, R + HL * 0.25), TextEntityAlignment.MIDDLE_CENTER)

    dim_h(msp, P(-R, 0)[0], P(R, 0)[0], P(0, -R)[1] - 12, f"Φ{PL_OD}")
    # 孔径标注放在圆外上方，避开十字中心线
    dim_h(msp, P(-r, 0)[0], P(r, 0)[0], P(0, R)[1] + 8, f"Φ{d}±0.05")
    T(msp, f"手柄 {HL}×{HW}", 1.9, P(HW / 2 + 8, R + HL * 0.5), TextEntityAlignment.LEFT, "标注")
    T(msp, "主视（上游面）比例1:2", 2.0, (cx, P(0, -R)[1] - 24), TextEntityAlignment.TOP_CENTER)

    # 孔口局部放大
    sc2 = 3.0
    px, py = ox + 295, oy + 190
    E, e = PL_E, PL_e
    h = 8.0
    y1 = h * sc2
    box(msp, px, py - y1, px + E * sc2, py + y1, "轮廓", LW_C)
    yb = 3.0 * sc2
    L(msp, (px, py + yb), (px + e * sc2, py + yb), "轮廓", LW_C)
    L(msp, (px, py - yb), (px + e * sc2, py - yb), "轮廓", LW_C)
    L(msp, (px + e * sc2, py + yb), (px + E * sc2, py + yb + (E - e) * sc2), "轮廓", LW_C)
    L(msp, (px + e * sc2, py - yb), (px + E * sc2, py - yb - (E - e) * sc2), "轮廓", LW_C)
    L(msp, (px + E * sc2, py + yb + (E - e) * sc2), (px + E * sc2, py - yb - (E - e) * sc2), "轮廓", LW_C)
    L(msp, (px - 3, py), (px + E * sc2 + 3, py), "中心线", LW_F, "CENTER")
    hatch(msp, px, py - y1, px + E * sc2, py - 0.5, 2.2)
    dim_h(msp, px, px + E * sc2, py - y1 - 7, f"E={E}")
    # e 标注放在图形上方空白，不进剖面线
    dim_h(msp, px, px + e * sc2, py + y1 + 6, f"e={e}")
    T(msp, "45°", 1.9, (px + E * sc2 + 3, py + 2), TextEntityAlignment.LEFT, "标注")
    T(msp, "孔口局部 3:1", 2.0, (px + E * sc2 / 2, py + y1 + 16), TextEntityAlignment.BOTTOM_CENTER)
    T(msp, "入口锐边保持", 1.8, (px + E * sc2 / 2, py - y1 - 14), TextEntityAlignment.TOP_CENTER)

    # 刻印/注释表（左侧低位，高于 floor）
    T(msp, "刻印与技术说明", 2.2, (ox + 12, oy + 118), TextEntityAlignment.LEFT)
    simple_table(
        msp,
        ox + 12,
        oy + 112,
        ["项目", "内容"],
        [
            ["位号", TAG],
            ["孔径d", str(d)],
            ["外径", str(PL_OD)],
            ["板厚E", str(PL_E)],
            ["孔口e", str(PL_e)],
            ["材料", MAT],
            ["件数", "1"],
            ["表面", "Ra1.6"],
        ],
        [45, 55],
        row_h=5.2,
        fs=1.7,
    )


# ---------- Sheet 3：法兰+取压管 ----------
def sheet3(msp):
    ox, oy = ox_of(2), 0.0
    y_floor = titleblock(msp, ox, oy, 3, 3, "取压法兰", "1:4", f"{DWG}-03")

    sc = 0.28
    bx, by = ox + 40, oy + 195
    neck = FL_H - FL_C

    def S(x, y):
        return (bx + x * sc, by + y * sc)

    x_face, x_back, x_hub = FL_C, 0.0, -neck
    pts = [
        S(x_face, FL_RF / 2),
        S(x_face, FL_OD / 2),
        S(x_back, FL_OD / 2),
        S(x_back, FL_NECK / 2),
        S(x_hub + 12, FL_NECK / 2),
        S(x_hub, PIPE_OD / 2),
    ]
    for a, b in zip(pts, pts[1:]):
        L(msp, a, b, "轮廓", LW_C)
    pts = [
        S(x_face, -FL_RF / 2),
        S(x_face, -FL_OD / 2),
        S(x_back, -FL_OD / 2),
        S(x_back, -FL_NECK / 2),
        S(x_hub + 12, -FL_NECK / 2),
        S(x_hub, -PIPE_OD / 2),
    ]
    for a, b in zip(pts, pts[1:]):
        L(msp, a, b, "轮廓", LW_C)
    L(msp, S(x_face, FL_RF / 2), S(x_face, -FL_RF / 2), "轮廓", LW_C)
    L(msp, S(x_hub, D / 2), S(x_face, D / 2), "细实线", LW_F)
    L(msp, S(x_hub, -D / 2), S(x_face, -D / 2), "细实线", LW_F)
    L(msp, S(x_hub - 10, 0), S(x_face + 15, 0), "中心线", LW_F, "CENTER")
    hatch(msp, S(x_back, -FL_OD / 2)[0], S(0, -FL_OD / 2)[1], S(x_face, -D / 2)[0], S(0, -D / 2)[1], 4)

    ax = x_face - (TAP_OFF - GST)
    L(msp, S(ax, D / 2), S(ax, FL_OD / 2), "虚线", LW_F, "DASHED")
    box(
        msp,
        S(ax - TAP_OD / 2, FL_OD / 2)[0],
        S(ax - TAP_OD / 2, FL_OD / 2)[1],
        S(ax + TAP_OD / 2, FL_OD / 2 + TAP_L)[0],
        S(ax + TAP_OD / 2, FL_OD / 2 + TAP_L)[1],
        "轮廓",
        LW_C,
    )

    dim_h(msp, S(x_back, 0)[0], S(x_face, 0)[0], S(0, -FL_OD / 2)[1] - 10, f"C={FL_C}")
    dim_h(msp, S(x_hub, 0)[0], S(x_face, 0)[0], S(0, -FL_OD / 2)[1] - 22, f"H={FL_H}")
    dim_h(msp, S(ax, 0)[0], S(x_face, 0)[0], S(0, FL_OD / 2 + TAP_L)[1] + 8, f"{TAP_OFF - GST:.1f}")
    dim_v(msp, S(x_face, 0)[0] + 10, S(0, -FL_OD / 2)[1], S(0, FL_OD / 2)[1], f"Φ{int(FL_OD)}", 1)
    T(msp, "半剖主视 1:4", 2.0, (S(FL_C / 2, 0)[0], S(0, -FL_OD / 2)[1] - 34), TextEntityAlignment.TOP_CENTER)

    # 密封面视（右侧，不碰到标题栏）
    cx, cy = ox + 300, oy + 195
    scf = 0.28
    C(msp, (cx, cy), FL_OD / 2 * scf, "轮廓", LW_C)
    C(msp, (cx, cy), FL_RF / 2 * scf, "细实线", LW_F)
    C(msp, (cx, cy), D / 2 * scf, "轮廓", LW_C)
    C(msp, (cx, cy), PCD / 2 * scf, "中心线", LW_F, "CENTER")
    for i in range(HOLE_N):
        ang = math.radians(90 + i * 360 / HOLE_N)
        C(msp, (cx + PCD / 2 * scf * math.cos(ang), cy + PCD / 2 * scf * math.sin(ang)), HOLE_D / 2 * scf, "细实线", LW_F)
    L(msp, (cx - FL_OD / 2 * scf - 6, cy), (cx + FL_OD / 2 * scf + 6, cy), "中心线", LW_F, "CENTER")
    L(msp, (cx, cy - FL_OD / 2 * scf - 6), (cx, cy + FL_OD / 2 * scf + 6), "中心线", LW_F, "CENTER")
    dim_h(msp, cx - PCD / 2 * scf, cx + PCD / 2 * scf, cy - FL_OD / 2 * scf - 10, f"Φ{int(PCD)}")
    T(msp, f"{HOLE_N}×Φ{int(HOLE_D)} {BOLT}", 1.9, (cx, cy - FL_OD / 2 * scf - 20), TextEntityAlignment.TOP_CENTER, "标注")
    T(msp, "密封面视", 2.0, (cx, cy + FL_OD / 2 * scf + 10), TextEntityAlignment.BOTTOM_CENTER)

    # 取压管小图（中下，高于 floor）
    x0, y0 = ox + 30, oy + 105
    sc2 = 1.5
    box(msp, x0, y0 - TAP_OD * sc2 / 2, x0 + TAP_L * sc2, y0 + TAP_OD * sc2 / 2, "轮廓", LW_C)
    id_ = TAP_OD - 2 * TAP_W
    L(msp, (x0, y0 - id_ * sc2 / 2), (x0 + TAP_L * sc2, y0 - id_ * sc2 / 2), "虚线", LW_F, "DASHED")
    L(msp, (x0, y0 + id_ * sc2 / 2), (x0 + TAP_L * sc2, y0 + id_ * sc2 / 2), "虚线", LW_F, "DASHED")
    dim_h(msp, x0, x0 + TAP_L * sc2, y0 - TAP_OD * sc2 / 2 - 8, f"L={TAP_L}")
    T(msp, f"取压管 Φ{TAP_OD}×{TAP_W}  件数2", 2.0, (x0 + TAP_L * sc2 / 2, y0 + TAP_OD * sc2 / 2 + 8), TextEntityAlignment.BOTTOM_CENTER)

    simple_table(
        msp,
        ox + 200,
        oy + 115,
        ["项目", "内容"],
        [
            ["标准", "HG/T20592 PN25 WN RF"],
            ["内径", f"D={D}"],
            ["取压孔", f"Φ{TAP_HOLE}"],
            ["密封面", "RF Ra3.2"],
            ["件数", "上/下游各1"],
        ],
        [36, 90],
        row_h=5.2,
        fs=1.7,
    )
    T(msp, "法兰说明", 2.2, (ox + 200, oy + 118), TextEntityAlignment.LEFT)


def build():
    doc = setup()
    msp = doc.modelspace()
    sheet1(msp)
    sheet2(msp)
    sheet3(msp)
    zoom.extents(msp)
    DXF_DIR.mkdir(parents=True, exist_ok=True)
    path = DXF_DIR / f"{TAG}_清洁版.dxf"
    doc.saveas(path)
    return path


def export_pdf(dxf_path: Path, pdf_path: Path):
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
        lineweight_scaling=0.95,
        min_lineweight=0.15,
        color_policy=ColorPolicy.BLACK,
        background_policy=BackgroundPolicy.WHITE,
    )
    with PdfPages(pdf_path) as pdf:
        for i in range(3):
            ox = ox_of(i)
            fig = plt.figure(figsize=(16.54, 11.69))
            ax = fig.add_axes([0, 0, 1, 1])
            props = LayoutProperties.from_layout(msp)
            props.set_colors("#FFFFFF", "#000000")
            Frontend(ctx, MatplotlibBackend(ax), config=cfg).draw_layout(msp, finalize=False, layout_properties=props)
            ax.set_xlim(ox - 1, ox + A3W + 1)
            ax.set_ylim(-1, A3H + 1)
            ax.set_aspect("equal")
            ax.axis("off")
            pdf.savefig(fig, facecolor="white")
            plt.close(fig)
            print("page", i + 1)


def main():
    dxf = build()
    print("DXF", dxf)
    pdf = OUT / f"{TAG}_清洁版出图.pdf"
    export_pdf(dxf, pdf)
    print("PDF", pdf, pdf.stat().st_size)
    import fitz

    doc = fitz.open(pdf)
    for i in range(len(doc)):
        pix = doc[i].get_pixmap(matrix=fitz.Matrix(1.35, 1.35))
        p = OUT / f"预览_清洁版_p{i+1}.png"
        pix.save(p)
        print("preview", p.name)


if __name__ == "__main__":
    main()
