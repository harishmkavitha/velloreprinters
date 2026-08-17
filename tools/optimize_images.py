# -*- coding: utf-8 -*-
"""Generate WebP versions + a width/height cache for every photo, and build the
Open Graph social image. Run after adding/replacing photos:
    python3 tools/optimize_images.py
Then rebuild:  python3 tools/build.py
Requires Pillow (pip install pillow). If Pillow is missing the site still works;
it just serves JPGs without WebP/known dimensions.
"""
import os, json, glob
try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    raise SystemExit("Pillow required: pip install pillow")

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
IMGDIR = os.path.join(ROOT, "assets", "img")

def rel(p):
    return os.path.relpath(p, ROOT).replace(os.sep, "/")

def build_webp_and_meta():
    meta = {}
    jpgs = glob.glob(os.path.join(IMGDIR, "**", "*.jpg"), recursive=True)
    for p in jpgs:
        im = Image.open(p).convert("RGB")
        w, h = im.size
        webp = p.rsplit(".", 1)[0] + ".webp"
        im.save(webp, "WEBP", quality=80, method=6)
        meta[rel(p)] = {"w": w, "h": h, "webp": True}
    with open(os.path.join(os.path.dirname(__file__), "img_meta.json"), "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=1)
    print(f"WebP generated for {len(jpgs)} images; wrote img_meta.json")

def build_og_cover():
    """1200x630 branded social share image (CMYK marks + wordmark)."""
    W, H = 1200, 630
    im = Image.new("RGB", (W, H), "#111014")
    d = ImageDraw.Draw(im, "RGBA")
    # dot grid
    for y in range(40, H, 46):
        for x in range(40, W, 46):
            d.ellipse([x-2, y-2, x+2, y+2], fill=(255, 255, 255, 18))
    # overlapping CMYK discs (screen-ish via additive alpha)
    cx, cy, r = 930, 300, 150
    for (col, dx, dy) in [((0,174,239,190), -55, -55), ((236,0,140,190), 55, -55), ((255,210,0,190), 0, 55)]:
        d.ellipse([cx+dx-r, cy+dy-r, cx+dx+r, cy+dy+r], fill=col)
    # wordmark
    def font(sz, bold=True):
        for name in (["DejaVuSans-Bold.ttf"] if bold else ["DejaVuSans.ttf"]):
            for base in ["/usr/share/fonts/truetype/dejavu/", ""]:
                try:
                    return ImageFont.truetype(base + name, sz)
                except Exception:
                    continue
        return ImageFont.load_default()
    d.text((80, 210), "Vellore Printers", font=font(78), fill="#ffffff")
    d.text((84, 312), "Printing Press in Vellore", font=font(40, False), fill="#c9c8d4")
    d.text((84, 372), "Offset · Digital · Design", font=font(30, False), fill="#8e8c9c")
    # cmyk bar
    bar = ["#00aeef", "#ec008c", "#ffd200", "#ffffff"]
    for i, c in enumerate(bar):
        d.rectangle([84 + i*52, 452, 84 + i*52 + 44, 462], fill=c)
    out = os.path.join(IMGDIR, "og-cover.jpg")
    im.save(out, "JPEG", quality=86, optimize=True)
    Image.open(out).save(out.rsplit(".", 1)[0] + ".webp", "WEBP", quality=82)
    print("wrote og-cover.jpg (+webp)")

if __name__ == "__main__":
    build_og_cover()
    build_webp_and_meta()
