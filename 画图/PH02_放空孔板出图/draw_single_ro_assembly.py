# -*- coding: utf-8 -*-
"""
单级放空限流孔板 — 工业半剖结构图（ezdxf）
工作流：顶部参数区 → 规范图层 → DXF R2013 → CAD 打开 / PNG 预览

制图习惯：
- 上半：外形（螺栓、螺母可见）
- 下半：剖视（细剖面线，非实体填充）
- 中心线点划线；尺寸/球标/流向
"""
from __future__ import annotations

import math
from pathlib import Path

import ezdxf
from ezdxf import units, zoom
from ezdxf.enums import TextEntityAlignment
from ezdxf.math import Vec2

# ===================== 通径参数表【改尺寸只改这里】 =====================
DN_TABLE = {
    # dn: pipe_od, wall, id, fl_od, L, plate_thk, stub, tf(matching), tof(orifice fl)
    "DN50":  dict(pipe_od=60.3, wall=5.54, fl_od=165, L=360, H=10, stub=55, tf=22, tof=24, n_bolt=4),
    "DN80":  dict(pipe_od=88.9, wall=5.49, fl_od=210, L=390, H=12, stub=60, tf=26, tof=28, n_bolt=4),
    "DN100": dict(pipe_od=114.3, wall=6.02, fl_od=273, L=420, H=15, stub=70, tf=32, tof=34, n_bolt=4),
    "DN150": dict(pipe_od=168.3, wall=8.8, fl_od=356, L=480, H=20, stub=80, tf=38, tof=40, n_bolt=6),
    "DN200": dict(pipe_od=219.1, wall=8.18, fl_od=419, L=520, H=25, stub=90, tf=45, tof=48, n_bolt=6),
}

BORE_D = 25.0          # 选用孔径 mm
TEXT_H = 3.5
ARROW = 2.5
OUT_DIR = Path(__file__).resolve().parent
DXF_DIR = OUT_DIR / "DXF"
PNG_DIR = OUT_DIR / "结构图PNG"
# ========================================================================

LW_C = 50   # 粗实线 0.50mm
LW_F = 18   # 细实线
LW_H = 13   # 剖面线


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
    ]:
        if name not in doc.layers:
            doc.layers.add(name, color=color, linetype=lt, lineweight=lw)
    if "CENTER" not in doc.linetypes:
        doc.linetypes.add("CENTER", pattern="A,.9,-.05,.09,-.05")
    if "DASHED" not in doc.linetypes:
        doc.linetypes.add("DASHED", pattern="A,.5,-.25")
    # 中文字体：必须用文件名（如 simhei.ttf）；完整路径会被回退成 Arial
    if "CN" not in doc.styles:
        doc.styles.add("CN", font="simhei.ttf")
    else:
        doc.styles.get("CN").dxf.font = "simhei.ttf"
    doc.styles.get("Standard").dxf.font = "simhei.ttf"
    # dim style
    if "MECH" not in doc.dimstyles:
        ds = doc.dimstyles.new("MECH")
        ds.dxf.dimtxt = TEXT_H
        ds.dxf.dimasz = ARROW
        ds.dxf.dimexe = 1.5
        ds.dxf.dimexo = 1.0
        ds.dxf.dimgap = 1.0
    return doc


def _hatch_lines(msp, x0, y0, x1, y1, step=4.0, angle_deg=45.0):
    """在矩形区域内画细剖面线（避免 hatch 实体渲染成黑块）。仅画 y<=0 的下半。"""
    y0 = min(y0, 0)
    y1 = min(y1, 0)
    if y1 <= y0:
        return
    ang = math.radians(angle_deg)
    dx, dy = math.cos(ang), math.sin(ang)
    # 覆盖矩形的一组平行线：沿法向推进
    nx, ny = -dy, dx
    # 投影范围
    corners = [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]
    projs = [c[0] * nx + c[1] * ny for c in corners]
    pmin, pmax = min(projs), max(projs)
    # 线段方向跨度
    t_span = abs((x1 - x0) * dx) + abs((y1 - y0) * dy) + 50

    def clip_seg(p1, p2):
        # Liang-Barsky clip to rect
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
        # 线上一点：原点沿法向 p
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


