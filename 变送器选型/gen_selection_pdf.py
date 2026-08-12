# -*- coding: utf-8 -*-
"""Generate Rosemount 3051CD selection PDF for WZDD-26-Z117."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, black, white
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, HRFlowable
)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
import os

OUT = os.path.join(os.path.dirname(__file__), "WZDD-26-Z117_3051CD选型单.pdf")

pdfmetrics.registerFont(TTFont("SimHei", r"C:\Windows\Fonts\simhei.ttf"))
pdfmetrics.registerFont(TTFont("SimSun", r"C:\Windows\Fonts\simsun.ttc", subfontIndex=0))

GREEN = HexColor("#006633")
LIGHT = HexColor("#E8F5E9")
GRAY = HexColor("#F5F5F5")
LINE = HexColor("#333333")
ACCENT = HexColor("#0D47A1")

styles = {
    "title": ParagraphStyle(
        "title", fontName="SimHei", fontSize=16, alignment=TA_CENTER,
        textColor=GREEN, spaceAfter=4 * mm, leading=22
    ),
    "sub": ParagraphStyle(
        "sub", fontName="SimSun", fontSize=10, alignment=TA_CENTER,
        textColor=LINE, spaceAfter=2 * mm, leading=14
    ),
    "h": ParagraphStyle(
        "h", fontName="SimHei", fontSize=11, alignment=TA_LEFT,
        textColor=GREEN, spaceBefore=3 * mm, spaceAfter=2 * mm, leading=16
    ),
    "body": ParagraphStyle(
        "body", fontName="SimSun", fontSize=9, alignment=TA_LEFT,
        textColor=black, leading=13
    ),
    "cell": ParagraphStyle(
        "cell", fontName="SimSun", fontSize=9, alignment=TA_LEFT,
        textColor=black, leading=12
    ),
    "cell_b": ParagraphStyle(
        "cell_b", fontName="SimHei", fontSize=9, alignment=TA_LEFT,
        textColor=black, leading=12
    ),
    "model": ParagraphStyle(
        "model", fontName="SimHei", fontSize=13, alignment=TA_CENTER,
        textColor=ACCENT, leading=18
    ),
    "note": ParagraphStyle(
        "note", fontName="SimSun", fontSize=8, alignment=TA_LEFT,
        textColor=HexColor("#555555"), leading=11
    ),
    "right": ParagraphStyle(
        "right", fontName="SimSun", fontSize=8, alignment=TA_RIGHT,
        textColor=HexColor("#666666"), leading=11
    ),
}


def P(text, style="cell"):
    return Paragraph(str(text).replace("\n", "<br/>"), styles[style])


def section_table(headers, rows, col_widths):
    data = [[P(h, "cell_b") for h in headers]]
    for r in rows:
        data.append([P(c, "cell") for c in r])
    t = Table(data, colWidths=col_widths, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), GREEN),
        ("TEXTCOLOR", (0, 0), (-1, 0), white),
        ("BACKGROUND", (0, 1), (-1, 1), LIGHT),
        ("ROWBACKGROUNDS", (0, 2), (-1, -1), [white, GRAY]),
        ("GRID", (0, 0), (-1, -1), 0.4, LINE),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 3),
        ("RIGHTPADDING", (0, 0), (-1, -1), 3),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        # header text white via Paragraph color override — use white style
    ]))
    # Fix header paragraphs to white
    for i, h in enumerate(headers):
        data[0][i] = Paragraph(
            str(h),
            ParagraphStyle("hw", fontName="SimHei", fontSize=9,
                           textColor=white, leading=12)
        )
    t = Table(data, colWidths=col_widths, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), GREEN),
        ("BACKGROUND", (0, 1), (-1, 1), LIGHT),
        ("ROWBACKGROUNDS", (0, 2), (-1, -1), [white, GRAY]),
        ("GRID", (0, 0), (-1, -1), 0.4, LINE),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 3),
        ("RIGHTPADDING", (0, 0), (-1, -1), 3),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))
    return t


def kv_table(pairs, col_widths):
    data = [[P(k, "cell_b"), P(v, "cell")] for k, v in pairs]
    t = Table(data, colWidths=col_widths)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, -1), GRAY),
        ("GRID", (0, 0), (-1, -1), 0.4, LINE),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))
    return t


def build():
    doc = SimpleDocTemplate(
        OUT, pagesize=A4,
        leftMargin=14 * mm, rightMargin=14 * mm,
        topMargin=12 * mm, bottomMargin=12 * mm
    )
    W = A4[0] - 28 * mm
    story = []

    story.append(Paragraph("Rosemount™ 3051CD 差压变送器选型单", styles["title"]))
    story.append(Paragraph(
        "依据产品选型样本（Product Data Sheet）订货信息表编制", styles["sub"]
    ))
    story.append(Paragraph(
        "订单 WZDD-26-Z117　|　合同 ZJSW-26-MM01-0143　|　西一线长兴站智能站场建设",
        styles["sub"]
    ))
    story.append(HRFlowable(width="100%", thickness=1.2, color=GREEN, spaceAfter=3 * mm))

    story.append(Paragraph("一、推荐完整型号", styles["h"]))
    model_box = Table(
        [[P("3051CD4A22A1A E3 DF", "model")],
         [P("工厂标定量程：-0.1 ~ 0.3 MPa　|　数量：3 台　|　规格书耐压：≥6.3 MPa / 耐受≥10 MPa（产品标准 25 MPa）", "sub")]],
        colWidths=[W]
    )
    model_box.setStyle(TableStyle([
        ("BOX", (0, 0), (-1, -1), 1.5, ACCENT),
        ("BACKGROUND", (0, 0), (-1, -1), HexColor("#E3F2FD")),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    ]))
    story.append(model_box)

    story.append(Paragraph("二、技术条件对照", styles["h"]))
    story.append(section_table(
        ["项目", "要求来源", "技术要求", "选型符合性"],
        [
            ["测量类型", "订单", "差压变送器", "3051CD 差压"],
            ["测量量程", "订单", "-0.1 ~ 0.3 MPa", "量程代码 4（±2.07 MPa），标定至该量程"],
            ["精度", "订单", "0.002 级（0.2%）", "参考精度约 0.065%，满足"],
            ["接液材质", "订单", "304L", "法兰/膜片 316L SST（优代 304L）"],
            ["过程连接", "订单", '1/2" NPT', "选项 DF：1/2–14 NPT 法兰接头"],
            ["防爆", "订单", "Ex d IIB T3", "选项 E3 中国隔爆（覆盖 IIB T3）"],
            ["防护等级", "订单", "IP40", "外壳通常 IP66/68，高于要求"],
            ["输出信号", "订单", "4–20 mA", "输出代码 A（4–20 mA HART）"],
            ["订单标注压力", "订单", "2.5 MPa", "物资描述末项"],
            ["耐压/静压", "规格书/数据单", "差压单向承压≥设计压力；数据单耐压≥6.3 MPa；耐受≥10 MPa", "标准静压/过压 25 MPa，满足；无需 P9"],
        ],
        [22 * mm, 22 * mm, 45 * mm, W - 89 * mm]
    ))

    story.append(Paragraph("三、选型样本代码分解（按 PDS 订货信息）", styles["h"]))
    story.append(section_table(
        ["位置", "代码", "选型样本说明", "选用理由"],
        [
            ["型号", "3051C", "共平面压力变送器", "共平面平台"],
            ["测量类型", "D", "差压 Differential", "订单：差压"],
            ["压力量程", "4", "差压 ±300 psi（±20.68 bar / ±2.07 MPa）", "覆盖 -0.1~0.3 MPa；量程3上限约0.25 MPa不足"],
            ["变送器输出", "A", "4–20 mA，带 HART 数字信号", "订单：4–20 mA"],
            ["构件材料", "2", "共平面法兰 316 SST + 316 排污/排气阀", "标准可订货；316L 优于 304L"],
            ["隔离膜片", "2", "316L 不锈钢", "无 304L 膜片选项"],
            ["O 型圈", "A", "玻璃填充 PTFE", "标准选项"],
            ["传感器充液", "1", "硅油", "标准选项"],
            ["外壳", "A", "铝，导管口 1/2–14 NPT", "标准选项"],
            ["产品认证", "E3", "中国隔爆 China Flameproof", "对应 Ex d IIB T3"],
            ["法兰接头", "DF", "1/2–14 NPT flange adapter(s)", "对应 1/2\" NPT"],
        ],
        [22 * mm, 18 * mm, 70 * mm, W - 110 * mm]
    ))

    story.append(Paragraph("四、静压 / 耐压说明（选型样本规格）", styles["h"]))
    story.append(kv_table([
        ["标准静压限值（3051CD 量程 2–5）", "3626 psig ≈ 25 MPa"],
        ["过压限值（3051CD 量程 2–5）", "3626 psig ≈ 25 MPa"],
        ["规格书 5.10", "差压变送器单向承压不低于管道设计压力"],
        ["数据单（差压 PDT）", "耐压不低于 6.3 MPa"],
        ["数据单专用技术要求", "耐受压力不得低于 10 MPa"],
        ["结论", "标准配置 25 MPa 满足 6.3/10 MPa，不必增加 P9"],
    ], [55 * mm, W - 55 * mm]))

    story.append(Paragraph("五、订货信息摘要", styles["h"]))
    story.append(kv_table([
        ["完整型号", "3051CD4A22A1A E3 DF"],
        ["数量", "3 台"],
        ["工厂标定", "LRV = -0.1 MPa，URV = 0.3 MPa"],
        ["建议加项（可选）", "C1 出厂组态 / M5 表头 / B4 支架 / Q4 标定证书"],
        ["物资编码（订单）", "080200810000437"],
        ["交货地点", "浙江省金华市浦江县郑家坞镇振浦路280号西气东输浦江维抢修队"],
    ], [40 * mm, W - 40 * mm]))

    story.append(Spacer(1, 4 * mm))
    story.append(P(
        "备注：1）本选型单按 Emerson Rosemount 3051 产品选型样本（PDS）订货信息表编制；"
        "2）接液材质以 316L 优代订单 304L，若需 304 法兰（部分渠道代码 6）请另行确认；"
        "3）耐静压按客户规格书/数据单：单向承压≥设计压力、PDT耐压≥6.3 MPa、耐受≥10 MPa；产品标准静压 25 MPa 可覆盖。"
        "手头规格书封面为延川/龙游工程，若长兴站另有数据单以该单为准。",
        "note"
    ))
    story.append(Spacer(1, 2 * mm))
    story.append(Paragraph("编制依据：订单 WZDD-26-Z117 + 客户规格书/数据单耐静压要求　|　型号：Rosemount 3051CD", styles["right"]))

    doc.build(story)
    print("OK", OUT)


if __name__ == "__main__":
    build()
