#!/usr/bin/env python3
"""Generate PPT: overseas Chinese-model token / Baidu compute sales briefing."""

from __future__ import annotations

from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.util import Emu, Inches, Pt

OUT = Path(__file__).with_name("海外AI模型与算力出海方案.pptx")

# Visual system — deep ink + copper (not purple/cream AI defaults)
INK = RGBColor(0x0F, 0x1C, 0x2E)
INK2 = RGBColor(0x1A, 0x2F, 0x45)
SLATE = RGBColor(0x3D, 0x4F, 0x63)
MUTED = RGBColor(0x6B, 0x7C, 0x8E)
LINE = RGBColor(0xD8, 0xE0, 0xE8)
CARD = RGBColor(0xF4, 0xF7, 0xFA)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
COPPER = RGBColor(0xC4, 0x5C, 0x26)
TEAL = RGBColor(0x1F, 0x7A, 0x6E)
OK = RGBColor(0x1F, 0x7A, 0x6E)
BAD = RGBColor(0xA8, 0x3B, 0x2C)


def set_run(run, text, size=18, bold=False, color=INK, font="Microsoft YaHei"):
    run.text = text
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.color.rgb = color
    run.font.name = font


def add_text(tf, text, size=18, bold=False, color=INK, align=PP_ALIGN.LEFT, space_after=6):
    p = tf.paragraphs[0] if not tf.paragraphs[0].text else tf.add_paragraph()
    p.alignment = align
    p.space_after = Pt(space_after)
    run = p.add_run()
    set_run(run, text, size=size, bold=bold, color=color)
    return p


def clear_tf(tf):
    tf.clear()
    tf.word_wrap = True


def fill_shape(shape, color):
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.line.fill.background()


def band(slide, top, height, color):
    sh = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), top, Inches(13.333), height)
    fill_shape(sh, color)
    return sh


def accent_bar(slide, left, top, width=Inches(0.12), height=Inches(0.55)):
    sh = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, height)
    fill_shape(sh, COPPER)
    return sh


def card(slide, left, top, width, height, fill=CARD):
    sh = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    fill_shape(sh, fill)
    sh.adjustments[0] = 0.08
    return sh


def textbox(slide, left, top, width, height):
    return slide.shapes.add_textbox(left, top, width, height)


def title_slide(prs, title, subtitle, foot):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    band(slide, Inches(0), Inches(7.5), INK)
    band(slide, Inches(0), Inches(0.18), COPPER)
    tb = textbox(slide, Inches(0.9), Inches(2.1), Inches(11.5), Inches(1.4))
    tf = tb.text_frame
    clear_tf(tf)
    add_text(tf, title, size=36, bold=True, color=WHITE, space_after=10)
    tb2 = textbox(slide, Inches(0.9), Inches(3.6), Inches(11.5), Inches(1.2))
    tf2 = tb2.text_frame
    clear_tf(tf2)
    add_text(tf2, subtitle, size=18, color=RGBColor(0xB8, 0xC7, 0xD6), space_after=8)
    tb3 = textbox(slide, Inches(0.9), Inches(6.5), Inches(11.5), Inches(0.5))
    tf3 = tb3.text_frame
    clear_tf(tf3)
    add_text(tf3, foot, size=12, color=MUTED)
    return slide


def section_header(slide, title, subtitle=None):
    band(slide, Inches(0), Inches(0.08), COPPER)
    accent_bar(slide, Inches(0.7), Inches(0.35))
    tb = textbox(slide, Inches(1.0), Inches(0.32), Inches(11.5), Inches(0.6))
    tf = tb.text_frame
    clear_tf(tf)
    add_text(tf, title, size=26, bold=True, color=INK, space_after=0)
    if subtitle:
        tb2 = textbox(slide, Inches(1.0), Inches(0.95), Inches(11.5), Inches(0.4))
        tf2 = tb2.text_frame
        clear_tf(tf2)
        add_text(tf2, subtitle, size=13, color=MUTED, space_after=0)


def bullet_block(slide, left, top, width, height, lines, size=15):
    tb = textbox(slide, left, top, width, height)
    tf = tb.text_frame
    clear_tf(tf)
    for i, line in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = PP_ALIGN.LEFT
        p.space_after = Pt(8)
        p.level = 0
        run = p.add_run()
        set_run(run, line, size=size, color=INK2)
    return tb