def _balloon(msp, x, y, bx, by, txt):
    msp.add_line((x, y), (bx, by), dxfattribs={"layer": "标注", "lineweight": LW_F})
    msp.add_circle((bx, by), 4.2, dxfattribs={"layer": "轮廓", "lineweight": LW_C})
    _txt(msp, str(txt), 3.2, (bx, by), TextEntityAlignment.MIDDLE_CENTER)


def _arrow_h(msp, tip_x, y, direction):
    """空心箭头，避免 SOLID 填充。direction: +1 向右尖, -1 向左尖"""
    s = 3.0
    msp.add_line((tip_x, y), (tip_x - direction * s, y + 1.1), dxfattribs={"layer": "标注", "lineweight": LW_F})
    msp.add_line((tip_x, y), (tip_x - direction * s, y - 1.1), dxfattribs={"layer": "标注", "lineweight": LW_F})


def _dim_h(msp, x0, x1, y, label):
    msp.add_line((x0, y), (x1, y), dxfattribs={"layer": "标注", "lineweight": LW_F})
    for x in (x0, x1):
        msp.add_line((x, y - 2), (x, y + 2), dxfattribs={"layer": "标注", "lineweight": LW_F})
    _arrow_h(msp, x0, y, -1)
    _arrow_h(msp, x1, y, +1)
    _txt(msp, label, TEXT_H, ((x0 + x1) / 2, y + 2.2), TextEntityAlignment.BOTTOM_CENTER)


def _dim_v(msp, x, y0, y1, label, side=-1):
    msp.add_line((x, y0), (x, y1), dxfattribs={"layer": "标注", "lineweight": LW_F})
    for y in (y0, y1):
        msp.add_line((x - 2, y), (x + 2, y), dxfattribs={"layer": "标注", "lineweight": LW_F})
    s = 3.0
    msp.add_line((x, y0), (x - 1.1, y0 + s), dxfattribs={"layer": "标注", "lineweight": LW_F})
    msp.add_line((x, y0), (x + 1.1, y0 + s), dxfattribs={"layer": "标注", "lineweight": LW_F})
    msp.add_line((x, y1), (x - 1.1, y1 - s), dxfattribs={"layer": "标注", "lineweight": LW_F})
    msp.add_line((x, y1), (x + 1.1, y1 - s), dxfattribs={"layer": "标注", "lineweight": LW_F})
    _txt(msp, label, TEXT_H, (x + 5.5 * side, (y0 + y1) / 2), TextEntityAlignment.MIDDLE_CENTER, rot=90)


