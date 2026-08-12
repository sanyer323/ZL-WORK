# -*- coding: utf-8 -*-
import fitz, re, sys, os, shutil
sys.stdout.reconfigure(encoding='utf-8')
files = [
    r'C:\Users\sanye\xwechat_files\q251818162_6887\msg\file\2026-05\2-压力（差压）变送器数据单.pdf',
    r'C:\Users\sanye\xwechat_files\q251818162_6887\msg\file\2026-07\80D01BG01-SP001-000#EIN-DS-0003-A_压力变送器数据单.pdf',
]
outdir = r'C:\Users\sanye\Desktop\AI\变送器选型'
for src in files:
    name = os.path.basename(src)
    print('='*60, name)
    doc = fitz.open(src)
    print('pages', doc.page_count)
    texts=[]
    for i,p in enumerate(doc):
        t=p.get_text()
        texts.append(f'--- page {i+1} ---\n{t}')
        # also save page image for page 1-3
        if i < 3:
            pix=p.get_pixmap(matrix=fitz.Matrix(1.5,1.5))
            safe=re.sub(r'[^\w\-]+','_', name)[:40]
            pix.save(os.path.join(outdir, f'{safe}_p{i+1}.png'))
    full='\n'.join(texts)
    out=os.path.join(outdir, name.replace('.pdf','_extract.txt'))
    open(out,'w',encoding='utf-8').write(full)
    shutil.copy2(src, os.path.join(outdir, name))
    for pat in ['静压','耐压','设计压力','工作压力','过载','单向','MPa','差压','量程','管道']:
        print(f'-- {pat} --')
        for m in re.finditer(r'.{0,35}'+re.escape(pat)+r'.{0,55}', full):
            print(re.sub(r'\s+',' ', m.group(0)))
    print('saved', out)