def two_col_cards(slide, left_title, left_lines, right_title, right_lines, left_color=TEAL, right_color=COPPER):
    c1 = card(slide, Inches(0.7), Inches(1.6), Inches(5.7), Inches(5.0))
    c2 = card(slide, Inches(6.9), Inches(1.6), Inches(5.7), Inches(5.0))
    # title strips
    s1 = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.7), Inches(1.6), Inches(5.7), Inches(0.55))
    fill_shape(s1, left_color)
    s2 = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(6.9), Inches(1.6), Inches(5.7), Inches(0.55))
    fill_shape(s2, right_color)
    t1 = textbox(slide, Inches(0.95), Inches(1.68), Inches(5.2), Inches(0.4))
    tf = t1.text_frame
    clear_tf(tf)
    add_text(tf, left_title, size=16, bold=True, color=WHITE, space_after=0)
    t2 = textbox(slide, Inches(7.15), Inches(1.68), Inches(5.2), Inches(0.4))
    tf = t2.text_frame
    clear_tf(tf)
    add_text(tf, right_title, size=16, bold=True, color=WHITE, space_after=0)
    bullet_block(slide, Inches(0.95), Inches(2.4), Inches(5.2), Inches(3.9), left_lines, size=14)
    bullet_block(slide, Inches(7.15), Inches(2.4), Inches(5.2), Inches(3.9), right_lines, size=14)


def table_slide(slide, headers, rows, left=Inches(0.7), top=Inches(1.55), width=Inches(11.9), row_h=0.55):
    cols = len(headers)
    nrows = len(rows) + 1
    table_shape = slide.shapes.add_table(nrows, cols, left, top, width, Inches(row_h * nrows))
    table = table_shape.table
    col_w = int(width / cols)
    for i in range(cols):
        table.columns[i].width = col_w
    for j, h in enumerate(headers):
        cell = table.cell(0, j)
        cell.text = h
        for p in cell.text_frame.paragraphs:
            p.alignment = PP_ALIGN.CENTER
            for r in p.runs:
                set_run(r, h, size=13, bold=True, color=WHITE)
        cell.fill.solid()
        cell.fill.fore_color.rgb = INK
    for i, row in enumerate(rows, start=1):
        for j, val in enumerate(row):
            cell = table.cell(i, j)
            cell.text = val
            for p in cell.text_frame.paragraphs:
                p.alignment = PP_ALIGN.LEFT if j else PP_ALIGN.CENTER
                for r in p.runs:
                    set_run(r, val, size=12, color=INK2)
            cell.fill.solid()
            cell.fill.fore_color.rgb = WHITE if i % 2 else CARD


