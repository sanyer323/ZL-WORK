# -*- coding: utf-8 -*-
"""
FE-1002 法兰对夹孔板 — EMCO 风格正式出图
参考：Emco Controls 3-09-7820-2 / GA 装配图版式
- 半剖细部（颈锥、突面、螺柱上半外形/下半剖）
- 轴测分解球标
- 铭牌刻字框
- 明细 + Design Data 表
- 分区留白，禁止叠字
输出：DXF + 矢量多页 PDF
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
DWG = "FE-1002-GA"
COMPANY = "FE-1002 Shop Drawing"

DN, PIPE_OD, PIPE_WALL = 250, 273.0, 4.0
METER_ID, BORE_D, BETA = 265.0, 136.18, 0.5139
TF_C, PF_KPAG, FA = -162.0, 600.0, 0.9938

PLATE_OD, PLATE_E, PLATE_E_EDGE = 320.0, 6.0, 2.5
BEVEL, HANDLE_W, HANDLE_L = 45.0, 36.0, 50.0
HANDLE_HOLE = 8.0

FL_OD, FL_PCD, FL_HOLE, FL_N = 425.0, 370.0, 30.0, 12
FL_BOLT, FL_C, FL_RF, FL_RF_H = "M27", 32.0, 335.0, 2.0
FL_NECK, FL_H, FL_R = 298.0, 88.0, 12.0

GASKET_T, GASKET_OD, GASKET_ID = 2.0, 335.0, 274.0
STUB_L = 150.0
TAP_OFF, TAP_TOL, TAP_HOLE = 25.4, 0.8, 8.0
TAP_OD, TAP_WALL, TAP_L = 21.3, 2.77, 100.0

MAT = "F304/F304L"
OUT = Path(__file__).resolve().parent
DXF_DIR = OUT / "DXF"
A3W, A3H = 420.0, 297.0
LW_C, LW_F, LW_H = 60, 18, 13
# ==================================================


def setup():
    doc = ezdxf.new("R2013", setup=True)
    doc.units = units.MM
    doc.header["$INSUNITS"] = 4
    doc.header["$MEASUREMENT"] = 1
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
        ("轴测", 7, LW_F, "Continuous"),
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
    doc.styles.get("Standard").dxf.font = "simhei.ttf"
    return doc


def T(msp, s, h, xy, align=TextEntityAlignment.LEFT, layer="文字", rot=0):
    t = msp.add_text(str(s), height=h, dxfattribs={"layer": layer, "style": "CN", "rotation": rot})
    t.set_placement(xy, align=align)
    return t


def line(msp, a, b, layer="轮廓", lw=LW_C, lt="Continuous"):
    msp.add_line(a, b, dxfattribs={"layer": layer, "lineweight": lw, "linetype": lt})


def circ(msp, c, r, layer="轮廓", lw=LW_C, lt="Continuous"):
    msp.add_circle(c, r, dxfattribs={"layer": layer, "lineweight": lw, "linetype": lt})


def rect(msp, x0, y0, x1, y1, layer="轮廓", lw=LW_C):
    line(msp, (x0, y0), (x1, y0), layer, lw)
    line(msp, (x1, y0), (x1, y1), layer, lw)
    line(msp, (x1, y1), (x0, y1), layer, lw)
    line(msp, (x0, y1), (x0, y0), layer, lw)


def poly(msp, pts, close=False, layer="轮廓", lw=LW_C):
    if close and pts[0] != pts[-1]:
        pts = list(pts) + [pts[0]]
    for a, b in zip(pts[:-1], pts[1:]):
        line(msp, a, b, layer, lw)


def hatch_box(msp, x0, y0, x1, y1, step=3.2, ang=45.0, y_clip_max=None):
    """矩形内细剖面线；可限制不超过 y_clip_max（世界坐标）"""
    if y_clip_max is not None:
        y1 = min(y1, y_clip_max)
        y0 = min(y0, y_clip_max)
    if abs(y1 - y0) < 0.2 or abs(x1 - x0) < 0.2:
        return
    if y0 > y1:
        y0, y1 = y1, y0
    if x0 > x1:
        x0, x1 = x1, x0
    a = math.radians(ang)
    dx, dy = math.cos(a), math.sin(a)
    nx, ny = -dy, dx
    corners = [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]
    ps = [p[0] * nx + p[1] * ny for p in corners]
    pmin, pmax = min(ps), max(ps)
    span = abs((x1 - x0) * dx) + abs((y1 - y0) * dy) + 100.0
    p = pmin - step
    while p <= pmax + step:
        cx, cy = nx * p, ny * p
        p1 = (cx - dx * span, cy - dy * span)
        p2 = (cx + dx * span, cy + dy * span)
        dxs, dys = p2[0] - p1[0], p2[1] - p1[1]
        t0, t1 = 0.0, 1.0
        ok = True
        for pp, q in (
            (-dxs, p1[0] - x0),
            (dxs, x1 - p1[0]),
            (-dys, p1[1] - y0),
            (dys, y1 - p1[1]),
        ):
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
            line(
                msp,
                (p1[0] + t0 * dxs, p1[1] + t0 * dys),
                (p1[0] + t1 * dxs, p1[1] + t1 * dys),
                "剖面线",
                LW_H,
            )
        p += step


def dim_h(msp, x0, x1, y, label, gap=2.0):
    line(msp, (x0, y), (x1, y), "标注", LW_F)
    for x in (x0, x1):
        line(msp, (x, y - 1.6), (x, y + 1.6), "标注", LW_F)
    s = 2.4
    line(msp, (x0, y), (x0 + s, y + 0.85), "标注", LW_F)
    line(msp, (x0, y), (x0 + s, y - 0.85), "标注", LW_F)
    line(msp, (x1, y), (x1 - s, y + 0.85), "标注", LW_F)
    line(msp, (x1, y), (x1 - s, y - 0.85), "标注", LW_F)
    T(msp, label, 2.5, ((x0 + x1) / 2, y + gap), TextEntityAlignment.BOTTOM_CENTER, "标注")


def dim_v(msp, x, y0, y1, label, side=-1):
    line(msp, (x, y0), (x, y1), "标注", LW_F)
    for y in (y0, y1):
        line(msp, (x - 1.6, y), (x + 1.6, y), "标注", LW_F)
    s = 2.4
    line(msp, (x, y0), (x - 0.85, y0 + s), "标注", LW_F)
    line(msp, (x, y0), (x + 0.85, y0 + s), "标注", LW_F)
    line(msp, (x, y1), (x - 0.85, y1 - s), "标注", LW_F)
    line(msp, (x, y1), (x + 0.85, y1 - s), "标注", LW_F)
    T(msp, label, 2.5, (x + 5.0 * side, (y0 + y1) / 2), TextEntityAlignment.MIDDLE_CENTER, "标注", 90)


def balloon(msp, x, y, bx, by, n, r=4.0):
    line(msp, (x, y), (bx, by), "标注", LW_F)
    circ(msp, (bx, by), r, "轮廓", LW_C)
    T(msp, str(n), 2.8, (bx, by), TextEntityAlignment.MIDDLE_CENTER)


def sheet_xy(i):
    return i * (A3W + 50.0), 0.0


def frame_and_title(msp, ox, oy, sheet, total, title, scale, dwg_no):
    """A3 图框 + EMCO 风格标题栏（右下，单行文字防叠）"""
    rect(msp, ox, oy, ox + A3W, oy + A3H, "图框", LW_C)
    m = 8.0
    rect(msp, ox + m, oy + m, ox + A3W - m, oy + A3H - m, "图框", LW_F)
    # 标题栏 200×52
    tw, th = 200.0, 52.0
    tx0 = ox + A3W - m - tw
    ty0 = oy + m
    rect(msp, tx0, ty0, tx0 + tw, ty0 + th, "图框", LW_C)
    # 横线
    for dy in (13, 26, 39):
        line(msp, (tx0, ty0 + dy), (tx0 + tw, ty0 + dy), "图框", LW_F)
    # 竖线
    for dx in (55, 130, 165):
        line(msp, (tx0 + dx, ty0), (tx0 + dx, ty0 + th), "图框", LW_F)

    T(msp, COMPANY[:18], 2.4, (tx0 + 27, ty0 + 45.5), TextEntityAlignment.MIDDLE_CENTER)
    T(msp, title[:22], 3.0, (tx0 + 92, ty0 + 45.5), TextEntityAlignment.MIDDLE_CENTER)
    T(msp, MAT, 2.2, (tx0 + 147, ty0 + 45.5), TextEntityAlignment.MIDDLE_CENTER)
    T(msp, scale, 2.2, (tx0 + 182, ty0 + 45.5), TextEntityAlignment.MIDDLE_CENTER)

    T(msp, f"Tag {TAG}", 2.3, (tx0 + 27, ty0 + 32.5), TextEntityAlignment.MIDDLE_CENTER)
    T(msp, f"Dwg {dwg_no}", 2.3, (tx0 + 92, ty0 + 32.5), TextEntityAlignment.MIDDLE_CENTER)
    T(msp, f"Sheet {sheet}/{total}", 2.2, (tx0 + 147, ty0 + 32.5), TextEntityAlignment.MIDDLE_CENTER)
    T(msp, "A3", 2.2, (tx0 + 182, ty0 + 32.5), TextEntityAlignment.MIDDLE_CENTER)

    T(msp, f"S/N {SERIAL}", 2.2, (tx0 + 27, ty0 + 19.5), TextEntityAlignment.MIDDLE_CENTER)
    T(msp, MODEL, 2.1, (tx0 + 92, ty0 + 19.5), TextEntityAlignment.MIDDLE_CENTER)
    T(msp, "Unit: mm", 2.2, (tx0 + 147, ty0 + 19.5), TextEntityAlignment.MIDDLE_CENTER)
    T(msp, "R2013", 2.0, (tx0 + 182, ty0 + 19.5), TextEntityAlignment.MIDDLE_CENTER)

    T(msp, "Drawn", 2.0, (tx0 + 14, ty0 + 6.5), TextEntityAlignment.MIDDLE_CENTER)
    T(msp, "Checked", 2.0, (tx0 + 40, ty0 + 6.5), TextEntityAlignment.MIDDLE_CENTER)
    T(msp, f"DN{DN} PN25 HG/T20592 RF  Flange taps", 2.1, (tx0 + 120, ty0 + 6.5), TextEntityAlignment.MIDDLE_CENTER)

    T(msp, f"{TAG}  {title}", 4.2, (ox + m + 3, oy + A3H - m - 7), TextEntityAlignment.LEFT)
    # 返回内容安全区上沿（标题栏顶 + 间隙）
    return ty0 + th + 4.0


def table(msp, x, y, headers, rows, col_w, row_h=6.2, title=None, fs=1.9):
    """向下生长的表格；返回表格底边 y"""
    if title:
        T(msp, title, 2.6, (x, y + 3.5), TextEntityAlignment.LEFT)
    data = [headers] + rows
    yy = y
    for i, row in enumerate(data):
        xx = x
        for j, cell in enumerate(row):
            w = col_w[j]
            rect(msp, xx, yy - row_h, xx + w, yy, "表格", LW_F)
            T(msp, str(cell)[:28], fs if i else fs + 0.2, (xx + 1.0, yy - row_h / 2), TextEntityAlignment.MIDDLE_LEFT, "表格")
            xx += w
        yy -= row_h
    return yy


# ---------- 细部：法兰半剖轮廓（真实比例，世界坐标） ----------
def draw_flange_half(msp, x_face, facing, y0=0.0, section_lower=True):
    """
    x_face: RF 密封面所在 X（孔板侧）
    facing: +1 密封面朝 +X；-1 朝 -X
    画出带颈对焊法兰：盘厚 C、颈高、颈锥、突面；下半剖面线
    """
    s = 1.0 if facing > 0 else -1.0
    # 法兰盘：从密封面往颈部方向
    # 密封面 x_face，盘背面 x_face - s*C
    x_back = x_face - s * FL_C
    x_hub = x_back - s * (FL_H - FL_C)  # 焊端附近

    # 外轮廓（上半 + 下半对称）
    def yl(r):
        return y0 + r

    def ym(r):
        return y0 - r

    # RF 台阶
    x_rf = x_face - s * FL_RF_H
    # 上半外形
    poly(
        msp,
        [
            (x_face, yl(FL_RF / 2)),
            (x_face, yl(FL_OD / 2)),
            (x_back, yl(FL_OD / 2)),
            (x_back, yl(FL_NECK / 2)),
            (x_hub + s * 18, yl(FL_NECK / 2)),
            (x_hub, yl(PIPE_OD / 2)),
        ],
        layer="轮廓",
        lw=LW_C,
    )
    # 下半外形
    poly(
        msp,
        [
            (x_face, ym(FL_RF / 2)),
            (x_face, ym(FL_OD / 2)),
            (x_back, ym(FL_OD / 2)),
            (x_back, ym(FL_NECK / 2)),
            (x_hub + s * 18, ym(FL_NECK / 2)),
            (x_hub, ym(PIPE_OD / 2)),
        ],
        layer="轮廓",
        lw=LW_C,
    )
    # RF 内径竖线
    line(msp, (x_rf, yl(FL_RF / 2)), (x_face, yl(FL_RF / 2)), "细实线", LW_F)
    line(msp, (x_rf, ym(FL_RF / 2)), (x_face, ym(FL_RF / 2)), "细实线", LW_F)
    line(msp, (x_rf, yl(FL_RF / 2)), (x_rf, yl(METER_ID / 2)), "细实线", LW_F)
    line(msp, (x_rf, ym(FL_RF / 2)), (x_rf, ym(METER_ID / 2)), "细实线", LW_F)

    # 内孔（通径）
    line(msp, (x_hub, yl(METER_ID / 2)), (x_face, yl(METER_ID / 2)), "细实线", LW_F)
    line(msp, (x_hub, ym(METER_ID / 2)), (x_face, ym(METER_ID / 2)), "细实线", LW_F)

    # 上半：螺栓外形（可见）
    by = FL_PCD / 2 * 0.92
    bx = (x_face + x_back) / 2
    circ(msp, (bx, y0 + by), FL_HOLE / 2 * 0.55, "细实线", LW_F)
    # 下半：螺栓孔剖到（虚线圆）
    circ(msp, (bx, y0 - by), FL_HOLE / 2 * 0.55, "虚线", LW_F, "DASHED")

    if section_lower:
        # 盘下半剖面
        xa, xb = min(x_face, x_back), max(x_face, x_back)
        hatch_box(msp, xa, y0 - FL_OD / 2, xb, y0 - METER_ID / 2, step=4.0, y_clip_max=y0 - 0.5)
        # 颈下半
        xa, xb = min(x_hub, x_back), max(x_hub, x_back)
        hatch_box(msp, xa, y0 - FL_NECK / 2, xb, y0 - METER_ID / 2, step=3.5, y_clip_max=y0 - 0.5)

    return x_hub, x_back, x_face


def draw_plate_section(msp, x_up, y0=0.0):
    """孔板剖视：上游面在 x_up，厚度沿 +X"""
    e, E = PLATE_E_EDGE, PLATE_E
    br = BORE_D / 2
    pod = PLATE_OD / 2
    bev = E - e
    # 外廓
    poly(
        msp,
        [
            (x_up, y0 + pod),
            (x_up + E, y0 + pod),
            (x_up + E, y0 - pod),
            (x_up, y0 - pod),
            (x_up, y0 + pod),
        ],
        layer="轮廓",
        lw=LW_C,
    )
    # 孔口
    line(msp, (x_up, y0 + br), (x_up + e, y0 + br), "轮廓", LW_C)
    line(msp, (x_up, y0 - br), (x_up + e, y0 - br), "轮廓", LW_C)
    line(msp, (x_up + e, y0 + br), (x_up + E, y0 + br + bev), "轮廓", LW_C)
    line(msp, (x_up + e, y0 - br), (x_up + E, y0 - br - bev), "轮廓", LW_C)
    line(msp, (x_up + E, y0 + br + bev), (x_up + E, y0 - br - bev), "轮廓", LW_C)
    line(msp, (x_up, y0 + br), (x_up, y0 - br), "轮廓", LW_C)
    hatch_box(msp, x_up, y0 - pod, x_up + E, y0, step=2.8, y_clip_max=y0 - 0.2)
    return x_up + E


# ===================== Sheet 1: GA =====================
def sheet1(msp):
    ox, oy = sheet_xy(0)
    y_safe = frame_and_title(msp, ox, oy, 1, 3, "Orifice Assembly GA", "1:3", f"{DWG}-01")

    # ---- 主视图区：半剖装配（真实 mm，再整体平移缩放）----
    # 用 1:3 显示：世界坐标先按真实画在局部，再 *sc 平移
    sc = 1.0 / 3.0
    # 局部真实坐标原点
    # 布局：stub | flange1 | g | plate | g | flange2 | stub
    neck = FL_H - FL_C
    g, H = GASKET_T, PLATE_E

    # 真实 X 链
    x = 0.0
    x_stub1_0 = x
    x_stub1_1 = x + STUB_L
    x_hub1 = x_stub1_1
    x_face1 = x_hub1 + neck + FL_C  # 密封面
    # 重新：焊端在左，密封面在右
    # hub at left of flange
    x_hub1 = x_stub1_1
    x_back1 = x_hub1 + neck
    x_face1 = x_back1 + FL_C
    x_g1 = x_face1
    x_pl = x_g1 + g
    x_g2 = x_pl + H
    x_face2 = x_g2 + g
    x_back2 = x_face2 + FL_C
    x_hub2 = x_back2 + neck
    x_stub2_0 = x_hub2
    x_stub2_1 = x_stub2_0 + STUB_L

    # 显示原点：图框内上部
    bx = ox + 25
    by = oy + 175

    def S(X, Y):
        return (bx + X * sc, by + Y * sc)

    # 中心线
    line(msp, S(x_stub1_0 - 30, 0), S(x_stub2_1 + 30, 0), "中心线", LW_F, "CENTER")

    # 短节
    def pipe(xa, xb):
        line(msp, S(xa, PIPE_OD / 2), S(xb, PIPE_OD / 2), "轮廓", LW_C)
        line(msp, S(xa, -PIPE_OD / 2), S(xb, -PIPE_OD / 2), "轮廓", LW_C)
        line(msp, S(xa, METER_ID / 2), S(xb, METER_ID / 2), "虚线", LW_F, "DASHED")
        line(msp, S(xa, -METER_ID / 2), S(xb, -METER_ID / 2), "虚线", LW_F, "DASHED")
        # 下半管壁剖
        hatch_box(
            msp,
            S(xa, -PIPE_OD / 2)[0],
            S(xa, -PIPE_OD / 2)[1],
            S(xb, -METER_ID / 2)[0],
            S(xb, -METER_ID / 2)[1],
            step=3.0,
            y_clip_max=by - 0.5,
        )

    pipe(x_stub1_0, x_stub1_1)
    pipe(x_stub2_0, x_stub2_1)

    # 法兰：在显示坐标直接细画（调用辅助按真实尺寸换算）
    def flange_draw(x_face, facing):
        s = 1.0 if facing > 0 else -1.0
        x_back = x_face - s * FL_C
        x_hub = x_back - s * neck
        # 外轮廓折线（上）
        pts_u = [
            S(x_face, FL_RF / 2),
            S(x_face, FL_OD / 2),
            S(x_back, FL_OD / 2),
            S(x_back, FL_NECK / 2),
            S(x_hub + s * 20, FL_NECK / 2),
            S(x_hub, PIPE_OD / 2),
        ]
        pts_d = [
            S(x_face, -FL_RF / 2),
            S(x_face, -FL_OD / 2),
            S(x_back, -FL_OD / 2),
            S(x_back, -FL_NECK / 2),
            S(x_hub + s * 20, -FL_NECK / 2),
            S(x_hub, -PIPE_OD / 2),
        ]
        for a, b in zip(pts_u, pts_u[1:]):
            line(msp, a, b, "轮廓", LW_C)
        for a, b in zip(pts_d, pts_d[1:]):
            line(msp, a, b, "轮廓", LW_C)
        # 端面封闭
        line(msp, S(x_face, FL_RF / 2), S(x_face, -FL_RF / 2), "轮廓", LW_C)
        line(msp, S(x_hub, PIPE_OD / 2), S(x_hub, -PIPE_OD / 2), "细实线", LW_F)
        # RF 内台
        x_rf = x_face - s * FL_RF_H
        line(msp, S(x_rf, FL_RF / 2), S(x_face, FL_RF / 2), "细实线", LW_F)
        line(msp, S(x_rf, -FL_RF / 2), S(x_face, -FL_RF / 2), "细实线", LW_F)
        line(msp, S(x_rf, FL_RF / 2), S(x_rf, METER_ID / 2), "细实线", LW_F)
        line(msp, S(x_rf, -FL_RF / 2), S(x_rf, -METER_ID / 2), "细实线", LW_F)
        # 通径
        line(msp, S(x_hub, METER_ID / 2), S(x_face, METER_ID / 2), "细实线", LW_F)
        line(msp, S(x_hub, -METER_ID / 2), S(x_face, -METER_ID / 2), "细实线", LW_F)
        # 螺栓
        bx = (x_face + x_back) / 2
        circ(msp, S(bx, FL_PCD / 2 * 0.9), 3.2, "细实线", LW_F)
        circ(msp, S(bx, -FL_PCD / 2 * 0.9), 3.2, "虚线", LW_F, "DASHED")
        # 剖面
        xa, xb = min(S(x_face, 0)[0], S(x_back, 0)[0]), max(S(x_face, 0)[0], S(x_back, 0)[0])
        hatch_box(msp, xa, S(0, -FL_OD / 2)[1], xb, S(0, -METER_ID / 2)[1], 3.8, y_clip_max=by - 0.5)
        xa, xb = min(S(x_hub, 0)[0], S(x_back, 0)[0]), max(S(x_hub, 0)[0], S(x_back, 0)[0])
        hatch_box(msp, xa, S(0, -FL_NECK / 2)[1], xb, S(0, -METER_ID / 2)[1], 3.2, y_clip_max=by - 0.5)
        return x_hub

    flange_draw(x_face1, +1)
    flange_draw(x_face2, -1)

    # 垫片（加厚示意）
    for xa in (x_g1, x_g2):
        rect(
            msp,
            S(xa, -GASKET_OD / 2)[0],
            S(xa, -GASKET_OD / 2)[1],
            S(xa + g, GASKET_OD / 2)[0],
            S(xa + g, GASKET_OD / 2)[1],
            "细实线",
            LW_F,
        )

    # 孔板
    e, br, pod = PLATE_E_EDGE, BORE_D / 2, PLATE_OD / 2
    bev = PLATE_E - e
    rect(msp, S(x_pl, -pod)[0], S(x_pl, -pod)[1], S(x_pl + H, pod)[0], S(x_pl + H, pod)[1], "轮廓", LW_C)
    line(msp, S(x_pl, br), S(x_pl + e, br), "轮廓", LW_C)
    line(msp, S(x_pl, -br), S(x_pl + e, -br), "轮廓", LW_C)
    line(msp, S(x_pl + e, br), S(x_pl + H, br + bev), "轮廓", LW_C)
    line(msp, S(x_pl + e, -br), S(x_pl + H, -br - bev), "轮廓", LW_C)
    line(msp, S(x_pl + H, br + bev), S(x_pl + H, -br - bev), "轮廓", LW_C)
    line(msp, S(x_pl, br), S(x_pl, -br), "轮廓", LW_C)
    hatch_box(msp, S(x_pl, -pod)[0], S(x_pl, -pod)[1], S(x_pl + H, 0)[0], by - 0.3, 2.6, y_clip_max=by - 0.3)

    # 手柄
    hx = x_pl + H / 2
    line(msp, S(hx, pod), S(hx, pod + 22), "轮廓", LW_C)
    rect(
        msp,
        S(hx - HANDLE_W / 2, pod + 22)[0],
        S(hx - HANDLE_W / 2, pod + 22)[1],
        S(hx + HANDLE_W / 2, pod + 22 + 30)[0],
        S(hx + HANDLE_W / 2, pod + 22 + 30)[1],
        "轮廓",
        LW_C,
    )

    # 取压管 + 钻孔
    def tap(ax):
        line(msp, S(ax - TAP_OD / 2, FL_OD / 2), S(ax - TAP_OD / 2, FL_OD / 2 + TAP_L), "轮廓", LW_C)
        line(msp, S(ax + TAP_OD / 2, FL_OD / 2), S(ax + TAP_OD / 2, FL_OD / 2 + TAP_L), "轮廓", LW_C)
        line(msp, S(ax - TAP_OD / 2, FL_OD / 2 + TAP_L), S(ax + TAP_OD / 2, FL_OD / 2 + TAP_L), "轮廓", LW_C)
        line(msp, S(ax - TAP_OD / 2 + TAP_WALL, FL_OD / 2), S(ax - TAP_OD / 2 + TAP_WALL, FL_OD / 2 + TAP_L), "虚线", LW_F, "DASHED")
        line(msp, S(ax + TAP_OD / 2 - TAP_WALL, FL_OD / 2), S(ax + TAP_OD / 2 - TAP_WALL, FL_OD / 2 + TAP_L), "虚线", LW_F, "DASHED")
        line(msp, S(ax, FL_OD / 2), S(ax, METER_ID / 2), "虚线", LW_F, "DASHED")
        # 焊脚示意
        line(msp, S(ax - TAP_OD / 2 - 2, FL_OD / 2), S(ax - TAP_OD / 2, FL_OD / 2 + 4), "细实线", LW_F)
        line(msp, S(ax + TAP_OD / 2 + 2, FL_OD / 2), S(ax + TAP_OD / 2, FL_OD / 2 + 4), "细实线", LW_F)

    ax1 = x_pl - TAP_OFF
    ax2 = x_pl + H + TAP_OFF
    tap(ax1)
    tap(ax2)

    # 螺柱（上半外形完整，下半剖）
    yb = FL_PCD / 2 * 0.88
    line(msp, S(x_face1 - FL_C + 6, yb), S(x_face2 + FL_C - 6, yb), "轮廓", LW_C)
    line(msp, S(x_face1 - FL_C + 6, -yb), S(x_face2 + FL_C - 6, -yb), "轮廓", LW_C)
    for xx in (x_face1 - FL_C + 6, x_face2 + FL_C - 6):
        rect(msp, S(xx - 5, yb - 6)[0], S(xx - 5, yb - 6)[1], S(xx + 5, yb + 6)[0], S(xx + 5, yb + 6)[1], "轮廓", LW_C)
        rect(msp, S(xx - 5, -yb - 6)[0], S(xx - 5, -yb - 6)[1], S(xx + 5, -yb + 6)[0], S(xx + 5, -yb + 6)[1], "细实线", LW_F)

    # 尺寸（放在图形下方空白，远离标题栏）
    dim_h(msp, S(x_face1 - FL_C, 0)[0], S(x_face2 + FL_C, 0)[0], S(0, -FL_OD / 2)[1] - 14, f"≈{int((x_face2 + FL_C) - (x_face1 - FL_C))}")
    dim_v(msp, S(x_stub1_0 - 20, 0)[0], S(0, -FL_OD / 2)[1], S(0, FL_OD / 2)[1], f"Ø{int(FL_OD)}", -1)
    T(msp, f"Ø{PIPE_OD}×{PIPE_WALL}", 2.3, S((x_stub1_0 + x_stub1_1) / 2, PIPE_OD / 2 + 10), TextEntityAlignment.BOTTOM_CENTER, "标注")
    T(msp, f"d=Ø{BORE_D}", 2.3, S(x_pl + H + 18, 8), TextEntityAlignment.LEFT, "标注")
    T(msp, f"taps {TAP_OFF}±{TAP_TOL} from plate face", 2.1, S((ax1 + ax2) / 2, FL_OD / 2 + TAP_L + 18), TextEntityAlignment.BOTTOM_CENTER, "标注")
    T(msp, "FLOW →  (bevel downstream)", 2.4, S((x_face1 + x_face2) / 2, -FL_OD / 2 - 32), TextEntityAlignment.TOP_CENTER, "标注")
    T(msp, "Section A-A  (upper: outline / lower: section)", 2.4, (S((x_stub1_0 + x_stub2_1) / 2, 0)[0], by + FL_OD / 2 * sc + 48), TextEntityAlignment.BOTTOM_CENTER)

    # ---- 右侧轴测（斜二测简图）----
    ix, iy = ox + 310, oy + 200

    def iso(x, y, z):
        # 斜二测：x右, z上, y向右下
        return (ix + x * 0.35 + y * 0.25, iy + z * 0.35 - y * 0.18)

    # 简化轴测：两法兰盘 + 孔板 + 取压管
    def iso_box(x0, y0, z0, dx, dy, dz, layer="轴测"):
        pts = [
            iso(x0, y0, z0),
            iso(x0 + dx, y0, z0),
            iso(x0 + dx, y0 + dy, z0),
            iso(x0, y0 + dy, z0),
            iso(x0, y0, z0 + dz),
            iso(x0 + dx, y0, z0 + dz),
            iso(x0 + dx, y0 + dy, z0 + dz),
            iso(x0, y0 + dy, z0 + dz),
        ]
        # 底
        poly(msp, pts[0:4], True, layer, LW_F)
        # 顶
        poly(msp, pts[4:8], True, layer, LW_F)
        for i in range(4):
            line(msp, pts[i], pts[i + 4], layer, LW_F)

    iso_box(0, 0, -40, 12, 80, 80)  # fl1
    iso_box(18, 5, -30, 3, 70, 60)  # plate
    iso_box(26, 0, -40, 12, 80, 80)  # fl2
    # taps
    iso_box(6, 35, 42, 4, 4, 28)
    iso_box(30, 35, 42, 4, 4, 28)
    T(msp, "Isometric (schematic)", 2.3, (ix + 30, iy + 55), TextEntityAlignment.BOTTOM_CENTER)
    balloon(msp, *iso(6, 40, 0), ix - 25, iy + 20, "1")
    balloon(msp, *iso(32, 40, 0), ix + 70, iy + 20, "2")
    balloon(msp, *iso(19, 40, 0), ix + 25, iy - 55, "3")
    balloon(msp, *iso(8, 37, 55), ix - 20, iy + 50, "4")
    balloon(msp, *iso(32, 37, 55), ix + 75, iy + 50, "5")

    # ---- 铭牌（避开 Design 表：表在 ox+250,y≈118 向下；铭牌放更上）----
    nx0, ny0 = ox + 305, oy + 125
    rect(msp, nx0, ny0, nx0 + 90, ny0 + 42, "轮廓", LW_C)
    T(msp, "NAMEPLATE", 1.8, (nx0 + 45, ny0 + 37), TextEntityAlignment.MIDDLE_CENTER)
    for i, s in enumerate(
        [f"TAG: {TAG}", f"S/N: {SERIAL}", f"DN{DN} PN25", f"d={BORE_D} D={METER_ID}", f"MAT: {MAT}", f"MODEL: {MODEL}"]
    ):
        T(msp, s, 1.7, (nx0 + 3, ny0 + 30 - i * 4.8), TextEntityAlignment.LEFT)

    # ---- Parts list（左侧可低至图框内边）+ Design data（必须在标题栏上方）----
    # 标题栏顶 ≈ oy+8+52=oy+60；右侧内容 y 必须 > oy+64
    bom_y = oy + 92
    table(
        msp,
        ox + 12,
        bom_y,
        ["Item", "Qty", "Description", "Material", "Remark"],
        [
            ["1", "1", f"Upstream orifice flange WN RF DN{DN} PN25", MAT, "HG/T20592"],
            ["2", "1", f"Downstream orifice flange WN RF DN{DN} PN25", MAT, "mirror"],
            ["3", "1", f"Orifice plate Ø{PLATE_OD}×{PLATE_E} bore Ø{BORE_D}", MAT, TAG],
            ["4", "1", f"Impulse pipe DN15 Ø{TAP_OD}×{TAP_WALL} L={TAP_L}", MAT, "upstream"],
            ["5", "1", f"Impulse pipe DN15 Ø{TAP_OD}×{TAP_WALL} L={TAP_L}", MAT, "downstream"],
            ["6", f"{FL_N}", f"Stud {FL_BOLT} + nuts", "B8M/B8M", "w/ washers"],
            ["7", "2", f"Spiral wound gasket DN{DN} PN25 RF", "304+Graphite", "cryogenic"],
            ["8", "2", f"Pipe stub Ø{PIPE_OD}×{PIPE_WALL} L={STUB_L}", MAT, "BW"],
        ],
        [18, 14, 115, 40, 32],
        row_h=5.6,
        title="Parts List",
        fs=1.65,
    )

    # Design data 放在标题栏正上方（x 进入标题栏区时 y 必须足够高）
    table(
        msp,
        ox + 250,
        oy + 118,
        ["Design Data", ""],
        [
            ["Code", "GB/T2624.2 / ISO5167-2"],
            ["Flange", "HG/T20592 PN25 RF WN"],
            ["Service", f"LNG  {TF_C}C  {PF_KPAG}kPaG"],
            ["Beta / Fa", f"{BETA} / {FA}"],
            ["Tap type", f"Flange {TAP_OFF}+/-{TAP_TOL}"],
            ["NDT", "PT welds; hydro per piping"],
        ],
        [40, 95],
        row_h=5.4,
        title="Design / Test",
        fs=1.65,
    )


# ===================== Sheet 2: Orifice plate =====================
def sheet2(msp):
    ox, oy = sheet_xy(1)
    y_safe = frame_and_title(msp, ox, oy, 2, 3, "Orifice Plate Detail", "1:2 / 5:1", f"{DWG}-02")

    # 主视 1:2 — 放左上，远离标题栏
    sc = 0.5
    cx, cy = ox + 115, oy + 175

    def P(x, y):
        return (cx + x * sc, cy + y * sc)

    R, r = PLATE_OD / 2, BORE_D / 2
    circ(msp, (cx, cy), R * sc, "轮廓", LW_C)
    circ(msp, (cx, cy), r * sc, "轮廓", LW_C)
    # 同心细线（密封接触示意）
    circ(msp, (cx, cy), (R - 8) * sc, "细实线", LW_F)
    line(msp, P(-R - 12, 0), P(R + 12, 0), "中心线", LW_F, "CENTER")
    line(msp, P(0, -R - 12), P(0, R + HANDLE_L + 4), "中心线", LW_F, "CENTER")
    # 手柄 + 吊孔
    rect(msp, P(-HANDLE_W / 2, R)[0], P(-HANDLE_W / 2, R)[1], P(HANDLE_W / 2, R + HANDLE_L)[0], P(HANDLE_W / 2, R + HANDLE_L)[1], "轮廓", LW_C)
    circ(msp, P(0, R + HANDLE_L - 12), HANDLE_HOLE / 2 * sc, "细实线", LW_F)
    T(msp, TAG, 2.4, P(0, R + HANDLE_L * 0.55), TextEntityAlignment.MIDDLE_CENTER)
    T(msp, "UPSTREAM", 1.8, P(0, R + HANDLE_L * 0.28), TextEntityAlignment.MIDDLE_CENTER)

    # 流向刻印
    line(msp, P(r + 10, -18), P(r + 38, -18), "标注", LW_F)
    line(msp, P(r + 38, -18), P(r + 32, -14), "标注", LW_F)
    line(msp, P(r + 38, -18), P(r + 32, -22), "标注", LW_F)
    T(msp, "flow mark", 1.8, P(r + 24, -26), TextEntityAlignment.TOP_CENTER, "标注")

    dim_h(msp, P(-R, 0)[0], P(R, 0)[0], P(0, -R)[1] - 14, f"Ø{PLATE_OD}  0/-0.2")
    dim_h(msp, P(-r, 0)[0], P(r, 0)[0], cy + 6, f"Ø{BORE_D} ±0.05")
    dim_v(msp, P(R, 0)[0] + 12, P(0, R)[1], P(0, R + HANDLE_L)[1], f"{HANDLE_L}", 1)
    dim_h(msp, P(-HANDLE_W / 2, 0)[0], P(HANDLE_W / 2, 0)[0], P(0, R + HANDLE_L)[1] + 6, f"{HANDLE_W}")
    # 粗糙度
    line(msp, P(-R * 0.65, R * 0.5), P(-R * 0.65 - 2, R * 0.5 + 4), "标注", LW_F)
    line(msp, P(-R * 0.65, R * 0.5), P(-R * 0.65 + 2, R * 0.5 + 4), "标注", LW_F)
    T(msp, "Ra1.6", 1.8, P(-R * 0.65 + 4, R * 0.5 + 3), TextEntityAlignment.LEFT, "标注")
    T(msp, "Front view  1:2  (upstream face)", 2.3, (cx, cy - R * sc - 28), TextEntityAlignment.TOP_CENTER)

    # A-A 放大 5:1 — 右侧，底部不低于 y_safe+60
    sc2 = 5.0
    px, py = ox + 280, oy + 175

    def Q(x, y):
        return (px + x * sc2, py + y * sc2)

    E, e = PLATE_E, PLATE_E_EDGE
    bev = E - e
    h = 28.0  # 只画孔口附近
    # 板两侧
    line(msp, Q(0, -h), Q(0, h), "轮廓", LW_C)
    line(msp, Q(E, -h), Q(E, h), "轮廓", LW_C)
    line(msp, Q(0, h), Q(E, h), "轮廓", LW_C)
    line(msp, Q(0, -h), Q(E, -h), "轮廓", LW_C)
    # 孔口
    line(msp, Q(0, r), Q(e, r), "轮廓", LW_C)
    line(msp, Q(0, -r), Q(e, -r), "轮廓", LW_C)
    line(msp, Q(e, r), Q(E, r + bev), "轮廓", LW_C)
    line(msp, Q(e, -r), Q(E, -r - bev), "轮廓", LW_C)
    line(msp, Q(E, r + bev), Q(E, -r - bev), "轮廓", LW_C)
    line(msp, Q(0, r), Q(0, -r), "轮廓", LW_C)
    line(msp, Q(-3, 0), Q(E + 3, 0), "中心线", LW_F, "CENTER")
    hatch_box(msp, Q(0, -h)[0], Q(0, -h)[1], Q(E, 0)[0], py - 0.2, 2.2, y_clip_max=py - 0.2)

    dim_h(msp, Q(0, 0)[0], Q(E, 0)[0], Q(0, -h)[1] - 10, f"E={E}")
    dim_h(msp, Q(0, 0)[0], Q(e, 0)[0], Q(0, r)[1] + 12, f"e={e}")
    T(msp, f"{BEVEL}°", 2.2, Q(e + bev * 0.45, r + bev + 3), TextEntityAlignment.BOTTOM_CENTER, "标注")
    dim_v(msp, Q(E, 0)[0] + 10, Q(0, -r)[1], Q(0, r)[1], f"Ø{BORE_D}", 1)
    T(msp, "Ra0.8", 1.8, Q(-5, r + 2), TextEntityAlignment.RIGHT, "标注")
    T(msp, "Detail A-A  5:1  (downstream bevel)", 2.3, (px + E * sc2 / 2, py + h * sc2 + 14), TextEntityAlignment.BOTTOM_CENTER)
    T(msp, "Inlet edge sharp  G ≤ 0.0004d", 2.0, (px + E * sc2 / 2, Q(0, -h)[1] - 22), TextEntityAlignment.TOP_CENTER)

    # 刻字内容表（底部左侧，在标题栏之上）
    table(
        msp,
        ox + 12,
        min(y_safe - 2, oy + 95),
        ["Marking on handle", ""],
        [
            ["Line1", TAG],
            ["Line2", f"DN{DN} / PN25"],
            ["Line3", f"d={BORE_D}  D={METER_ID}"],
            ["Line4", "UPSTREAM + flow arrow"],
            ["Material", MAT],
            ["Qty", "1"],
            ["Tol. (ISO 2768-m)", "unless noted"],
            ["Edge", "Keep sharp / no chamfer on inlet"],
        ],
        [50, 90],
        row_h=5.5,
        title="Plate notes",
        fs=1.7,
    )


# ===================== Sheet 3: Flange + taps =====================
def sheet3(msp):
    ox, oy = sheet_xy(2)
    y_safe = frame_and_title(msp, ox, oy, 3, 3, "Orifice Flange & Taps", "1:3 / 2:1", f"{DWG}-03")

    sc = 1 / 3.0
    bx, by = ox + 35, oy + 175
    neck = FL_H - FL_C

    def S(x, y):
        return (bx + x * sc, by + y * sc)

    # 法兰半剖（密封面朝右）
    x_face = FL_C
    x_back = 0.0
    x_hub = -neck
    pts_u = [
        S(x_face, FL_RF / 2),
        S(x_face, FL_OD / 2),
        S(x_back, FL_OD / 2),
        S(x_back, FL_NECK / 2),
        S(x_hub + 20, FL_NECK / 2),
        S(x_hub, PIPE_OD / 2),
    ]
    pts_d = [
        S(x_face, -FL_RF / 2),
        S(x_face, -FL_OD / 2),
        S(x_back, -FL_OD / 2),
        S(x_back, -FL_NECK / 2),
        S(x_hub + 20, -FL_NECK / 2),
        S(x_hub, -PIPE_OD / 2),
    ]
    for a, b in zip(pts_u, pts_u[1:]):
        line(msp, a, b, "轮廓", LW_C)
    for a, b in zip(pts_d, pts_d[1:]):
        line(msp, a, b, "轮廓", LW_C)
    line(msp, S(x_face, FL_RF / 2), S(x_face, -FL_RF / 2), "轮廓", LW_C)
    line(msp, S(x_hub, PIPE_OD / 2), S(x_hub, -PIPE_OD / 2), "细实线", LW_F)
    x_rf = x_face - FL_RF_H
    line(msp, S(x_rf, FL_RF / 2), S(x_face, FL_RF / 2), "细实线", LW_F)
    line(msp, S(x_rf, -FL_RF / 2), S(x_face, -FL_RF / 2), "细实线", LW_F)
    line(msp, S(x_hub, METER_ID / 2), S(x_face, METER_ID / 2), "细实线", LW_F)
    line(msp, S(x_hub, -METER_ID / 2), S(x_face, -METER_ID / 2), "细实线", LW_F)
    line(msp, S(x_hub - 15, 0), S(x_face + 20, 0), "中心线", LW_F, "CENTER")
    hatch_box(msp, S(x_back, -FL_OD / 2)[0], S(0, -FL_OD / 2)[1], S(x_face, -METER_ID / 2)[0], S(0, -METER_ID / 2)[1], 3.5, y_clip_max=by - 0.5)
    hatch_box(msp, S(x_hub, -FL_NECK / 2)[0], S(0, -FL_NECK / 2)[1], S(x_back, -METER_ID / 2)[0], S(0, -METER_ID / 2)[1], 3.0, y_clip_max=by - 0.5)

    # 取压
    tap_from_rf = TAP_OFF - GASKET_T
    ax = x_face - tap_from_rf
    line(msp, S(ax, METER_ID / 2), S(ax, FL_OD / 2), "虚线", LW_F, "DASHED")
    line(msp, S(ax - TAP_HOLE / 2, METER_ID / 2), S(ax - TAP_HOLE / 2, FL_OD / 2), "细实线", LW_F)
    line(msp, S(ax + TAP_HOLE / 2, METER_ID / 2), S(ax + TAP_HOLE / 2, FL_OD / 2), "细实线", LW_F)
    rect(
        msp,
        S(ax - TAP_OD / 2, FL_OD / 2)[0],
        S(ax - TAP_OD / 2, FL_OD / 2)[1],
        S(ax + TAP_OD / 2, FL_OD / 2 + TAP_L)[0],
        S(ax + TAP_OD / 2, FL_OD / 2 + TAP_L)[1],
        "轮廓",
        LW_C,
    )
    # 焊角
    line(msp, S(ax - TAP_OD / 2 - 3, FL_OD / 2), S(ax - TAP_OD / 2, FL_OD / 2 + 5), "细实线", LW_F)
    line(msp, S(ax + TAP_OD / 2 + 3, FL_OD / 2), S(ax + TAP_OD / 2, FL_OD / 2 + 5), "细实线", LW_F)

    dim_h(msp, S(x_back, 0)[0], S(x_face, 0)[0], S(0, -FL_OD / 2)[1] - 12, f"C={FL_C}")
    dim_h(msp, S(x_hub, 0)[0], S(x_face, 0)[0], S(0, -FL_OD / 2)[1] - 26, f"H={FL_H}")
    dim_h(msp, S(ax, 0)[0], S(x_face, 0)[0], S(0, FL_OD / 2 + TAP_L)[1] + 10, f"{tap_from_rf:.1f}")
    dim_v(msp, S(x_face, 0)[0] + 12, S(0, -FL_OD / 2)[1], S(0, FL_OD / 2)[1], f"Ø{int(FL_OD)}", 1)
    dim_v(msp, S(x_hub, 0)[0] - 10, S(0, -PIPE_OD / 2)[1], S(0, PIPE_OD / 2)[1], f"Ø{PIPE_OD}", -1)
    T(msp, f"tap hole Ø{TAP_HOLE}", 2.0, S(ax + 10, FL_OD * 0.2), TextEntityAlignment.LEFT, "标注")
    T(msp, f"as-built to plate face {TAP_OFF}±{TAP_TOL}", 1.9, S(ax, FL_OD / 2 + TAP_L + 20), TextEntityAlignment.BOTTOM_CENTER, "标注")
    T(msp, "Half section  1:3", 2.2, (S(x_face / 2, 0)[0], by - FL_OD / 2 * sc - 40), TextEntityAlignment.TOP_CENTER)

    # 密封面视
    cx, cy = ox + 300, oy + 175
    scf = 1 / 3.2
    circ(msp, (cx, cy), FL_OD / 2 * scf, "轮廓", LW_C)
    circ(msp, (cx, cy), FL_RF / 2 * scf, "细实线", LW_F)
    circ(msp, (cx, cy), METER_ID / 2 * scf, "轮廓", LW_C)
    circ(msp, (cx, cy), FL_PCD / 2 * scf, "中心线", LW_F, "CENTER")
    for i in range(FL_N):
        ang = math.radians(90 + i * 360 / FL_N)
        circ(msp, (cx + FL_PCD / 2 * scf * math.cos(ang), cy + FL_PCD / 2 * scf * math.sin(ang)), FL_HOLE / 2 * scf, "细实线", LW_F)
    circ(msp, (cx, cy + (FL_OD + METER_ID) / 4 * scf), 2.2, "轮廓", LW_C)
    line(msp, (cx - FL_OD / 2 * scf - 8, cy), (cx + FL_OD / 2 * scf + 8, cy), "中心线", LW_F, "CENTER")
    line(msp, (cx, cy - FL_OD / 2 * scf - 8), (cx, cy + FL_OD / 2 * scf + 8), "中心线", LW_F, "CENTER")
    dim_h(msp, cx - FL_PCD / 2 * scf, cx + FL_PCD / 2 * scf, cy - FL_OD / 2 * scf - 12, f"Ø{int(FL_PCD)}")
    T(msp, f"{FL_N}×Ø{int(FL_HOLE)}  {FL_BOLT}", 2.0, (cx, cy - FL_OD / 2 * scf - 24), TextEntityAlignment.TOP_CENTER, "标注")
    T(msp, f"RF Ø{int(FL_RF)}×{FL_RF_H}", 2.0, (cx, cy + FL_OD / 2 * scf + 10), TextEntityAlignment.BOTTOM_CENTER, "标注")
    T(msp, "Flange face view", 2.2, (cx, cy - FL_OD / 2 * scf - 38), TextEntityAlignment.TOP_CENTER)

    # 取压管大样 2:1
    sc2 = 2.0
    x0, y0 = ox + 30, oy + 95
    tl = TAP_L
    rect(msp, x0, y0 - TAP_OD * sc2 / 2, x0 + tl * sc2, y0 + TAP_OD * sc2 / 2, "轮廓", LW_C)
    id_ = TAP_OD - 2 * TAP_WALL
    line(msp, (x0, y0 - id_ * sc2 / 2), (x0 + tl * sc2, y0 - id_ * sc2 / 2), "虚线", LW_F, "DASHED")
    line(msp, (x0, y0 + id_ * sc2 / 2), (x0 + tl * sc2, y0 + id_ * sc2 / 2), "虚线", LW_F, "DASHED")
    line(msp, (x0 - 6, y0), (x0 + tl * sc2 + 6, y0), "中心线", LW_F, "CENTER")
    for x, sgn in ((x0, 1), (x0 + tl * sc2, -1)):
        line(msp, (x, y0 - TAP_OD * sc2 / 2), (x + sgn * 4, y0 - id_ * sc2 / 2), "轮廓", LW_C)
        line(msp, (x, y0 + TAP_OD * sc2 / 2), (x + sgn * 4, y0 + id_ * sc2 / 2), "轮廓", LW_C)
    dim_h(msp, x0, x0 + tl * sc2, y0 - TAP_OD * sc2 / 2 - 10, f"L={TAP_L}")
    dim_v(msp, x0 + tl * sc2 + 10, y0 - TAP_OD * sc2 / 2, y0 + TAP_OD * sc2 / 2, f"Ø{TAP_OD}×{TAP_WALL}", 1)
    T(msp, "Impulse pipe detail  2:1   Qty=2", 2.2, (x0 + tl * sc2 / 2, y0 + TAP_OD * sc2 / 2 + 12), TextEntityAlignment.BOTTOM_CENTER)

    table(
        msp,
        ox + 220,
        min(y_safe - 2, oy + 100),
        ["Flange notes", ""],
        [
            ["Std", "HG/T20592-2009 PN25 DN250 WN RF"],
            ["ID", f"Match pipe ID D={METER_ID}"],
            ["Taps", "Flange taps; deburr inside"],
            ["Weld", "Nipple to flange OD per WPS"],
            ["Face", "RF Ra3.2"],
            ["Qty", "1 upstream + 1 downstream"],
            ["Cryogenic", f"{TF_C}°C  solution anneal SS"],
        ],
        [40, 120],
        row_h=5.5,
        title="Notes",
        fs=1.7,
    )


def build():
    doc = setup()
    msp = doc.modelspace()
    sheet1(msp)
    sheet2(msp)
    sheet3(msp)
    zoom.extents(msp)
    DXF_DIR.mkdir(parents=True, exist_ok=True)
    path = DXF_DIR / f"{TAG}_EMCO风格_生产图.dxf"
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
        lineweight_scaling=1.0,
        min_lineweight=0.16,
        color_policy=ColorPolicy.BLACK,
        background_policy=BackgroundPolicy.WHITE,
    )
    with PdfPages(pdf_path) as pdf:
        for i in range(3):
            ox, oy = sheet_xy(i)
            fig = plt.figure(figsize=(16.54, 11.69))
            ax = fig.add_axes([0, 0, 1, 1])
            props = LayoutProperties.from_layout(msp)
            props.set_colors("#FFFFFF", "#000000")
            Frontend(ctx, MatplotlibBackend(ax), config=cfg).draw_layout(msp, finalize=False, layout_properties=props)
            ax.set_xlim(ox - 1, ox + A3W + 1)
            ax.set_ylim(oy - 1, oy + A3H + 1)
            ax.set_aspect("equal")
            ax.axis("off")
            pdf.savefig(fig, facecolor="white")
            plt.close(fig)
            print("page", i + 1)


def main():
    dxf = build()
    print("DXF", dxf)
    pdf = OUT / f"{TAG}_生产机加装配图_EMCO风格.pdf"
    export_pdf(dxf, pdf)
    print("PDF", pdf, pdf.stat().st_size)
    # 预览第1页
    import fitz

    doc = fitz.open(pdf)
    pix = doc[0].get_pixmap(matrix=fitz.Matrix(1.3, 1.3))
    prev = OUT / f"预览_{TAG}_EMCO_p1.png"
    pix.save(prev)
    print("PREVIEW", prev)


if __name__ == "__main__":
    main()
