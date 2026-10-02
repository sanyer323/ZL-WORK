# -*- coding: utf-8 -*-
"""EA10 传感布置：输出轴编码干腔 + 蜗杆力矩垫圈。"""
from __future__ import annotations

from pathlib import Path

import ezdxf
from ezdxf import units, zoom
from ezdxf.enums import TextEntityAlignment

OUT = Path(__file__).resolve().parent
DXF_DIR = OUT / "DXF"
LW_C, LW_F = 50, 18


def setup():
    doc = ezdxf.new("R2013", setup=True)
    doc.units = units.MM
    doc.header["$INSUNITS"] = 4
    for n, c, lw, lt in [
        ("轮廓", 7, LW_C, "Continuous"),
        ("细实线", 7, LW_F, "Continuous"),
        ("中心线", 1, LW_F, "CENTER"),
        ("标注", 3, LW_F, "Continuous"),
        ("文字", 7, LW_F, "Continuous"),
    ]:
        if n not in doc.layers:
            doc.layers.add(n, color=c, linetype=lt, lineweight=lw)
    if "CENTER" not in doc.linetypes:
        doc.linetypes.add("CENTER", pattern="A,.9,-.05,.09,-.05")
    if "CN" not in doc.styles:
        doc.styles.add("CN", font="DroidSansFallbackFull.ttf")
    return doc


def T(msp, s, h, xy, a=TextEntityAlignment.LEFT):
    t = msp.add_text(str(s), height=h, dxfattribs={"layer": "文字", "style": "CN"})
    t.set_placement(xy, align=a)
    return t


def box(msp, xa, ya, xb, yb, layer="轮廓"):
    msp.add_line((xa, ya), (xb, ya), dxfattribs={"layer": layer, "lineweight": LW_C if layer == "轮廓" else LW_F})
    msp.add_line((xb, ya), (xb, yb), dxfattribs={"layer": layer, "lineweight": LW_C if layer == "轮廓" else LW_F})
    msp.add_line((xb, yb), (xa, yb), dxfattribs={"layer": layer, "lineweight": LW_C if layer == "轮廓" else LW_F})
    msp.add_line((xa, yb), (xa, ya), dxfattribs={"layer": layer, "lineweight": LW_C if layer == "轮廓" else LW_F})


def dimv(msp, x, y0, y1, label):
    msp.add_line((x, y0), (x, y1), dxfattribs={"layer": "标注", "lineweight": LW_F})
    T(msp, label, 3.0, (x + 4, (y0 + y1) / 2))


def draw():
    doc = setup()
    msp = doc.modelspace()
    cen = {"layer": "中心线", "lineweight": LW_F, "linetype": "CENTER"}

    # --- 左：编码干腔（输出轴竖直）---
    msp.add_line((0, -20), (0, 85), dxfattribs=cen)
    box(msp, -28, -8, 28, 12)  # 6010 示意
    T(msp, "6010", 2.8, (32, 2))
    box(msp, -16, 12, 16, 20, "细实线")  # 轴颈 φ20
    box(msp, -16, 20, 16, 27, "细实线")  # FB 油封
    T(msp, "FB20x32x7 oil", 2.6, (32, 23))
    box(msp, -4, 28, 4, 30.5)  # 磁铁 8x2.5
    T(msp, "mag 8x2.5", 2.6, (32, 29))
    box(msp, -12, 31.5, 12, 36)  # 气隙+芯片
    T(msp, "AS5047P gap 1.0", 2.6, (32, 34))
    box(msp, -22, 36, 22, 52, "细实线")  # 韦根模组
    T(msp, "Wiegand MT", 2.6, (32, 44))
    box(msp, -40, 12, 40, 70)  # 干腔壁
    T(msp, "dry cavity", 3.0, (-38, 62))
    dimv(msp, -48, 30.5, 31.5, "1.0")
    T(msp, "A  encoder on output", 4.0, (0, 78), TextEntityAlignment.BOTTOM_CENTER)

    # --- 右：力矩垫圈（蜗杆水平）---
    ox = 160
    msp.add_line((ox - 50, 20), (ox + 90, 20), dxfattribs=cen)
    box(msp, ox, 10, ox + 70, 30)  # 轴 φ20
    box(msp, ox + 8, 0, ox + 22, 40)  # 7204
    T(msp, "7204AC", 2.6, (ox + 10, 44))
    box(msp, ox + 22, 0, ox + 30, 40)  # 垫圈厚 8
    T(msp, "washer 0-1kN", 2.6, (ox + 18, -8))
    box(msp, ox + 30, -4, ox + 38, 44)  # 箱体
    T(msp, "housing", 2.6, (ox + 30, 50))
    T(msp, "B  torque washer on worm", 4.0, (ox + 20, 78), TextEntityAlignment.BOTTOM_CENTER)
    T(msp, "ID21 OD42 t=8  2.0 mV/V", 2.8, (ox + 20, -20), TextEntityAlignment.BOTTOM_CENTER)

    T(msp, "EA10 sensors  Step 5   position and torque independent", 5.0, (80, 95), TextEntityAlignment.BOTTOM_CENTER)

    zoom.extents(msp)
    DXF_DIR.mkdir(parents=True, exist_ok=True)
    p = DXF_DIR / "EA10_传感布置.dxf"
    doc.saveas(p)
    return p


def render(dxf_path: Path, png: Path):
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
    doc = ezdxf.readfile(dxf_path)
    fig = plt.figure(figsize=(11, 5.5), dpi=160)
    ax = fig.add_axes([0.02, 0.02, 0.96, 0.96])
    cfg = Configuration.defaults().with_changes(
        lineweight_scaling=0.9,
        min_lineweight=0.2,
        color_policy=ColorPolicy.BLACK,
        background_policy=BackgroundPolicy.WHITE,
    )
    props = LayoutProperties.from_layout(doc.modelspace())
    props.set_colors("#FFFFFF", "#000000")
    Frontend(RenderContext(doc), MatplotlibBackend(ax), config=cfg).draw_layout(
        doc.modelspace(), finalize=True, layout_properties=props
    )
    ax.set_aspect("equal")
    fig.savefig(png, dpi=160, facecolor="white", bbox_inches="tight")
    plt.close(fig)


def main():
    dxf = draw()
    png = OUT / "EA10_传感布置.png"
    render(dxf, png)
    print("OK", dxf.name, png.name)


if __name__ == "__main__":
    main()