def draw_single(dn: str) -> tuple[Path, Path]:
    p = DN_TABLE[dn]
    pipe_od = p["pipe_od"]
    pipe_id = pipe_od - 2 * p["wall"]
    fl = p["fl_od"]
    H = p["H"]
    stub = p["stub"]
    tf = p["tf"]
    tof = p["tof"]
    bore = BORE_D
    L = p["L"]

    doc = _setup_doc()
    msp = doc.modelspace()

    thick = {"layer": "轮廓", "lineweight": LW_C}
    thin = {"layer": "细实线", "lineweight": LW_F}
    dash = {"layer": "虚线", "lineweight": LW_F, "linetype": "DASHED"}
    cen = {"layer": "中心线", "lineweight": LW_F, "linetype": "CENTER"}

    # ---- X 布局（从左到右）----
    x0 = 0.0
    x_stub1_r = stub
    x_mf1 = x_stub1_r
    x_of1 = x_mf1 + tf + 1.5
    x_pl = x_of1 + tof + 1.5
    x_of2 = x_pl + H + 1.5
    x_mf2 = x_of2 + tof + 1.5
    x_stub2_l = x_mf2 + tf
    x_end = x_stub2_l + stub

    # 中心线
    msp.add_line((-25, 0), (x_end + 25, 0), dxfattribs=cen)

    # ---- 接管 ----
    def pipe(xa, xb):
        msp.add_line((xa, pipe_od / 2), (xb, pipe_od / 2), dxfattribs=thick)
        msp.add_line((xa, -pipe_od / 2), (xb, -pipe_od / 2), dxfattribs=thick)
        msp.add_line((xa, pipe_id / 2), (xb, pipe_id / 2), dxfattribs=dash)
        msp.add_line((xa, -pipe_id / 2), (xb, -pipe_id / 2), dxfattribs=dash)
        # 下半管壁剖面线
        _hatch_lines(msp, xa, -pipe_od / 2, xb, -pipe_id / 2, step=3.5)

    pipe(x0, x_stub1_r)
    pipe(x_stub2_l, x_end)

    # ---- 法兰（半剖：整圈外形 + 下半剖面）----
    def rect_outline(xa, ya, xb, yb):
        """仅轮廓线，禁止 close 填充（matplotlib 后端会把闭合多段线涂黑）。"""
        msp.add_line((xa, ya), (xb, ya), dxfattribs=thick)
        msp.add_line((xb, ya), (xb, yb), dxfattribs=thick)
        msp.add_line((xb, yb), (xa, yb), dxfattribs=thick)
        msp.add_line((xa, yb), (xa, ya), dxfattribs=thick)

    def flange(xa, thk, fod, bore_r):
        rect_outline(xa, fod / 2, xa + thk, -fod / 2)
        msp.add_line((xa, bore_r), (xa + thk, bore_r), dxfattribs=thin)
        msp.add_line((xa, -bore_r), (xa + thk, -bore_r), dxfattribs=thin)
        rf = min(2.5, thk * 0.1)
        msp.add_line((xa + thk - rf, fod * 0.16), (xa + thk, fod * 0.16), dxfattribs=thin)
        msp.add_line((xa + thk - rf, -fod * 0.16), (xa + thk, -fod * 0.16), dxfattribs=thin)
        msp.add_circle((xa + thk / 2, fod * 0.33), 3.8, dxfattribs=thin)
        msp.add_circle((xa + thk / 2, -fod * 0.33), 3.8, dxfattribs=dash)
        _hatch_lines(msp, xa, -fod / 2, xa + thk, -bore_r, step=5.5)

    flange(x_mf1, tf, fl, pipe_id / 2)
    flange(x_of1, tof, fl * 0.98, pipe_id / 2)
    flange(x_of2, tof, fl * 0.98, pipe_id / 2)
    flange(x_mf2, tf, fl, pipe_id / 2)

    # ---- 孔板 ----
    pod = fl * 0.70
    rect_outline(x_pl, pod / 2, x_pl + H, -pod / 2)
    _hatch_lines(msp, x_pl, -pod / 2, x_pl + H, 0, step=4.5)
    br = bore / 2
    msp.add_line((x_pl, br), (x_pl, -br), dxfattribs=thick)
    msp.add_line((x_pl, br), (x_pl + H, br * 0.72), dxfattribs=thick)
    msp.add_line((x_pl, -br), (x_pl + H, -br * 0.72), dxfattribs=thick)
    msp.add_line((x_pl + H, br * 0.72), (x_pl + H, -br * 0.72), dxfattribs=thick)
    msp.add_line((x_pl + H / 2, -br - 8), (x_pl + H / 2, br + 8), dxfattribs=cen)

    # 铭牌/手柄
    hx = x_pl + H / 2
    msp.add_line((hx, pod / 2), (hx, pod / 2 + 32), dxfattribs=thick)
    rect_outline(hx - 11, pod / 2 + 50, hx + 20, pod / 2 + 32)
    _txt(msp, "3", 4.0, (hx + 4.5, pod / 2 + 41), TextEntityAlignment.MIDDLE_CENTER)

    # ---- 螺柱/螺母 ----
    def stud(xa, xb, y):
        msp.add_line((xa, y), (xb, y), dxfattribs=thick)
        for xx in (xa, xb):
            rect_outline(xx - 3.5, y + 4.5, xx + 3.5, y - 4.5)

    yb = fl * 0.34
    stud(x_mf1 + 3, x_mf2 + tf - 3, yb)
    stud(x_mf1 + 3, x_mf2 + tf - 3, -yb)

    # ---- 球标 ----
    _balloon(msp, x_mf1 + tf / 2, -fl / 2, x_mf1 + tf / 2 - 8, -fl / 2 - 26, "1")
    _balloon(msp, x_of1 + tof / 2, -fl / 2, x_of1 + tof / 2 + 12, -fl / 2 - 26, "2")
    _balloon(msp, x_pl + H / 2, -pod / 2, x_pl + H / 2, -fl / 2 - 26, "3")
    _balloon(msp, x_mf2 + tf / 2, yb, x_mf2 + tf + 22, yb + 20, "B1")
    _balloon(msp, (x_mf1 + x_mf2 + tf) / 2, yb, (x_mf1 + x_mf2 + tf) / 2, yb + 26, "B2")
    _balloon(msp, x_pl, -pipe_id / 2 - 2, x_pl - 18, -fl * 0.22, "B3")

    # ---- 尺寸 ----
    _dim_h(msp, x_mf1, x_stub2_l, -fl / 2 - 48, f"≈{int(L)}")
    _dim_v(msp, x0 - 16, -fl / 2, fl / 2, f"Φ{int(fl)}", side=-1)
    _dim_v(msp, x_end + 16, -fl / 2, fl / 2, f"Φ{int(fl)}", side=1)
    _txt(
        msp,
        f"Φ{pipe_od}×{p['wall']}",
        TEXT_H,
        ((x0 + x_stub1_r) / 2, pipe_od / 2 + 9),
        TextEntityAlignment.BOTTOM_CENTER,
    )
    _txt(
        msp,
        f"Φ{pipe_od}×{p['wall']}",
        TEXT_H,
        ((x_stub2_l + x_end) / 2, pipe_od / 2 + 9),
        TextEntityAlignment.BOTTOM_CENTER,
    )
    _txt(msp, f"Φ{BORE_D:.0f}", TEXT_H, (x_pl + H + 14, 0), TextEntityAlignment.MIDDLE_LEFT)

    # 流向
    yf = -fl / 2 - 68
    msp.add_line((x_mf1 + 10, yf), (x_stub2_l - 15, yf), dxfattribs=thick)
    msp.add_line((x_stub2_l - 15, yf), (x_stub2_l - 26, yf + 3.5), dxfattribs=thick)
    msp.add_line((x_stub2_l - 15, yf), (x_stub2_l - 26, yf - 3.5), dxfattribs=thick)
    _txt(
        msp,
        "介质流向",
        4.5,
        ((x_mf1 + x_stub2_l) / 2, yf - 7),
        TextEntityAlignment.TOP_CENTER,
    )

    _txt(
        msp,
        f"单级限流孔板  LG-XLKB-CL600-{dn}-1",
        5.5,
        ((x0 + x_end) / 2, fl / 2 + 66),
        TextEntityAlignment.BOTTOM_CENTER,
    )
    _txt(
        msp,
        f"孔径 Φ{BORE_D:.0f}  孔板316L  法兰CL600/A105  H={H}  {dn}",
        4.0,
        ((x0 + x_end) / 2, fl / 2 + 55),
        TextEntityAlignment.BOTTOM_CENTER,
    )

    # 明细提示
    _txt(
        msp,
        "1配对法兰  2孔板法兰  3孔板  B1螺母  B2全螺纹螺柱  B3金属缠绕垫",
        3.2,
        ((x0 + x_end) / 2, yf - 18),
        TextEntityAlignment.TOP_CENTER,
    )

    zoom.extents(msp)
    DXF_DIR.mkdir(parents=True, exist_ok=True)
    PNG_DIR.mkdir(parents=True, exist_ok=True)
    dxf_path = DXF_DIR / f"结构图_{dn}_单级.dxf"
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
    fig = plt.figure(figsize=(13.5, 7.2), dpi=220)
    ax = fig.add_axes([0.01, 0.01, 0.98, 0.98])
    ctx = RenderContext(doc)
    # min_lineweight 单位 mm；过大（如 8）会把法兰/螺柱涂成实心黑块
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
    fig.savefig(png_path, dpi=220, facecolor="white", bbox_inches="tight", pad_inches=0.12)
    plt.close(fig)


def main():
    paths = {}
    for dn in DN_TABLE:
        dxf = draw_single(dn)
        png = PNG_DIR / f"结构图_{dn}_单级.png"
        render_png(dxf, png)
        paths[dn] = png
        print("OK", dn, dxf.name, "->", png.name, f"{png.stat().st_size}B")
    # 预览
    from shutil import copy2

    copy2(paths["DN100"], OUT_DIR / "预览_单级_DN100.png")
    print("preview", OUT_DIR / "预览_单级_DN100.png")
    return paths


if __name__ == "__main__":
    main()