def build():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    # 1 Title
    title_slide(
        prs,
        "海外卖中国模型 Token / 算力",
        "从官方折扣到百度渠道转售：完整业务梳理",
        "内部方案简报 · 香港公司主体 · 不自建服务器优先路径",
    )

    # 2 Agenda
    s = prs.slides.add_slide(prs.slide_layouts[6])
    band(s, Inches(0), Inches(7.5), WHITE)
    section_header(s, "目录", "把昨天讨论从头到尾串成一条决策链")
    items = [
        "01  起点：有国内主流模型官方折扣，想卖到海外",
        "02  红线：裸转售 Key vs 合规卖服务",
        "03  客户要什么、两种卖法、两类客户",
        "04  条件确认：全系折扣 + 香港公司 + 愿做交付",
        "05  技术路线 A：One API 自建网关（备选）",
        "06  最终选择：不买服务器，挂靠百度卖算力",
        "07  跟百度谈什么、本周怎么落地",
    ]
    bullet_block(s, Inches(1.0), Inches(1.7), Inches(11), Inches(5), items, size=18)

    # 3 Opportunity
    s = prs.slides.add_slide(prs.slide_layouts[6])
    band(s, Inches(0), Inches(7.5), WHITE)
    section_header(s, "01  机会从哪来", "成本优势已经成立，缺的是对外产品形态")
    cards = [
        ("供给", "国内主流模型\n官方折扣渠道\n（DeepSeek / 通义 /\n智谱 / 豆包 / 文心…）"),
        ("主体", "香港公司\n可做境外收款\n与对客合同"),
        ("关系", "与百度有现成合作基础\n可谈云资源与授权"),
        ("意愿", "可做网关/交付\n但更倾向轻资产\n不自购服务器"),
    ]
    for i, (t, body) in enumerate(cards):
        left = Inches(0.7 + i * 3.1)
        card(s, left, Inches(1.7), Inches(2.9), Inches(4.6))
        bar = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, Inches(1.7), Inches(2.9), Inches(0.5))
        fill_shape(bar, INK if i % 2 == 0 else TEAL)
        tb = textbox(s, left + Inches(0.2), Inches(1.78), Inches(2.5), Inches(0.35))
        tf = tb.text_frame
        clear_tf(tf)
        add_text(tf, t, size=15, bold=True, color=WHITE, space_after=0)
        tb2 = textbox(s, left + Inches(0.2), Inches(2.5), Inches(2.5), Inches(3.5))
        tf2 = tb2.text_frame
        clear_tf(tf2)
        for j, line in enumerate(body.split("\n")):
            p = tf2.paragraphs[0] if j == 0 else tf2.add_paragraph()
            p.space_after = Pt(6)
            run = p.add_run()
            set_run(run, line, size=13, color=INK2)

    # 4 Red lines
    s = prs.slides.add_slide(prs.slide_layouts[6])
    band(s, Inches(0), Inches(7.5), WHITE)
    section_header(s, "02  先分清：什么能卖，什么别碰", "官方折扣是起点；灰色倒卖 Key 不是生意")
    two_col_cards(
        s,
        "不建议：裸转售 Token / 共享 Key",
        [
            "• 多数厂商 ToS 禁止二次转售",
            "• 账号封禁、纠纷、拒付率高",
            "• 海外客户不敢把生产流量挂不明中间商",
            "• 信任差、无 SLA、难续费",
            "• 看起来赚差价，实际风险在你",
        ],
        "建议：卖服务（API / 算力渠道）",
        [
            "• 卖统一接入、账单、支持、配额",
            "• 折扣只是你的成本优势",
            "• 香港公司收款 + 合同",
            "• 上游官方/百度授权更稳",
            "• 可做成长期渠道生意",
        ],
        left_color=BAD,
        right_color=OK,
    )

    # 5 What customers buy
    s = prs.slides.add_slide(prs.slide_layouts[6])
    band(s, Inches(0), Inches(7.5), WHITE)
    section_header(s, "03  海外客户真正买什么", "便宜不够；稳定、账单、数据路径说明才成交")
    rows = [
        ("统一 Endpoint", "最好 OpenAI 兼容，降低接入成本"),
        ("多模型路由", "国内主流模型一站调用"),
        ("英文文档与账单", "USD / Stripe / 香港主体发票"),
        ("可用性说明", "延迟、备用、故障责任边界"),
        ("企业刚需", "密钥隔离、限额、审计（后期再做）"),
    ]
    table_slide(s, ["客户要的", "含义"], [[a, b] for a, b in rows], top=Inches(1.6), row_h=0.7)
    note = textbox(s, Inches(0.7), Inches(6.5), Inches(11.9), Inches(0.5))
    tf = note.text_frame
    clear_tf(tf)
    add_text(tf, "结论：对外卖的是「可信的推理/算力服务」，不是「国内更便宜的额度」。", size=14, bold=True, color=COPPER)

    # 6 Two product forms
    s = prs.slides.add_slide(prs.slide_layouts[6])
    band(s, Inches(0), Inches(7.5), WHITE)
    section_header(s, "04  两种卖法（当时解释过）", "你已表示「两种我都不懂」——这里用一张图定调")
    two_col_cards(
        s,
        "A. 纯转售 API（像卖加油卡）",
        [
            "• 客户拿你的 Key，自己调模型",
            "• 你赚进销差价",
            "• 上手快，黏性低",
            "• 封号/涨价客户就走",
            "• 大客户一般不买单",
        ],
        "B. 网关/产品（像卖加油站服务）",
        [
            "• 客户连的是你的地址或百度资源",
            "• 你提供计费、限流、文档、客服",
            "• 难一点，但能长期卖",
            "• 更像正经生意",
            "• 推荐作为对外形态",
        ],
    )

    # 7 Two customer types
    s = prs.slides.add_slide(prs.slide_layouts[6])
    band(s, Inches(0), Inches(7.5), WHITE)
    section_header(s, "05  两类客户：先谁后谁", "建议顺序：个人/小团队 → 再公司")
    table_slide(
        s,
        ["维度", "个人开发者 / 小团队", "海外公司"],
        [
            ["要什么", "便宜、好接、文档清楚", "稳定、合同、发票、合规说明"],
            ["客单价", "低（数美元～数百美元/月）", "高（可到数千美元以上）"],
            ["成交难度", "低，网上就能卖", "高，要信任与材料"],
            ["适合阶段", "现在 / 内测", "稳定运行后再做"],
        ],
        top=Inches(1.7),
        row_h=0.85,
    )

    # 8 Confirmed assets
    s = prs.slides.add_slide(prs.slide_layouts[6])
    band(s, Inches(0), Inches(7.5), WHITE)
    section_header(s, "06  已确认的条件", "讨论过程中你明确过的事实")
    lines = [
        "✓  折扣覆盖所提主流模型（不是只拿一两个）",
        "✓  折扣性质：官方折扣（非灰色二手额度）",
        "✓  主体：已有香港公司",
        "✓  交付意愿：愿意做网关/产品层（后来改为更轻）",
        "✓  供给偏好：可与百度合作，用百度侧资源承载",
        "✓  运维偏好：不买服务器，尽量让百度来做底座",
    ]
    bullet_block(s, Inches(1.0), Inches(1.8), Inches(11), Inches(5), lines, size=18)

    # 9 Path A One API - kept as alternate
    s = prs.slides.add_slide(prs.slide_layouts[6])
    band(s, Inches(0), Inches(7.5), WHITE)
    section_header(s, "07  备选技术路线：One API 自建网关", "你曾选 A；若日后要自控品牌 API，可启用")
    table_slide(
        s,
        ["步骤", "做什么"],
        [
            ["1", "香港/新加坡云主机 + Docker 部署 One API"],
            ["2", "域名 HTTPS，Base URL = https://api.xxx.com/v1"],
            ["3", "后台接各厂商官方折扣 Key，做模型名映射"],
            ["4", "售价 ≈ 成本 × 1.5～1.8，预充值扣费"],
            ["5", "香港公司 Stripe 收款；英文一页文档上线"],
        ],
        top=Inches(1.6),
        row_h=0.7,
    )
    note = textbox(s, Inches(0.7), Inches(6.4), Inches(11.9), Inches(0.6))
    tf = note.text_frame
    clear_tf(tf)
    add_text(
        tf,
        "现状：你决定暂不买服务器 → 本路线降级为「备用能力」，主路径改为百度算力渠道。",
        size=14,
        bold=True,
        color=COPPER,
    )

    # 10 Final choice
    s = prs.slides.add_slide(prs.slide_layouts[6])
    band(s, Inches(0), Inches(7.5), WHITE)
    section_header(s, "08  最终选择：挂靠百度，只卖算力", "轻资产：百度出资源，你做出海销售与资金流")
    two_col_cards(
        s,
        "百度负责",
        [
            "• 服务器 / GPU / 平台底座",
            "• 开通、底层账单、技术供给",
            "• 基础设施稳定性",
            "• （谈妥后）授权与配额保障",
        ],
        "你负责",
        [
            "• 找海外客户、谈价签约",
            "• 香港公司收款与对客合同",
            "• 用官方/百度折扣进货",
            "• 一线商务、续费、需求转述",
        ],
        left_color=INK,
        right_color=TEAL,
    )

    # 11 Two concepts
    s = prs.slides.add_slide(prs.slide_layouts[6])
    band(s, Inches(0), Inches(7.5), WHITE)
    section_header(s, "09  概念澄清：卖模型 Token ≠ 卖 GPU 算力", "对外可以都叫「算力/AI 云」，对内账要分清")
    table_slide(
        s,
        ["", "卖模型（API / Token）", "卖算力（GPU）"],
        [
            ["客户买的", "调模型接口", "租显卡小时 / 包月机器"],
            ["你的优势", "模型官方折扣", "百度云渠道价 + 海外获客"],
            ["客户画像", "App / 开发者", "训练或自建推理的人"],
            ["运维负担", "相对低", "更高（机器、网络、赔付）"],
            ["与现状匹配", "折扣模型强相关", "更贴「百度出机器」"],
        ],
        top=Inches(1.55),
        row_h=0.75,
    )

    # 12 Baidu deal points
    s = prs.slides.add_slide(prs.slide_layouts[6])
    band(s, Inches(0), Inches(7.5), WHITE)
    section_header(s, "10  跟百度必须谈死的 5 句话", "没谈清不要对外报价")
    points = [
        ("01 身份", "渠道 / 代理 / 合作伙伴？有没有书面授权？"),
        ("02 结算", "目录价几折？按量还是包年？月结还是预充？"),
        ("03 客户落户", "开在我名下子账号，还是客户直开百度、我拿返点？"),
        ("04 出海", "是否允许境外客户？合同、发票、数据说明谁出？"),
        ("05 品牌", "能否说 Powered by Baidu Cloud？能否白标？"),
    ]
    for i, (h, body) in enumerate(points):
        top = Inches(1.45 + i * 1.05)
        card(s, Inches(0.7), top, Inches(11.9), Inches(0.9))
        tb = textbox(s, Inches(0.95), top + Inches(0.12), Inches(2.2), Inches(0.6))
        tf = tb.text_frame
        clear_tf(tf)
        add_text(tf, h, size=16, bold=True, color=COPPER, space_after=0)
        tb2 = textbox(s, Inches(3.3), top + Inches(0.22), Inches(9), Inches(0.55))
        tf2 = tb2.text_frame
        clear_tf(tf2)
        add_text(tf2, body, size=15, color=INK2, space_after=0)

    # 13 Two Baidu models
    s = prs.slides.add_slide(prs.slide_layouts[6])
    band(s, Inches(0), Inches(7.5), WHITE)
    section_header(s, "11  百度合作两种做法", "要「折扣在我这、我在卖算力」→ 优先子账号转售")
    two_col_cards(
        s,
        "做法 1：子账号转售（推荐）",
        [
            "• 客户用量记在你组织/主账号下",
            "• 你按折扣向百度付",
            "• 你按销售价向客户收 USD",
            "• 更像真正的「你在卖算力」",
            "• 毛利与客户关系都在你这",
        ],
        "做法 2：推荐返点（最轻）",
        [
            "• 客户直接在百度开户",
            "• 你拿佣金/返点",
            "• 几乎不碰交付",
            "• 不像自有算力生意",
            "• 毛利薄，品牌弱",
        ],
        left_color=TEAL,
        right_color=SLATE,
    )

    # 14 Pricing
    s = prs.slides.add_slide(prs.slide_layouts[6])
    band(s, Inches(0), Inches(7.5), WHITE)
    section_header(s, "12  定价与资金流", "差价要覆盖支付、拒付、客服与上游波动")
    card(s, Inches(0.7), Inches(1.6), Inches(11.9), Inches(2.0))
    tb = textbox(s, Inches(1.0), Inches(1.9), Inches(11.3), Inches(1.5))
    tf = tb.text_frame
    clear_tf(tf)
    add_text(tf, "售价 ≈ 官方/百度结算成本  ×  1.5～1.8", size=28, bold=True, color=INK, align=PP_ALIGN.CENTER, space_after=12)
    add_text(tf, "对外展示：Official ref. price vs Our price（一眼觉得划算，但别打穿毛利）", size=15, color=MUTED, align=PP_ALIGN.CENTER)

    flow = [
        ("海外客户", "付 USD\n香港公司"),
        ("你", "加价出售\n签合同"),
        ("百度", "按折扣结算\n出资源"),
        ("交付", "GPU/平台\n在百度侧"),
    ]
    for i, (t, b) in enumerate(flow):
        left = Inches(0.7 + i * 3.1)
        card(s, left, Inches(4.1), Inches(2.9), Inches(2.4))
        tb = textbox(s, left + Inches(0.15), Inches(4.3), Inches(2.6), Inches(0.4))
        tf = tb.text_frame
        clear_tf(tf)
        add_text(tf, t, size=16, bold=True, color=TEAL if i % 2 == 0 else COPPER, align=PP_ALIGN.CENTER, space_after=0)
        tb2 = textbox(s, left + Inches(0.15), Inches(4.9), Inches(2.6), Inches(1.3))
        tf2 = tb2.text_frame
        clear_tf(tf2)
        for j, line in enumerate(b.split("\n")):
            p = tf2.paragraphs[0] if j == 0 else tf2.add_paragraph()
            p.alignment = PP_ALIGN.CENTER
            p.space_after = Pt(4)
            run = p.add_run()
            set_run(run, line, size=13, color=INK2)

    # 15 What you still own
    s = prs.slides.add_slide(prs.slide_layouts[6])
    band(s, Inches(0), Inches(7.5), WHITE)
    section_header(s, "13  即使不买服务器，你仍要搞定", "轻资产 ≠ 零运营")
    items = [
        "香港公司：对客合同、收款、开票",
        "价目表：GPU 型号 / 包月 / 按小时；进价与售价两列",
        "英文一页介绍：卖的是 Baidu Cloud 算力，谁交付、谁支持",
        "责任边界：底层故障找百度；账号、账单、续费找你",
        "上游合规：书面确认允许面向境外客户提供服务",
    ]
    for i, line in enumerate(items):
        top = Inches(1.55 + i * 0.95)
        n = s.shapes.add_shape(MSO_SHAPE.OVAL, Inches(0.85), top + Inches(0.1), Inches(0.55), Inches(0.55))
        fill_shape(n, INK)
        tb = textbox(s, Inches(0.95), top + Inches(0.18), Inches(0.4), Inches(0.4))
        tf = tb.text_frame
        clear_tf(tf)
        add_text(tf, str(i + 1), size=16, bold=True, color=WHITE, align=PP_ALIGN.CENTER, space_after=0)
        card(s, Inches(1.7), top, Inches(10.8), Inches(0.8))
        tb2 = textbox(s, Inches(2.0), top + Inches(0.2), Inches(10.2), Inches(0.5))
        tf2 = tb2.text_frame
        clear_tf(tf2)
        add_text(tf2, line, size=16, color=INK2, space_after=0)

    # 16 This week
    s = prs.slides.add_slide(prs.slide_layouts[6])
    band(s, Inches(0), Inches(7.5), WHITE)
    section_header(s, "14  本周只做 3 件事", "先把供给和授权钉死，再谈获客")
    weeks = [
        ("① 约百度对接人", "把「身份 / 结算 / 落户 / 出海 / 品牌」五句问出书面或聊天记录"),
        ("② 摸清可卖清单", "折扣到底覆盖：GPU 算力？模型调用？还是两者都有？型号与配额？"),
        ("③ 出一张报价骨架", "香港公司抬头；成本 / 售价 / 付款方式；先别对外公开大范围投放"),
    ]
    for i, (h, b) in enumerate(weeks):
        left = Inches(0.7 + i * 4.1)
        card(s, left, Inches(1.8), Inches(3.9), Inches(4.5))
        bar = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, Inches(1.8), Inches(3.9), Inches(0.7))
        fill_shape(bar, [INK, TEAL, COPPER][i])
        tb = textbox(s, left + Inches(0.2), Inches(1.95), Inches(3.5), Inches(0.45))
        tf = tb.text_frame
        clear_tf(tf)
        add_text(tf, h, size=16, bold=True, color=WHITE, space_after=0)
        tb2 = textbox(s, left + Inches(0.25), Inches(2.8), Inches(3.4), Inches(3.2))
        tf2 = tb2.text_frame
        clear_tf(tf2)
        add_text(tf2, b, size=15, color=INK2)

    # 17 Decision summary
    s = prs.slides.add_slide(prs.slide_layouts[6])
    band(s, Inches(0), Inches(7.5), WHITE)
    section_header(s, "15  决策一页纸", "昨天讨论的最终收敛")
    table_slide(
        s,
        ["议题", "结论"],
        [
            ["生意本质", "官方折扣成本优势 + 海外销售，不是黄牛倒卖 Key"],
            ["对外产品", "百度侧算力/推理服务（渠道转售），而非自建机房"],
            ["主体与收款", "香港公司"],
            ["技术自建", "暂不做 One API；保留为备用"],
            ["优先合作形态", "百度子账号转售（优于纯返点）"],
            ["客户顺序", "先开发者/小团队，再企业"],
            ["定价", "成本 × 1.5～1.8，对照官网公开价展示"],
            ["下一步瓶颈", "与百度书面确认授权、结算、出海与落户方式"],
        ],
        top=Inches(1.45),
        row_h=0.6,
    )

    # 18 Closing
    title_slide(
        prs,
        "下一步",
        "把百度五句话谈成记录 → 出报价骨架 → 找 3～5 个种子客户试单",
        "备选：若百度路径谈不拢，再启用 One API 自建网关方案",
    )

    prs.save(OUT)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    build()
