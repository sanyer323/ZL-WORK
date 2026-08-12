# -*- coding: utf-8 -*-
"""将单级计算书中的结构图替换为最新 DXF 渲染 PNG（按页通径匹配）。"""
from __future__ import annotations

import re
from pathlib import Path

import fitz

OUT = Path(__file__).resolve().parent
PDF = OUT / "PH02_放空限流孔板计算书_单级_Campbell.pdf"
PNG_DIR = OUT / "结构图PNG"


def page_dn(page) -> str:
    text = page.get_text("text")
    m = re.search(r"管道通径[^\n]*?(DN(?:50|80|100|150|200))", text)
    if m:
        return m.group(1)
    # 回退：取文中首次标准通径
    m = re.search(r"\bDN(?:50|80|100|150|200)\b", text)
    if not m:
        raise RuntimeError("page missing DN")
    return m.group(0)


def main():
    doc = fitz.open(PDF)
    for i, page in enumerate(doc):
        dn = page_dn(page)
        png = PNG_DIR / f"结构图_{dn}_单级.png"
        if not png.exists():
            raise FileNotFoundError(png)
        imgs = page.get_images(full=True)
        if not imgs:
            raise RuntimeError(f"page {i+1} has no image")
        xref = imgs[0][0]
        page.replace_image(xref, filename=str(png))
        print(f"page {i+1:02d} -> {dn} ({png.name})")
    doc.saveIncr()
    doc.close()
    print("OK", PDF)


if __name__ == "__main__":
    main()
