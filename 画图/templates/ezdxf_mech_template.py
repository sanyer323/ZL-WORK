# -*- coding: utf-8 -*-
"""
机械 CAD ezdxf 成品模板（参数化 + 自动尺寸标注）
单位 mm，DXF R2013，兼容 AutoCAD / 浩辰 / 中望
用法：只改【参数区】→ python 本文件 → 用 CAD 打开 mech_part.dxf
"""
from pathlib import Path
import ezdxf
from ezdxf import units

# ===================== 参数区【仅修改这里】 =====================
WIDTH = 200        # 零件总长
HEIGHT = 120       # 零件总宽
HOLE_DIA = 12      # 安装孔直径
R = 5              # 外圆角半径
HOLE_OFFSET = 15   # 孔距离边缘距离
TEXT_HEIGHT = 3.5  # 标注文字高度
ARROW_SIZE = 2.5   # 标注箭头大小
OUT_FILE = Path(__file__).with_name("mech_part.dxf")
# =================================================================

doc = ezdxf.new("R2013")
doc.units = units.MM
msp = doc.modelspace()

doc.layers.add("轮廓", color=7, linetype="Continuous")
doc.layers.add("中心线", color=1, linetype="CENTER")
doc.layers.add("标注", color=3, linetype="Continuous")

if "MECH_STYLE" not in doc.dimstyles:
    dimstyle = doc.dimstyles.new("MECH_STYLE")
else:
    dimstyle = doc.dimstyles.get("MECH_STYLE")
dimstyle.dxf.dimtxt = TEXT_HEIGHT
dimstyle.dxf.dimasz = ARROW_SIZE

# 带圆角外轮廓（用直线近似圆角角点；复杂圆角请用 bulges 或 FILLET 后处理）
pts = [
    (0 + R, 0),
    (WIDTH - R, 0),
    (WIDTH, 0 + R),
    (WIDTH, HEIGHT - R),
    (WIDTH - R, HEIGHT),
    (0 + R, HEIGHT),
    (0, HEIGHT - R),
    (0, 0 + R),
]
msp.add_lwpolyline(pts, close=True, dxfattribs={"layer": "轮廓"})

for x, y in [
    (HOLE_OFFSET, HOLE_OFFSET),
    (WIDTH - HOLE_OFFSET, HOLE_OFFSET),
    (HOLE_OFFSET, HEIGHT - HOLE_OFFSET),
    (WIDTH - HOLE_OFFSET, HEIGHT - HOLE_OFFSET),
]:
    msp.add_circle((x, y), HOLE_DIA / 2, dxfattribs={"layer": "轮廓"})

msp.add_line((-15, HEIGHT / 2), (WIDTH + 15, HEIGHT / 2), dxfattribs={"layer": "中心线"})
msp.add_line((WIDTH / 2, -15), (WIDTH / 2, HEIGHT + 15), dxfattribs={"layer": "中心线"})

msp.add_linear_dim(
    base=(0, -12),
    p1=(0, 0),
    p2=(WIDTH, 0),
    dimstyle="MECH_STYLE",
    override={"layer": "标注"},
).render()

msp.add_linear_dim(
    base=(-12, 0),
    p1=(0, 0),
    p2=(0, HEIGHT),
    dimstyle="MECH_STYLE",
    override={"layer": "标注"},
).render()

doc.saveas(OUT_FILE)
print(f"OK: {OUT_FILE}")
