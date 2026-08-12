# -*- coding: utf-8 -*-
import fitz, re, sys, shutil, os
sys.stdout.reconfigure(encoding='utf-8')
src = r'C:\Users\sanye\xwechat_files\q251818162_6887\msg\file\2026-05\2-压力（差压）变送器技术规格书.pdf'
dst_dir = r'C:\Users\sanye\Desktop\AI\变送器选型'
dst = os.path.join(dst_dir, '2-压力（差压）变送器技术规格书.pdf')
out = os.path.join(dst_dir, '规格书_extract.txt')
shutil.copy2(src, dst)
doc = fitz.open(src)
print('pages', doc.page_count)
texts = []
for i, p in enumerate(doc):
    t = p.get_text()
    texts.append(f'--- page {i+1} ---\n{t}')
full = '\n'.join(texts)
open(out, 'w', encoding='utf-8').write(full)
print('--- hits ---')
for m in re.finditer(r'.{0,50}(静压|耐压|过压|工作压力|额定压力|最大工作|单向静压|6\s*MPa|2\.5\s*MPa).{0,80}', full):
    s = re.sub(r'\s+', ' ', m.group(0))
    print('HIT:', s)
print('saved', out)
