from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import numpy as np

src = Path(r"C:\Users\sanye\.cursor\projects\c-Users-sanye-Desktop-AI\assets\c__Users_sanye_AppData_Roaming_Cursor_User_workspaceStorage_empty-window_images_c6f6bf0ddcd3295d0c89d8587d00f09f-3c06721a-ebac-4d02-92e7-14cd20693bb0.png")
out = Path(r"C:\Users\sanye\Desktop\AI\日常\报价单_单价已改.png")

im = Image.open(src).convert("RGB")
arr = np.array(im)
draw = ImageDraw.Draw(im)

# Column bounds from grid detection
price_x0, price_x1 = 662, 753  # 单价列
# Data row y bounds
rows = [
    (127, 158),  # row1
    (160, 185),  # row2
    (187, 211),  # row3
    (213, 238),  # row4
]
new_prices = ["21", "27", "19", "22"]

# Sample background color near blank area of price cells
bg = (255, 255, 255)

# Find a good font similar to spreadsheet
font_candidates = [
    r"C:\Windows\Fonts\simsun.ttc",
    r"C:\Windows\Fonts\simhei.ttf",
    r"C:\Windows\Fonts\msyh.ttc",
    r"C:\Windows\Fonts\arial.ttf",
    r"C:\Windows\Fonts\calibri.ttf",
]
font = None
for fp in font_candidates:
    try:
        font = ImageFont.truetype(fp, 14)
        print("using font", fp)
        break
    except Exception as e:
        print("fail", fp, e)

if font is None:
    font = ImageFont.load_default()

# First, inspect ink in each price cell to refine fill box
gray = arr.mean(axis=2)
for i, ((y0, y1), price) in enumerate(zip(rows, new_prices)):
    cell = gray[y0:y1, price_x0:price_x1]
    ink_ys, ink_xs = np.where(cell < 140)
    if len(ink_xs):
        bx0 = price_x0 + int(ink_xs.min()) - 2
        bx1 = price_x0 + int(ink_xs.max()) + 3
        by0 = y0 + int(ink_ys.min()) - 2
        by1 = y0 + int(ink_ys.max()) + 3
    else:
        bx0, bx1, by0, by1 = price_x0 + 5, price_x1 - 5, y0 + 3, y1 - 3
    print(f"row{i+1} ink box", bx0, by0, bx1, by1)

    # Cover old price with white (slightly padded within cell, avoid grid lines)
    pad = 1
    fill_box = [
        max(price_x0 + 2, bx0 - 4),
        max(y0 + 1, by0 - 2),
        min(price_x1 - 2, bx1 + 4),
        min(y1 - 1, by1 + 2),
    ]
    draw.rectangle(fill_box, fill=bg)

    # Measure and center new text
    bbox = draw.textbbox((0, 0), price, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    cx = (price_x0 + price_x1) // 2
    cy = (y0 + y1) // 2
    tx = cx - tw // 2 - bbox[0]
    ty = cy - th // 2 - bbox[1]
    draw.text((tx, ty), price, fill=(0, 0, 0), font=font)

im.save(out)
print("saved", out)

# Also save a crop for verification
im.crop((560, 120, 780, 260)).save(Path(r"C:\Users\sanye\Desktop\AI\日常\price_verify.png"))
print("verify crop saved")
