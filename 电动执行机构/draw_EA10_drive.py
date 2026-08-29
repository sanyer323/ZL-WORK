# -*- coding: utf-8 -*-
"""EA10 传动剖视（Step 4）：蜗杆轴 + 输出轴/F10 螺母。F10 型 A φ20 已冻结。"""
from __future__ import annotations

import math
from pathlib import Path

import ezdxf
from ezdxf import units, zoom
from ezdxf.enums import TextEntityAlignment

# ===================== 参数区 =====================
M, Z1, Z2, Q = 2.5, 1, 70, 16.0
D1, D2 = Q * M, M * Z2
A = 0.5 * (D1 + D2)
R1, R2 = D1 / 2, D2 / 2
B_FACE = 28.0
NUT_L, STEM, HOLLOW_ID = 100.0, 20.0, 22.0
F10_OD, F10_PCD, F10_SPIG, F10_THK = 125.0, 102.0, 70.0, 22.0
TEXT_H = 3.5
OUT = Path(__file__).resolve().parent
DXF_DIR = OUT / "DXF"
LW_C, LW_F, LW_H = 50, 18, 13
# =================================================


def setup():
    doc = ezdxf.new("R2013", setup=True)
    doc.units = units.MM
    doc.header["$INSUNITS"] = 4
    for name, color, lw, lt in [
        ("轮廓", 7, LW_C, "Continuous"),
        ("细实线", 7, LW_F, "Continuous"),
        ("中心线", 1, LW_F, "CENTER"),
        ("虚线", 8, LW_F, "DASHED"),
        ("剖面线", 8, LW_H, "Continuous"),
        ("标注", 3, LW_F, "Continuous"),
        ("文字", 7, LW_F, "Continuous"),
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


def hatch_rect(msp, x0, y0, x1, y1, step=5.0):
    x0, x1 = min(x0, x1), max(x0, x1)
    y0, y1 = min(y0, y1), max(y0, y1)
    if y1 - y0 < 0.8 or x1 - x0 < 0.8:
        return
    ang = math.radians(45)
    dx, dy = math.cos(ang), math.sin(ang)
    nx, ny = -dy, dx
    corners = [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]
    projs = [c[0] * nx + c[1] * ny for c in corners]
    span = abs((x1 - x0) * dx) + abs((y1 - y0) * dy) + 40

    def clip(p1, p2):
        ddx, ddy = p2[0] - p1[0], p2[1] - p1[1]
        t0, t1 = 0.0, 1.0
        for p, q in (
            (-ddx, p1[0] - x0),
            (ddx, x1 - p1[0]),
            (-ddy, p1[1] - y0),
            (ddy, y1 - p1[1]),
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

    p = min(projs) - step
    while p <= max(projs) + step:
        cx, cy = nx * p, ny * p
        c = clip((cx - dx * span, cy - dy * span), (cx + dx * span, cy + dy * span))
        if c:
            msp.add_line(c[0], c[1], dxfattribs={"layer": "剖面线", "lineweight": LW_H})
        p += step


def balloon(msp, x, y, bx, by, n):
    msp.add_line((x, y), (bx, by), dxfattribs={"layer": "标注", "lineweight": LW_F})
    msp.add_circle((bx, by), 4.5, dxfattribs={"layer": "轮廓", "lineweight": LW_C})
    txt(msp, n, 3.2, (bx, by), TextEntityAlignment.MIDDLE_CENTER)


def dim_h(msp, x0, x1, y, label):
    msp.add_line((x0, y), (x1, y), dxfattribs={"layer": "标注", "lineweight": LW_F})
    for x in (x0, x1):
        msp.add_line((x, y - 2), (x, y + 2), dxfattribs={"layer": "标注", "lineweight": LW_F})
    txt(msp, label, TEXT_H, ((x0 + x1) / 2, y + 2.2), TextEntityAlignment.BOTTOM_CENTER, layer="标注")


def dim_v(msp, x, y0, y1, label, side=-1):
    msp.add_line((x, y0), (x, y1), dxfattribs={"layer": "标注", "lineweight": LW_F})
    txt(
        msp,
        label,
        TEXT_H,
        (x + 6.2 * side, (y0 + y1) / 2),
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

    # ----- 视图一：蜗杆轴纵剖（水平，原点在啮合）-----
    msp.add_line((-160, 0), (150, 0), dxfattribs=cen)
    msp.add_line((0, 55), (0, -A - 160), dxfattribs=cen)

    # 蜗杆螺纹段
    xt0, xt1 = -36, 36
    tip, root = R1 + M, R1 - 1.2 * M
    rect(msp, xt0, -tip, xt1, tip)
    msp.add_line((xt0, root), (xt1, root), dxfattribs=thin)
    msp.add_line((xt0, -root), (xt1, -root), dxfattribs=thin)
    hatch_rect(msp, xt0, -root, xt1, root, step=4.0)
    x = xt0 + 3
    while x < xt1 - 3:
        msp.add_line((x, tip), (x + 4.5, root), dxfattribs=thin)
        msp.add_line((x, -tip), (x + 4.5, -root), dxfattribs=thin)
        x += 6

    # 轴伸 φ20 + 7204（20x47x14）
    def bearing_7204(xmid, label_y=38):
        rect(msp, xmid - 7, -23.5, xmid + 7, 23.5)
        hatch_rect(msp, xmid - 7, -23.5, xmid + 7, 23.5, step=3.2)
        txt(msp, "7204AC", 2.6, (xmid, label_y), TextEntityAlignment.BOTTOM_CENTER)

    bearing_7204(-58)
    bearing_7204(58)
    # 轴 φ20
    msp.add_line((-120, 10), (95, 10), dxfattribs=thick)
    msp.add_line((-120, -10), (95, -10), dxfattribs=thick)
    hatch_rect(msp, -120, -10, 95, 10, step=4.5)

    # 力矩垫圈
    rect(msp, -78, -24, -70, 24)
    hatch_rect(msp, -78, -24, -70, 24, step=2.8)
    txt(msp, "力矩垫", 2.6, (-74, -32), TextEntityAlignment.TOP_CENTER)

    # 锤击牙嵌（电机侧）
    rect(msp, 72, -16, 88, 16)
    msp.add_line((80, -16), (80, 16), dxfattribs=dash)
    txt(msp, "牙嵌 12 deg", 2.6, (80, -28), TextEntityAlignment.TOP_CENTER)

    # 油封
    rect(msp, 90, -16, 97, 16, layer="细实线", lw=LW_F)
    rect(msp, -97, -16, -90, 16, layer="细实线", lw=LW_F)
    txt(msp, "FB20x32x7", 2.5, (93.5, 28), TextEntityAlignment.BOTTOM_CENTER)

    # 离合器滑套 + 手轮毂
    rect(msp, -132, -22, -100, 22)
    hatch_rect(msp, -132, -22, -100, 22, step=3.5)
    txt(msp, "离合滑套", 2.6, (-116, 30), TextEntityAlignment.BOTTOM_CENTER)
    msp.add_circle((-155, 0), 28, dxfattribs=thick)
    txt(msp, "手轮毂", 2.6, (-155, -38), TextEntityAlignment.TOP_CENTER)

    # 蜗轮（圆）
    msp.add_circle((0, -A), R2 + M, dxfattribs=thick)
    msp.add_circle((0, -A), R2, dxfattribs={**thin, "linetype": "CENTER"})
    msp.add_circle((0, -A), 25, dxfattribs=thin)
    txt(msp, "ZCuSn10P1  z2=70", 2.8, (52, -A), TextEntityAlignment.MIDDLE_LEFT)

    # ----- 输出轴叠层（竖直，与蜗轮同心）-----
    y_enc = -A + 70
    y_brg_u = -A + 48
    y_hub_top = -A + B_FACE / 2
    y_hub_bot = -A - B_FACE / 2
    y_brg_l = -A - 55
    y_nut_top = -A - 75
    y_nut_bot = y_nut_top - NUT_L
    y_thk_top = y_nut_bot - 2
    y_thk_bot = y_thk_top - 22  # 81210
    y_f10_top = y_thk_bot - 8
    y_f10_bot = y_f10_top - F10_THK

    # 空心轴外径 50 / 内 22
    msp.add_line((-25, y_enc), (-25, y_f10_top), dxfattribs=thick)
    msp.add_line((25, y_enc), (25, y_f10_top), dxfattribs=thick)
    msp.add_line((-HOLLOW_ID / 2, y_enc), (-HOLLOW_ID / 2, y_f10_bot - 6), dxfattribs=dash)
    msp.add_line((HOLLOW_ID / 2, y_enc), (HOLLOW_ID / 2, y_f10_bot - 6), dxfattribs=dash)
    msp.add_line((-STEM / 2, y_enc + 8), (-STEM / 2, y_f10_bot - 10), dxfattribs=dash)
    msp.add_line((STEM / 2, y_enc + 8), (STEM / 2, y_f10_bot - 10), dxfattribs=dash)

    # 编码磁环
    rect(msp, -30, y_enc, 30, y_enc + 12, layer="细实线", lw=LW_F)
    txt(msp, "编码磁环", 2.6, (36, y_enc + 6), TextEntityAlignment.MIDDLE_LEFT)

    def brg_6010(y):
        rect(msp, -40, y, 40, y + 16)
        hatch_rect(msp, -40, y, -25, y + 16, step=3.0)
        hatch_rect(msp, 25, y, 40, y + 16, step=3.0)
        txt(msp, "6010", 2.6, (46, y + 8), TextEntityAlignment.MIDDLE_LEFT)

    brg_6010(y_brg_u)
    brg_6010(y_brg_l)

    # 轮毂
    rect(msp, -35, y_hub_bot, 35, y_hub_top, layer="细实线", lw=LW_F)
    hatch_rect(msp, -35, y_hub_bot, -25, y_hub_top, step=3.5)
    hatch_rect(msp, 25, y_hub_bot, 35, y_hub_top, step=3.5)

    # 螺母 Tr20x4 L=100
    rect(msp, -18, y_nut_bot, 18, y_nut_top)
    hatch_rect(msp, -18, y_nut_bot, -HOLLOW_ID / 2, y_nut_top, step=3.2)
    hatch_rect(msp, HOLLOW_ID / 2, y_nut_bot, 18, y_nut_top, step=3.2)
    txt(msp, "Tr20x4  L=100  ZCuAl10Fe3", 2.8, (42, (y_nut_top + y_nut_bot) / 2), TextEntityAlignment.MIDDLE_LEFT)

    # 81210
    rect(msp, -39, y_thk_bot, 39, y_thk_top)
    hatch_rect(msp, -39, y_thk_bot, 39, y_thk_top, step=3.0)
    txt(msp, "81210  thrust", 2.6, (46, (y_thk_top + y_thk_bot) / 2), TextEntityAlignment.MIDDLE_LEFT)

    # F10 法兰
    rect(msp, -F10_OD / 2, y_f10_bot, F10_OD / 2, y_f10_top)
    hatch_rect(msp, -F10_OD / 2, y_f10_bot, F10_OD / 2, y_f10_top, step=4.0)
    rect(msp, -F10_SPIG / 2, y_f10_bot - 3, F10_SPIG / 2, y_f10_bot, layer="细实线", lw=LW_F)
    for sgn in (-1, 1):
        msp.add_circle((sgn * F10_PCD / 2, (y_f10_top + y_f10_bot) / 2), 5.5, dxfattribs=thin)

    dim_v(msp, -48, 0, -A, f"a={A:.1f}", side=-1)
    dim_v(msp, 22, y_nut_bot, y_nut_top, "100", side=1)
    dim_h(msp, -F10_OD / 2, F10_OD / 2, y_f10_bot - 18, f"F10 d1={F10_OD:.0f}")
    dim_h(msp, -STEM / 2, STEM / 2, y_f10_bot - 32, f"stem {STEM:.0f}")

    balloon(msp, 36, 0, 120, 48, "1")
    balloon(msp, -74, 24, -74, 58, "2")
    balloon(msp, 80, 16, 120, 16, "3")
    balloon(msp, -116, 22, -116, 58, "4")
    balloon(msp, 40, -A, 120, -A + 20, "5")
    balloon(msp, 18, (y_nut_top + y_nut_bot) / 2, 120, (y_nut_top + y_nut_bot) / 2, "6")
    balloon(msp, 39, (y_thk_top + y_thk_bot) / 2, 120, y_thk_bot - 10, "7")
    balloon(msp, F10_OD / 2, y_f10_top, 120, y_f10_top + 8, "8")
    balloon(msp, 40, y_brg_u + 8, 120, y_brg_u + 8, "9")

    txt(msp, "EA10 传动剖视  Step 4  ISO 5210 F10 type A  stem 20 mm", 5.5, (0, 78), TextEntityAlignment.BOTTOM_CENTER)
    txt(msp, "100 Nm -> stem thrust 57.8 kN   breakout 86.6 kN   nut L=100 Al-bronze", 3.2, (0, 68), TextEntityAlignment.BOTTOM_CENTER)

    bom = [
        "1 worm 20CrMnTi m=2.5 z1=1",
        "2 torque washer 0-1 kN",
        "3 hammerblow jaws 12 deg",
        "4 handwheel clutch sleeve",
        "5 wheel ZCuSn10P1 z2=70",
        "6 stem nut Tr20x4 L=100",
        "7 thrust 81210",
        "8 F10 base 4xM10",
        "9 radial 6010 / worm 7204AC",
    ]
    bx = 175
    by = 50
    rect(msp, bx - 6, by - 12 * len(bom) - 10, bx + 175, by + 14, layer="细实线", lw=LW_F)
    txt(msp, "BOM", 3.5, (bx, by + 4))
    for i, line in enumerate(bom):
        txt(msp, line, 2.8, (bx, by - 12 - i * 12))

    notes = [
        "F10 frozen: do not change to F14.",
        "Stem max 20 mm. Nut interchangeable, envelope fixed.",
        "Do not raise rated torque on F10.",
        "Step 5: encoder chip and torque cal.",
    ]
    ny = y_f10_bot - 50
    for i, line in enumerate(notes):
        txt(msp, line, 3.0, (-160, ny - i * 8))

    zoom.extents(msp)
    DXF_DIR.mkdir(parents=True, exist_ok=True)
    path = DXF_DIR / "EA10_传动剖视.dxf"
    doc.saveas(path)
    return path


def render_png(dxf_path: Path, png_path: Path):
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib import font_manager
    from ezdxf.addons.drawing import Frontend, RenderContext
    from ezdxf.addons.drawing.config import BackgroundPolicy, ColorPolicy, Configuration
    from ezdxf.addons.drawing.matplotlib import MatplotlibBackend
    from ezdxf.addons.drawing.properties import LayoutProperties

    for fp in (
        "/usr/share/fonts/truetype/wqy/wqy-microhei.ttc",
        "/usr/share/fonts/truetype/droid/DroidSansFallbackFull.ttf",
    ):
        if Path(fp).exists():
            font_manager.fontManager.addfont(fp)
    plt.rcParams["font.sans-serif"] = ["WenQuanYi Micro Hei", "Droid Sans Fallback"]
    plt.rcParams["axes.unicode_minus"] = False
    doc = ezdxf.readfile(dxf_path)
    fig = plt.figure(figsize=(14, 11), dpi=170)
    ax = fig.add_axes([0.01, 0.01, 0.98, 0.98])
    cfg = Configuration.defaults().with_changes(
        lineweight_scaling=0.85,
        min_lineweight=0.18,
        color_policy=ColorPolicy.BLACK,
        background_policy=BackgroundPolicy.WHITE,
    )
    props = LayoutProperties.from_layout(doc.modelspace())
    props.set_colors("#FFFFFF", "#000000")
    Frontend(RenderContext(doc), MatplotlibBackend(ax), config=cfg).draw_layout(
        doc.modelspace(), finalize=True, layout_properties=props
    )
    ax.set_aspect("equal")
    fig.savefig(png_path, dpi=170, facecolor="white", bbox_inches="tight", pad_inches=0.12)
    plt.close(fig)


def main():
    dxf = draw()
    png = OUT / "EA10_传动剖视.png"
    render_png(dxf, png)
    print("OK", dxf.name, png.name, png.stat().st_size)


if __name__ == "__main__":
    main()
