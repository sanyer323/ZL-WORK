from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import numpy as np

src = Path(
    r"C:\Users\sanye\.cursor\projects\c-Users-sanye-Desktop-AI\assets"
    r"\c__Users_sanye_AppData_Roaming_Cursor_User_workspaceStorage_empty-window_images"
    r"\c6f6bf0ddcd3295d0c89d8587d00f09f-3c06721a-ebac-4d02-92e7-14cd20693bb0.png"
)
out = Path(r"C:\Users\sanye\Desktop\AI\日常\报价单_发给客户.png")
verify = Path(r"C:\Users\sanye\Desktop\AI\日常\verify_prices.png")

im = Image.open(src).convert("RGB")
draw = ImageDraw.Draw(im)
arr = np.array(im)
gray = arr.mean(axis=2)

# 单价列：竖线 661 ~ 754
x0, x1 = 662, 753

# 数据行（跳过表头 126-159）
rows = [
    (160, 185),  # 16.5 -> 21
    (187, 211),  # 21.3 -> 27
    (213, 238),  # 15.4 -> 19
    (240, 264),  # 17.8 -> 22
]
prices = ["21", "27", "19", "22"]

# 优先用 Excel 常见数字字体
font = None
for fp, size in [
    (r"C:\Windows\Fonts\calibri.ttf", 13),
    (r"C:\Windows\Fonts\arial.ttf", 12),
    (r"C:\Windows\Fonts\simsun.ttc", 12),
]:
    try:
        font = ImageFont.truetype(fp, size)
        print("font", fp, size)
        break
    except Exception as e:
        print("skip", fp, e)

for (y0, y1), price in zip(rows, prices):
    # 确认本格有墨迹
    cell = gray[y0:y1, x0:x1]
    ink = np.where(cell < 150)
    print(f"row {y0}-{y1} ink count={len(ink[0])} -> {price}")

    # 整格涂白（避开边框 1px）
    draw.rectangle([x0 + 1, y0, x1 - 1, y1], fill=(255, 255, 255))

    bbox = draw.textbbox((0, 0), price, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    cx = (x0 + x1) / 2
    cy = (y0 + y1) / 2
    tx = cx - tw / 2 - bbox[0]
    ty = cy - th / 2 - bbox[1]
    draw.text((tx, ty), price, fill=(0, 0, 0), font=font)

im.save(out)
im.crop((560, 100, 780, 280)).save(verify)
print("saved", out)
