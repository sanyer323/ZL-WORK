# -*- coding: utf-8 -*-
"""Generate 公司业务一页纸.pdf from structured content."""
from pathlib import Path

from fpdf import FPDF

OUT = Path(__file__).resolve().parent / "公司业务一页纸.pdf"
FONT = "/usr/share/fonts/truetype/wqy/wqy-microhei.ttc"


def main():
    pdf = FPDF()
    pdf.set_margins(18, 18, 18)
    pdf.add_font("wqy", "", FONT)
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    w = pdf.epw

    pdf.set_font("wqy", "", 14)
    pdf.cell(w, 10, "过程工业流量测量与过程控制", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("wqy", "", 10)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w, 6, "业务一页纸", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(4)
    pdf.set_text_color(0, 0, 0)

    pdf.set_font("wqy", "", 9)
    pdf.multi_cell(w, 5, "定位：过程工业流量测量 + 过程控制 + 工程计算工具")
    pdf.multi_cell(
        w,
        5,
        "服务对象：油气管道运营商、EPC 设计院、智能站场集成商、过程工业终端用户",
    )
    pdf.ln(3)

    sections = [
        (
            "我们能做什么",
            [
                "差压流量一次元件：选型、核算、计算书、结构出图（ISO 5167；PRESO 族）",
                "限流孔板 RO：单级/多级降压、放空核算、CAD 出图",
                "调节阀选型：Cv/Kv、阻塞流、气蚀闪蒸（IEC 60534）",
                "变送器集成：差压/压力变送器型号分解与规格校核（Rosemount 等）",
                "工程计算软件：流衡 FlowSize，标准可追溯、计算书可导出",
                "培训与仿真：智能定位器原理讲解与互动仿真（SMAR FY301）",
            ],
        ),
        (
            "核心产品线（差压计量）",
            [
                "标准孔板、调整型/平衡孔板",
                "文丘里管/喷嘴、楔形、V 锥、均速管（椭圆巴）",
                "限流孔板（放空、降压限流）",
            ],
        ),
        (
            "代表业绩（节选）",
            [
                "濮阳-鹤壁天然气输气管道：15 台二级限流孔板核算与结构出图",
                "西一线长兴站智能站场：差压变送器选型（3051CD）",
                "过程装置：法兰对夹孔板生产级机加装配图交付",
            ],
        ),
        (
            "自研产品 · 流衡 FlowSize",
            [
                "调节阀 + 差压节流装置工程计算（CONVAL 类能力方向）",
                "9 个计算模块、约百种工质库、计算书导出、Web 优先（MVP 0.1）",
            ],
        ),
        (
            "联系方式（请填写）",
            ["公司：", "联系人：", "电话：", "邮箱："],
        ),
    ]

    for title, items in sections:
        pdf.set_font("wqy", "", 11)
        pdf.set_fill_color(232, 245, 233)
        pdf.cell(w, 8, title, fill=True, new_x="LMARGIN", new_y="NEXT")
        pdf.ln(1)
        pdf.set_font("wqy", "", 9)
        for item in items:
            pdf.multi_cell(w, 5, f"- {item}")
        pdf.ln(2)

    pdf.set_font("wqy", "", 7)
    pdf.set_text_color(120, 120, 120)
    pdf.cell(w, 5, "ZL-WORK · 可用于投标附件或客户首次介绍", align="C")

    pdf.output(str(OUT))
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
