# -*- coding: utf-8 -*-
"""
FY301 产品部件原理动画
- 每个部件用对应实物照片
- 半透明透视（ghost / cutaway）
- 可见动作：压电弯曲、气流、膜片起伏、滑阀位移、霍尔反馈
输出 out/product_parts/
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation, FFMpegWriter
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch, Ellipse, Rectangle
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageOps

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "out"
OUT.mkdir(exist_ok=True)

PRODUCT_OUT = ROOT / "out" / "product_parts"
ASSETS = PRODUCT_OUT / "_assets"
PRODUCT_OUT.mkdir(parents=True, exist_ok=True)
ASSETS.mkdir(parents=True, exist_ok=True)
OUT = PRODUCT_OUT  # legacy alias within this script

from fy301_common import load_parts_index  # noqa: E402

try:
    import imageio_ffmpeg

    FF = imageio_ffmpeg.get_ffmpeg_exe()
    plt.rcParams["animation.ffmpeg_path"] = FF
except Exception:
    FF = None

from matplotlib import font_manager

_CJK = None
for _name in ("Microsoft YaHei", "SimHei", "WenQuanYi Micro Hei", "Noto Sans CJK SC"):
    for _f in font_manager.fontManager.ttflist:
        if _name.lower() in (_f.name or "").lower():
            _CJK = _f.name
            break
    if _CJK:
        break
if _CJK is None:
    for _f in font_manager.fontManager.ttflist:
        if any(k in (_f.name or "") for k in ("CJK", "Hei", "YaHei", "WenQuanYi")):
            _CJK = _f.name
            break
plt.rcParams["font.sans-serif"] = [_CJK or "DejaVu Sans", "SimHei", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

FPS = 20
DPI = 100
W, H = 1280, 720
BG = "#0b1220"
FG = "#e8eef7"
ACCENT = "#4fc3f7"
AIR = "#ffb74d"
PIEZO = "#ce93d8"
OK = "#81c784"
WARN = "#ff8a65"


def load_rgb(path: Path) -> Image.Image:
    return Image.open(path).convert("RGBA")


def soft_cutout(im: Image.Image, chroma_keys=None) -> Image.Image:
    """Approximate transparent cutout without rembg (green cloth / cardboard / white paper)."""
    arr = np.asarray(im).astype(np.float32)
    r, g, b, a = arr[..., 0], arr[..., 1], arr[..., 2], arr[..., 3]
    # green fabric
    green = (g > r + 25) & (g > b + 15) & (g > 80)
    # brown cardboard
    brown = (r > 90) & (g > 60) & (b < 90) & (r > b + 30) & (g > b + 15)
    # near-white paper
    white = (r > 210) & (g > 210) & (b > 210)
    # wood-ish
    wood = (r > 100) & (g > 70) & (b < 100) & (r - b > 40)
    mask_bg = green | brown | white | wood
    alpha = np.where(mask_bg, 0, 255).astype(np.uint8)
    # feather
    alpha_img = Image.fromarray(alpha, mode="L").filter(ImageFilter.GaussianBlur(1.2))
    out = im.copy()
    out.putalpha(alpha_img)
    return out


def make_ghost(im: Image.Image, alpha: float = 0.45) -> Image.Image:
    out = im.copy()
    a = np.asarray(out.split()[-1]).astype(np.float32)
    a = (a * alpha).astype(np.uint8)
    bands = list(out.split())
    bands[-1] = Image.fromarray(a)
    return Image.merge("RGBA", bands)


def fit_canvas(im: Image.Image, size=(W, H), pad=40) -> Image.Image:
    canvas = Image.new("RGBA", size, (11, 18, 32, 255))
    im2 = im.copy()
    im2.thumbnail((size[0] - pad * 2, size[1] - pad * 2), Image.Resampling.LANCZOS)
    x = (size[0] - im2.width) // 2
    y = (size[1] - im2.height) // 2
    canvas.alpha_composite(im2, (x, y))
    return canvas, (x, y, im2.width, im2.height)


def save_anim(fig, anim, name: str):
    path = OUT / f"{name}.mp4"
    if FF:
        writer = FFMpegWriter(fps=FPS, bitrate=3500)
        print(f"[..] {name}", flush=True)
        anim.save(str(path), writer=writer, dpi=DPI)
        print(f"[OK] {path}", flush=True)
    else:
        path = OUT / f"{name}.gif"
        anim.save(str(path), writer="pillow", fps=FPS, dpi=DPI)
        print(f"[OK] {path}", flush=True)
    plt.close(fig)


def style(ax, title):
    ax.set_xlim(0, W)
    ax.set_ylim(H, 0)
    ax.axis("off")
    ax.set_facecolor(BG)
    ax.set_title(title, color=FG, fontsize=14, pad=8, fontweight="bold")


# ---------- prepare cropped assets from FY301 SKD ----------
def prepare_assets():
    by_name = load_parts_index()
    skd_path = by_name.get("FY301 SKD Parts.jpeg")
    if skd_path is None or not skd_path.exists():
        raise SystemExit(
            "SKD photos not found. Place files under AI研发产品/SMAR SKD/ "
            "then run: python rebuild_parts_index.py"
        )
    skd = load_rgb(skd_path)
    # approximate crops on  original resolution
    ow, oh = skd.size
    # normalized crops (l,t,r,b) based on layout description
    crops = {
        "pneumatic_block": (0.02, 0.02, 0.38, 0.78),  # left tall block IN/OUT
        "housing": (0.34, 0.08, 0.62, 0.72),
        "pcb_display": (0.36, 0.55, 0.62, 0.95),
        "cover_solid": (0.60, 0.28, 0.78, 0.72),
        "cover_glass": (0.76, 0.28, 0.98, 0.72),
        "fittings": (0.05, 0.72, 0.32, 0.98),
        "hall_base": (0.00, 0.78, 0.18, 1.00),
    }
    paths = {}
    for key, (l, t, r, b) in crops.items():
        box = (int(l * ow), int(t * oh), int(r * ow), int(b * oh))
        part = skd.crop(box)
        cut = soft_cutout(part)
        ghost = make_ghost(cut, 0.55)
        p = ASSETS / f"{key}.png"
        g = ASSETS / f"{key}_ghost.png"
        cut.save(p)
        ghost.save(g)
        paths[key] = p
        paths[key + "_ghost"] = g

    # close-up parts
    extra = {
        "pcb_front": by_name.get("301线路板正面.jpeg"),
        "diaphragm": by_name.get("FY501膜片.png"),
        "flapper": by_name.get("挡板01.jpg"),
        "flapper2": by_name.get("挡板02.jpg"),
        "coil": by_name.get("线圈01.jpg"),
        "ip_top": by_name.get("上部小板.jpg"),
        "ip_base": by_name.get("下部大板.jpg"),
        "test_platform": by_name.get("FY301 Test Plateform.jpeg"),
        "skd_full": skd_path,
    }
    for k, p in extra.items():
        if p is None or not Path(p).exists():
            continue
        im = load_rgb(p)
        cut = soft_cutout(im)
        cut.save(ASSETS / f"{k}.png")
        make_ghost(cut, 0.5).save(ASSETS / f"{k}_ghost.png")
        paths[k] = ASSETS / f"{k}.png"
        paths[k + "_ghost"] = ASSETS / f"{k}_ghost.png"

    (ASSETS / "manifest.json").write_text(json.dumps({k: str(v) for k, v in paths.items()}, ensure_ascii=False, indent=2), encoding="utf-8")
    return paths


def pil_to_ax(ax, im: Image.Image, xy=(0, 0), alpha=1.0):
    """Draw RGBA PIL image on matplotlib axes in pixel coords."""
    arr = np.asarray(im)
    x, y = xy
    ax.imshow(arr, extent=[x, x + im.width, y + im.height, y], alpha=alpha, interpolation="bilinear", zorder=2)


# ============================================================
# 01 气动块：半透明壳体 + IN/OUT 气流动作
# ============================================================
def render_pneumatic(paths):
    base = Image.open(paths["pneumatic_block"]).convert("RGBA")
    ghost = Image.open(paths["pneumatic_block_ghost"]).convert("RGBA")
    canvas_bg = Image.new("RGBA", (W, H), (11, 18, 32, 255))

    fig, ax = plt.subplots(figsize=(W / DPI, H / DPI), dpi=DPI, facecolor=BG)
    style(ax, "气动块实物 · 半透明透视 · IN / OUT1 / OUT2 气流动作")
    n = 100
    n_part = 24

    def frame(k):
        ax.clear()
        style(ax, "气动块实物 · 半透明透视 · IN / OUT1 / OUT2 气流动作")
        t = k / n
        phase = 0.5 + 0.5 * math.sin(t * 2 * math.pi)

        # solid faint + stronger ghost to show "透视"
        solid = base.copy()
        solid.putalpha(ImageEnhance.Brightness(solid.split()[-1]).enhance(0.35) if False else solid.split()[-1].point(lambda a: int(a * 0.35)))
        # simpler alpha set
        a = np.asarray(base.split()[-1])
        solid_a = Image.fromarray((a * 0.38).astype(np.uint8))
        solid2 = base.copy()
        solid2.putalpha(solid_a)

        g = ghost.copy()
        fitted, (x0, y0, w0, h0) = fit_canvas(solid2, (W, H), 60)
        # rebuild: place ghost on dark bg
        bg = Image.new("RGBA", (W, H), (11, 18, 32, 255))
        g2 = g.copy()
        g2.thumbnail((W - 120, H - 120), Image.Resampling.LANCZOS)
        gx = (W - g2.width) // 2
        gy = (H - g2.height) // 2 - 20
        bg.alpha_composite(g2, (gx, gy))
        # extra transparent outline layer
        outline = g2.copy()
        oa = np.asarray(outline.split()[-1]).astype(np.float32)
        outline.putalpha(Image.fromarray((oa * 0.55).astype(np.uint8)))
        bg.alpha_composite(outline, (gx, gy))
        pil_to_ax(ax, bg)

        # ports relative to image
        # approximate port positions on crop
        cx = gx + g2.width * 0.72
        yin = gy + g2.height * 0.48
        y1 = gy + g2.height * 0.62
        y2 = gy + g2.height * 0.34
        pin_in = (gx + g2.width * 0.15, yin)
        # internal chamber ghost
        chamber = FancyBboxPatch(
            (gx + g2.width * 0.25, gy + g2.height * 0.18),
            g2.width * 0.45,
            g2.height * 0.55,
            boxstyle="round,pad=4",
            facecolor=(0.31, 0.76, 0.97, 0.12 + 0.18 * phase),
            edgecolor=ACCENT,
            lw=1.5,
            zorder=5,
        )
        ax.add_patch(chamber)
        ax.text(gx + g2.width * 0.47, gy + g2.height * 0.12, "先导/滑阀腔（透视）", color=ACCENT, ha="center", fontsize=11, zorder=6)

        # spool motion (visible)
        spool_y = gy + g2.height * (0.42 - 0.10 * (phase - 0.5) * 2)
        ax.add_patch(
            FancyBboxPatch(
                (gx + g2.width * 0.38, spool_y),
                g2.width * 0.18,
                g2.height * 0.12,
                boxstyle="round,pad=2",
                facecolor=(0.5, 0.55, 0.6, 0.55),
                edgecolor=FG,
                lw=1.5,
                zorder=7,
            )
        )
        ax.text(gx + g2.width * 0.47, spool_y - 8, "滑阀动作", color=FG, ha="center", fontsize=9, zorder=8)

        # air particles
        xs, ys, cs = [], [], []
        for i in range(n_part):
            u = (i / n_part + t * (0.9 + 0.5 * phase)) % 1.0
            if u < 0.35:  # enter IN
                xs.append(gx + g2.width * (0.05 + u / 0.35 * 0.35))
                ys.append(yin + 6 * math.sin(u * 20 + i))
                cs.append(AIR)
            elif phase > 0.55:  # to OUT1
                xs.append(gx + g2.width * (0.55 + (u - 0.35) / 0.65 * 0.4))
                ys.append(y1 + 8 * math.sin(u * 15))
                cs.append(OK)
            else:  # to OUT2
                xs.append(gx + g2.width * (0.55 + (u - 0.35) / 0.65 * 0.4))
                ys.append(y2 + 8 * math.sin(u * 15))
                cs.append(WARN)
        ax.scatter(xs, ys, c=cs, s=36, alpha=0.9, zorder=9)

        # labels
        ax.annotate("IN 供气", xy=(gx + g2.width * 0.2, yin), xytext=(40, yin), color=AIR, fontsize=12, arrowprops=dict(arrowstyle="->", color=AIR), zorder=10)
        ax.annotate("OUT1", xy=(gx + g2.width * 0.85, y1), xytext=(W - 120, y1), color=OK, fontsize=12, arrowprops=dict(arrowstyle="->", color=OK), zorder=10)
        ax.annotate("OUT2", xy=(gx + g2.width * 0.85, y2), xytext=(W - 120, y2), color=WARN, fontsize=12, arrowprops=dict(arrowstyle="->", color=WARN), zorder=10)

        mode = "先导↑ → 滑阀上移 → OUT1 供气增强" if phase > 0.55 else "先导↓ → 滑阀下移 → OUT2 供气增强"
        ax.text(W / 2, H - 36, mode, color=FG, ha="center", fontsize=13, zorder=12)
        return ()

    anim = FuncAnimation(fig, frame, frames=n, interval=1000 / FPS)
    save_anim(fig, anim, "P01_气动块_透明气流")


# ============================================================
# 02 挡板/压电：实物挡板半透明 + 弯曲动作
# ============================================================
def render_flapper(paths):
    flap = Image.open(ASSETS / "flapper.png").convert("RGBA")
    # crop center disc area roughly
    fw, fh = flap.size
    flap = flap.crop((int(fw * 0.25), int(fh * 0.15), int(fw * 0.75), int(fh * 0.85)))

    fig, ax = plt.subplots(figsize=(W / DPI, H / DPI), dpi=DPI, facecolor=BG)
    n = 100

    def warp_bend(im: Image.Image, amount: float) -> Image.Image:
        """Vertical bow warp to simulate bending."""
        arr = np.asarray(im)
        h, w = arr.shape[:2]
        ys, xs = np.meshgrid(np.arange(h), np.arange(w), indexing="ij")
        # displace y toward center based on x parabola
        nx = (xs / max(w - 1, 1) - 0.5) * 2
        shift = (amount * 18 * (1 - nx**2)).astype(np.int32)
        ys2 = np.clip(ys - shift, 0, h - 1)
        out = arr[ys2, xs]
        return Image.fromarray(out)

    def frame(k):
        ax.clear()
        style(ax, "挡板实物 · 半透明 · 压电弯曲靠近/远离喷嘴（可见动作）")
        t = k / n
        bend = 0.5 + 0.5 * math.sin(t * 2 * math.pi)  # 0..1
        V = bend * 100

        # ghost base
        g = make_ghost(flap, 0.35 + 0.25 * bend)
        bent = warp_bend(g, bend)
        # also a sharper opaque edge for motion readability
        edge = warp_bend(make_ghost(flap, 0.75), bend)

        bg = Image.new("RGBA", (W, H), (11, 18, 32, 255))
        for layer, alpha_mul in ((bent, 1.0), (edge, 0.65)):
            L = layer.copy()
            L.thumbnail((520, 520), Image.Resampling.LANCZOS)
            x = (W - L.width) // 2
            y = (H - L.height) // 2 - 30
            bg.alpha_composite(L, (x, y))
        pil_to_ax(ax, bg)

        # nozzle ghost below
        nx, ny = W / 2, H / 2 + 160 - bend * 35
        ax.add_patch(Rectangle((W / 2 - 28, ny), 56, 70, facecolor=(1, 0.72, 0.3, 0.35), edgecolor=AIR, lw=2, zorder=6))
        ax.text(W / 2, ny + 90, "喷嘴（示意）", color=AIR, ha="center", fontsize=11, zorder=7)

        # gap arrow
        gap = 48 - bend * 36
        ax.annotate(
            "",
            xy=(W / 2 + 80, ny - 5),
            xytext=(W / 2 + 80, ny - 5 - gap),
            arrowprops=dict(arrowstyle="<->", color=PIEZO, lw=2),
            zorder=8,
        )
        ax.text(W / 2 + 110, ny - gap / 2, f"间隙 δ\nV≈{V:.0f}V", color=PIEZO, fontsize=11, zorder=8)

        # particles escaping when gap large
        rng_n = 16
        xs, ys = [], []
        for i in range(rng_n):
            u = (i / rng_n + t * (1.2 - 0.8 * bend)) % 1
            if bend < 0.55:
                xs.append(W / 2 + 10 * math.sin(u * 30 + i))
                ys.append(ny + 20 + u * 120)
            else:
                xs.append(W / 2 - 60 + u * 120)
                ys.append(ny - 40 + 20 * math.sin(u * 12))
        ax.scatter(xs, ys, c=AIR if bend < 0.55 else WARN, s=28, alpha=0.85, zorder=9)

        tip = "挡板远离 → 排气畅通 → 先导压↓" if bend < 0.55 else "挡板靠近 → 堵住喷嘴 → 先导压↑"
        ax.text(W / 2, H - 40, tip, color=FG, ha="center", fontsize=13, zorder=10)
        ax.text(60, 60, "实物：FY501 挡板特写（同类喷嘴挡板结构参考）\nFY301 用压电盘驱动同等挡板动作", color="#94a3b8", fontsize=10, va="top")
        return ()

    anim = FuncAnimation(fig, frame, frames=n, interval=1000 / FPS)
    save_anim(fig, anim, "P02_挡板_透明弯曲动作")


# ============================================================
# 03 膜片：实物半透明 + 起伏驱动连杆
# ============================================================
def render_diaphragm(paths):
    dia = Image.open(ASSETS / "diaphragm.png").convert("RGBA")

    fig, ax = plt.subplots(figsize=(W / DPI, H / DPI), dpi=DPI, facecolor=BG)
    n = 100

    def frame(k):
        ax.clear()
        style(ax, "膜片实物 · 半透明 · 先导压驱动起伏（力放大可见）")
        t = k / n
        p = 0.5 + 0.5 * math.sin(t * 2 * math.pi)  # pilot pressure norm

        g = make_ghost(dia, 0.4 + 0.25 * p)
        # scale pulse to show inflation
        scale = 0.92 + 0.12 * p
        gw, gh = g.size
        nw, nh = int(gw * scale), int(gh * scale)
        g2 = g.resize((nw, nh), Image.Resampling.LANCZOS)

        bg = Image.new("RGBA", (W, H), (11, 18, 32, 255))
        x = (W - nw) // 2
        y = int(H * 0.22 - p * 18)
        bg.alpha_composite(g2, (x, y))
        # second ghost layer offset for depth
        g3 = make_ghost(dia, 0.22)
        g3 = g3.resize((int(gw * 0.88), int(gh * 0.88)), Image.Resampling.LANCZOS)
        bg.alpha_composite(g3, ((W - g3.width) // 2, int(H * 0.28)))
        pil_to_ax(ax, bg)

        # force arrows
        ax.annotate("", xy=(W / 2, y - 10), xytext=(W / 2, y - 80), arrowprops=dict(arrowstyle="->", color=ACCENT, lw=2.5), zorder=6)
        ax.text(W / 2 + 20, y - 70, f"P_pilot · A\n先导压→{p*12:.1f} psi(示意)", color=ACCENT, fontsize=11, zorder=6)

        # link motion
        link_y0 = y + nh - 10
        link_y1 = link_y0 + 90 + p * 40
        ax.plot([W / 2, W / 2], [link_y0, link_y1], color=FG, lw=4, alpha=0.8, zorder=7)
        ax.add_patch(FancyBboxPatch((W / 2 - 50, link_y1), 100, 36, boxstyle="round,pad=2", facecolor=(0.47, 0.56, 0.6, 0.55), edgecolor=WARN, lw=1.5, zorder=8))
        ax.text(W / 2, link_y1 + 18, "连杆 → 滑阀", color=FG, ha="center", va="center", fontsize=11, zorder=9)

        ax.text(W / 2, H - 40, "大膜片起伏（透明）→ 力放大 → 推动滑阀", color=FG, ha="center", fontsize=13)
        return ()

    anim = FuncAnimation(fig, frame, frames=n, interval=1000 / FPS)
    save_anim(fig, anim, "P03_膜片_透明起伏动作")


# ============================================================
# 04 线路板：半透明 + 信号流向压电排线
# ============================================================
def render_pcb(paths):
    pcb = Image.open(ASSETS / "pcb_front.png").convert("RGBA")
    fig, ax = plt.subplots(figsize=(W / DPI, H / DPI), dpi=DPI, facecolor=BG)
    n = 90

    def frame(k):
        ax.clear()
        style(ax, "主控/显示板实物 · 半透明 · 4-20mA→CPU→压电驱动")
        t = k / n
        g = make_ghost(pcb, 0.55)
        bg = Image.new("RGBA", (W, H), (11, 18, 32, 255))
        g2 = g.copy()
        g2.thumbnail((700, 700), Image.Resampling.LANCZOS)
        x = (W - g2.width) // 2 - 80
        y = (H - g2.height) // 2
        bg.alpha_composite(g2, (x, y))
        pil_to_ax(ax, bg)

        # signal particle path
        path = [
            (80, H * 0.7),
            (x + 40, y + g2.height * 0.75),
            (x + g2.width * 0.5, y + g2.height * 0.5),
            (x + g2.width * 0.85, y + g2.height * 0.35),
            (W - 100, H * 0.3),
        ]
        # draw path
        xs = [p[0] for p in path]
        ys = [p[1] for p in path]
        ax.plot(xs, ys, color=ACCENT, lw=1.5, alpha=0.35, zorder=5)
        # moving dots
        for i in range(8):
            u = (t + i / 8) % 1
            seg = min(int(u * (len(path) - 1)), len(path) - 2)
            local = u * (len(path) - 1) - seg
            x0, y0 = path[seg]
            x1, y1 = path[seg + 1]
            ax.scatter([x0 + (x1 - x0) * local], [y0 + (y1 - y0) * local], c=PIEZO, s=48, zorder=8, alpha=0.95)

        ax.text(80, H * 0.7 + 24, "4–20mA", color=ACCENT, fontsize=11)
        ax.text(x + g2.width * 0.5, y - 10, "CPU / HART", color=OK, ha="center", fontsize=11)
        ax.text(W - 100, H * 0.3 - 20, "压电驱动\n30–70V", color=PIEZO, ha="center", fontsize=11)

        # voltage pulse bar
        V = 30 + 40 * (0.5 + 0.5 * math.sin(t * 2 * math.pi))
        ax.add_patch(Rectangle((W - 160, H - 160), 40, 100, facecolor="#1e293b", edgecolor=FG, lw=1, zorder=6))
        ax.add_patch(Rectangle((W - 156, H - 60 - V), 32, V, facecolor=PIEZO, alpha=0.8, zorder=7))
        ax.text(W - 140, H - 40, f"{V:.0f}V", color=PIEZO, ha="center", fontsize=11, zorder=8)

        ax.text(W / 2, H - 36, "电信号在实物板上流动（半透明透视）", color=FG, ha="center", fontsize=13)
        return ()

    anim = FuncAnimation(fig, frame, frames=n, interval=1000 / FPS)
    save_anim(fig, anim, "P04_线路板_透明信号流")


# ============================================================
# 05 整机拆解：半透明部件分层 + 动作联锁
# ============================================================
def render_assembly(paths):
    skd = Image.open(ASSETS / "skd_full.png").convert("RGBA")
    fig, ax = plt.subplots(figsize=(W / DPI, H / DPI), dpi=DPI, facecolor=BG)
    n = 120

    layers = []
    for key, label, color in [
        ("pneumatic_block_ghost", "气动块", AIR),
        ("pcb_display_ghost", "显示/主板", ACCENT),
        ("housing_ghost", "壳体", OK),
        ("cover_glass_ghost", "观察窗盖", FG),
    ]:
        p = ASSETS / f"{key.replace('_ghost','')}_ghost.png"
        if not p.exists():
            p = ASSETS / f"{key}.png" if (ASSETS / f"{key}.png").exists() else None
        if p and p.exists():
            layers.append((Image.open(p).convert("RGBA"), label, color))

    def frame(k):
        ax.clear()
        style(ax, "FY301 实物拆解 · 半透明分层 · 原理动作联锁")
        t = k / n
        phase = 0.5 + 0.5 * math.sin(t * 2 * math.pi)

        # full skd as faint background plate
        bg = Image.new("RGBA", (W, H), (11, 18, 32, 255))
        base = make_ghost(skd, 0.22)
        base.thumbnail((1180, 700), Image.Resampling.LANCZOS)
        bx = (W - base.width) // 2
        by = (H - base.height) // 2
        bg.alpha_composite(base, (bx, by))

        # highlight regions pulsing
        # draw translucent boxes over pneumatic / pcb areas (relative to skd fit)
        pil_to_ax(ax, bg)
        # pneumatic highlight left
        ax.add_patch(
            FancyBboxPatch(
                (bx + base.width * 0.02, by + base.height * 0.05),
                base.width * 0.34,
                base.height * 0.7,
                boxstyle="round,pad=3",
                facecolor=(1.0, 0.72, 0.3, 0.08 + 0.10 * phase),
                edgecolor=AIR,
                lw=2,
                zorder=5,
            )
        )
        ax.add_patch(
            FancyBboxPatch(
                (bx + base.width * 0.36, by + base.height * 0.55),
                base.width * 0.26,
                base.height * 0.38,
                boxstyle="round,pad=3",
                facecolor=(0.31, 0.76, 0.97, 0.08 + 0.10 * (1 - phase)),
                edgecolor=ACCENT,
                lw=2,
                zorder=5,
            )
        )

        # motion: air particles on pneumatic zone
        xs, ys = [], []
        for i in range(18):
            u = (i / 18 + t) % 1
            xs.append(bx + base.width * (0.08 + u * 0.25))
            ys.append(by + base.height * (0.35 + 0.15 * math.sin(u * 12 + i) + 0.05 * phase))
        ax.scatter(xs, ys, c=AIR, s=22, alpha=0.85, zorder=8)

        # motion: signal dots to pcb
        xs2, ys2 = [], []
        for i in range(10):
            u = (i / 10 + t * 0.8) % 1
            xs2.append(bx + base.width * (0.4 + u * 0.18))
            ys2.append(by + base.height * (0.7 - u * 0.05))
        ax.scatter(xs2, ys2, c=PIEZO, s=26, alpha=0.9, zorder=8)

        ax.text(bx + base.width * 0.19, by + 24, "气动执行（透明高亮）", color=AIR, ha="center", fontsize=11, zorder=9)
        ax.text(bx + base.width * 0.49, by + base.height * 0.52, "电子控制", color=ACCENT, ha="center", fontsize=11, zorder=9)

        ax.text(
            W / 2,
            H - 40,
            "电信号 → 压电挡板 → 先导压 → 膜片/滑阀 → OUT1/OUT2（叠在实物拆解图上）",
            color=FG,
            ha="center",
            fontsize=12,
            zorder=10,
        )
        return ()

    anim = FuncAnimation(fig, frame, frames=n, interval=1000 / FPS)
    save_anim(fig, anim, "P05_整机拆解_透明联锁")


# ============================================================
# 06 测试台：半透明 + 气路动作
# ============================================================
def render_testbench(paths):
    im = Image.open(ASSETS / "test_platform.png").convert("RGBA")
    fig, ax = plt.subplots(figsize=(W / DPI, H / DPI), dpi=DPI, facecolor=BG)
    n = 90

    def frame(k):
        ax.clear()
        style(ax, "FY301 测试台实物 · 半透明 · 气路/电测动作")
        t = k / n
        g = make_ghost(im, 0.5)
        bg = Image.new("RGBA", (W, H), (11, 18, 32, 255))
        g2 = g.copy()
        g2.thumbnail((520, 680), Image.Resampling.LANCZOS)
        x = (W - g2.width) // 2
        y = (H - g2.height) // 2
        bg.alpha_composite(g2, (x, y))
        pil_to_ax(ax, bg)

        # flowing along tubes (schematic overlay)
        for i in range(20):
            u = (i / 20 + t) % 1
            ax.scatter(
                [x + g2.width * (0.15 + 0.7 * u)],
                [y + g2.height * (0.25 + 0.1 * math.sin(u * 10 + i) + 0.35 * ((i % 3) / 3))],
                c=AIR,
                s=20,
                alpha=0.75,
                zorder=6,
            )
        ax.add_patch(
            FancyBboxPatch(
                (x + 8, y + 8),
                g2.width - 16,
                g2.height - 16,
                boxstyle="round,pad=2",
                facecolor=(1, 1, 1, 0.03),
                edgecolor=(1, 0.72, 0.3, 0.5),
                lw=1.5,
                zorder=5,
            )
        )
        ax.text(W / 2, H - 40, "测试台气管中气流粒子（叠在实物半透明图上）", color=FG, ha="center", fontsize=12)
        return ()

    anim = FuncAnimation(fig, frame, frames=n, interval=1000 / FPS)
    save_anim(fig, anim, "P06_测试台_透明气路")


def concat_master():
    if not FF:
        return
    files = sorted(OUT.glob("P0*.mp4"))
    if len(files) < 2:
        return
    lst = OUT / "_concat.txt"
    lst.write_text("\n".join(f"file '{p.resolve().as_posix()}'" for p in files), encoding="utf-8")
    dest = OUT / "FY301_产品部件透明原理_完整版.mp4"
    import subprocess

    subprocess.run(
        [FF, "-y", "-f", "concat", "-safe", "0", "-i", str(lst), "-c:v", "libx264", "-pix_fmt", "yuv420p", str(dest)],
        check=False,
    )
    print("[OK] master", dest, flush=True)


def main():
    print("prepare assets...", flush=True)
    paths = prepare_assets()
    # ensure diaphragm path key
    if "diaphragm" not in paths and (ASSETS / "diaphragm.png").exists():
        paths["diaphragm"] = ASSETS / "diaphragm.png"
    # skip already done if present
    import sys
    only = sys.argv[1:] if len(sys.argv) > 1 else []
    jobs = [
        ("P01", render_pneumatic),
        ("P02", render_flapper),
        ("P03", render_diaphragm),
        ("P04", render_pcb),
        ("P05", render_assembly),
        ("P06", render_testbench),
    ]
    for key, fn in jobs:
        if only and key not in only:
            continue
        done = list(OUT.glob(f"{key}*.mp4"))
        if not only and done and key in ("P01", "P02", "P03"):
            print(f"skip existing {key}", flush=True)
            continue
        fn(paths)
    concat_master()
    print("ALL DONE", flush=True)


if __name__ == "__main__":
    main()
