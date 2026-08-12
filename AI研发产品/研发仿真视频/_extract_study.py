# -*- coding: utf-8 -*-
import re
import sys
from pathlib import Path

import fitz

sys.stdout.reconfigure(encoding="utf-8")
root = Path(r"C:\Users\sanye\Desktop\SMAR\AI研发产品")
study = Path(r"C:\Users\sanye\Desktop\SMAR\AI研发产品\研发仿真视频")

for p in sorted(root.glob("FY301ME*.pdf")):
    doc = fitz.open(p)
    parts = []
    for i in range(doc.page_count):
        parts.append(f"\n\n===== PAGE {i+1} =====\n{doc[i].get_text('text')}")
    text = "".join(parts)
    safe = "EN" if p.name == "FY301ME.pdf" else "CN"
    out = study / f"_study_FY301ME_{safe}.txt"
    out.write_text(text, encoding="utf-8")
    print(p.name, "pages", doc.page_count, "chars", len(text), "->", out.name)
    for kw in [
        "Diagnostic", "piezo", "FYCAL", "Hall", "restriction", "spool",
        "diaphragm", "without Configurator", "NOZZLE", "pilot", "error",
        "故障", "诊断", "压电", "节流",
    ]:
        print(f"  {kw}: {len(re.findall(re.escape(kw), text, re.I))}")
    doc.close()
