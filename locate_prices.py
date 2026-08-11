from PIL import Image
import numpy as np
from pathlib import Path

src = Path(r"C:\Users\sanye\.cursor\projects\c-Users-sanye-Desktop-AI\assets\c__Users_sanye_AppData_Roaming_Cursor_User_workspaceStorage_empty-window_images_c6f6bf0ddcd3295d0c89d8587d00f09f-3c06721a-ebac-4d02-92e7-14cd20693bb0.png")
out_dir = Path(r"C:\Users\sanye\Desktop\AI\日常")

im = Image.open(src).convert("RGB")
arr = np.array(im)
h, w = arr.shape[:2]

# Detect gray/dark lines (not pure white)
# White is ~255; grid lines are likely gray
gray = arr.mean(axis=2)
lineish = gray < 200

y0, y1 = 90, 430
col_sum = lineish[y0:y1].sum(axis=0)
# find peaks
thresh = (y1 - y0) * 0.35
peaks = np.where(col_sum > thresh)[0]
clusters = []
if len(peaks):
    start = prev = int(peaks[0])
    for p in peaks[1:]:
        p = int(p)
        if p - prev > 3:
            clusters.append((start, prev))
            start = p
        prev = p
    clusters.append((start, prev))
vlines = [(c[0] + c[1]) // 2 for c in clusters]
print("vlines", vlines)
print("col peaks count", len(peaks))
# print top column densities
top = np.argsort(col_sum)[-30:][::-1]
print("top x dens", [(int(x), int(col_sum[x])) for x in top])

row_sum = lineish[y0:y1].sum(axis=1)
thresh_r = w * 0.2
peaks = np.where(row_sum > thresh_r)[0]
clusters = []
if len(peaks):
    start = prev = int(peaks[0])
    for p in peaks[1:]:
        p = int(p)
        if p - prev > 2:
            clusters.append((start + y0, prev + y0))
            start = p
        prev = p
    clusters.append((start + y0, prev + y0))
hlines = [(c[0] + c[1]) // 2 for c in clusters]
print("hlines", hlines)

# Also try to find dark text blobs in price-looking area
# Sample several vertical strips
for x0, x1 in [(580,650),(600,680),(620,700),(640,720),(560,640)]:
    region = gray[150:260, x0:x1]
    ink = (region < 100).sum()
    print(f"ink {x0}-{x1}:", int(ink))

# Save wider crop of table mid section
im.crop((500, 120, 780, 300)).save(out_dir / "price_crop2.png")

# Print average color of a blank cell vs price cell area by scanning
# Look at row of pixels around y=165 (first data row middle)
for y in [155, 160, 165, 170, 175, 180]:
    row = gray[y, 580:720]
    dark_xs = np.where(row < 100)[0]
    if len(dark_xs):
        print(f"y={y} dark xs relative 580:", dark_xs.tolist()[:40], "... count", len(dark_xs))
