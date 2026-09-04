#!/usr/bin/env python3
"""Generate a readable business-description PDF for the HK industrial-automation company."""

from pathlib import Path

from fpdf import FPDF
from fpdf.enums import XPos, YPos

FONT = "/usr/share/fonts/truetype/wqy/wqy-microhei.ttc"
OUT_ARTIFACT = Path("/opt/cursor/artifacts/香港公司-工业自动化业务说明.pdf")
OUT_DOCS = Path("/workspace/docs/香港公司-工业自动化业务说明.pdf")
OUT_ASCII = Path("/workspace/docs/hk-industrial-automation-business-note.pdf")


class PDF(FPDF):
    def footer(self):
        self.set_y(-14)
        self.set_font("wqy", size=8)
        self.set_text_color(150, 150, 150)
        self.cell(0, 8, f"{self.page_no()}", align="C")


def usable_w(pdf):
    return pdf.w - pdf.l_margin - pdf.r_margin


def heading(pdf, text):
    pdf.ln(2.5)
    pdf.set_font("wqy", size=12.5)
    pdf.set_text_color(20, 55, 95)
    pdf.set_x(pdf.l_margin)
    pdf.cell(usable_w(pdf), 7.5, text, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_draw_color(20, 55, 95)
    pdf.set_line_width(0.35)
    y = pdf.get_y()
    pdf.line(pdf.l_margin, y, pdf.l_margin + 28, y)
    pdf.ln(2.2)


def para(pdf, text, size=10.8, leading=6.4):
    pdf.set_font("wqy", size=size)
    pdf.set_text_color(35, 35, 35)
    width = usable_w(pdf)
    for block in text.split("\n"):
        pdf.set_x(pdf.l_margin)
        if not block.strip():
            pdf.ln(2.2)
            continue
        pdf.multi_cell(width, leading, block)
        pdf.ln(0.7)


def build():
    pdf = PDF(format="A4")
    pdf.set_auto_page_break(auto=True, margin=18)
    pdf.add_font("wqy", fname=FONT)
    pdf.set_margins(18, 18, 18)
    pdf.add_page()

    pdf.set_font("wqy", size=20)
    pdf.set_text_color(18, 40, 72)
    pdf.cell(usable_w(pdf), 10, "香港公司业务说明", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(1)
    pdf.set_font("wqy", size=11)
    pdf.set_text_color(90, 90, 90)
    pdf.cell(usable_w(pdf), 7, "工业自动化  ·  石化 / 化工流程控制", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(2)
    pdf.set_draw_color(180, 180, 180)
    pdf.set_line_width(0.2)
    y = pdf.get_y()
    pdf.line(pdf.l_margin, y, pdf.l_margin + usable_w(pdf), y)
    pdf.ln(4)

    para(
        pdf,
        "我们做的是工业自动化这一行，终端都在石化、化工这类有流程控制的装置上。装置要稳定跑起来，现场就需要仪表、控制、执行这一套东西。我们不是做零售，也不是开店等人上门，生意围着这些终端转：生产厂、国际品牌的项目代理商、大型总包商，各干各的环节，最后都落到同一批用户身上。",
    )
    para(
        pdf,
        "单子分两种。一种是项目，跟着装置建设和改造走，金额大、节点清楚，合同、供货、验收绑在项目进度上。另一种是项目之外的日常采购，备件、补货、临时加购，单笔不大，但一直有。两种单会叠在一起：项目一次备得多，现场当下用得少，剩下的会在后面的项目或零星采购里慢慢消化。",
    )

    heading(pdf, "这一行在内地怎么做")
    para(
        pdf,
        "内地做工业自动化贸易，多数不是自己囤一大仓库。合同、采购、开票、收款、通知发货，这一整套都在国内完成。货往往不进自己公司的仓，由供货方按指令送到客户或指定地点。靠的是老板把客户关系和项目节点盯住，谁要货、什么时候要、规格会不会改，都在关系里。",
    )
    para(
        pdf,
        "这是真买卖。有合同、有票、有款、有发货，只是货不一定在自己仓库里过一晚。贸易商吃的是货权、账期、规格和交期，不是房租。",
    )

    heading(pdf, "香港公司做什么")
    para(
        pdf,
        "香港公司做的是同一门生意、同一批客户，不是另外变出一套只开票的空转。流程和内地一样：签约、采购、开票、收款、安排发货。差别在合同性质——采购和销售签的是进出口合同，开票和收款走香港公司。货按指令进保税监管场所，有出口报关单、有进口报关单。货权、报关、合同、银行收款对得上。",
    )
    para(
        pdf,
        "香港本身就是贸易港。我们这个行业在香港本地的工厂生意不多，客户和项目主要在内地流程工业上。所以香港公司的角色很清楚：进出口签约和结算放在这里，利润留在这里。毛利是正常的贸易加价，不是过一道手收一点通道费。对方以无关联的第三方为主。",
    )
    para(
        pdf,
        "办公室在香港，决策在香港。货不必开进办公室，也不必开进自有仓。保税进出和报关单说明货在监管链条里走，不是纸面上改个进出口抬头、货还在工厂之间直接调拨。",
    )

    heading(pdf, "为什么有时要国内公司接一批货")
    para(
        pdf,
        "项目供货和现场领用经常对不齐。比如一次要进十套，眼下装置只用得上一套，剩下九套要在后面的项目或日常采购里卖掉。如果整批都压在香港保税仓里，仓储费会很难看。我们用的是玉田香港有限公司的保税仓储，仓租不便宜。",
    )
    para(
        pdf,
        "所以有的单子会让国内公司做中转：按需要把一批货接进来，先把当下要出的卖掉，余量放在国内这边分批消化。这样少占香港保税仓的位置，节奏也跟得上现场。国内接的那一批，后面是要卖出去的，不是两家自己的公司把货空转一圈。说到底，香港公司管进出口合同、发票、收款和利润，货走保税、有报关；国内公司只在批量和出货对不上的时候接货分销，为的是少付玉田香港有限公司的仓租。",
    )

    pdf.ln(8)
    pdf.set_font("wqy", size=9)
    pdf.set_text_color(140, 140, 140)
    pdf.cell(usable_w(pdf), 6, "根据当事人说明整理   ·   2026年9月", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    OUT_ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
    OUT_DOCS.parent.mkdir(parents=True, exist_ok=True)
    pdf.output(str(OUT_ARTIFACT))
    pdf.output(str(OUT_DOCS))
    pdf.output(str(OUT_ASCII))
    print(OUT_ARTIFACT)
    print(OUT_DOCS)
    print(OUT_ASCII)


if __name__ == "__main__":
    build()
