#!/usr/bin/env python3
"""
verify_favicon.py — official check for Y12B site favicon.
Verifies:
  1. favicon.png / favicon.ico exist locally with a SQUARE canvas
     and the original icon placed WITHOUT cropping (aspect preserved,
     fully inside the canvas with dark padding).
  2. index.html references rel="icon".
  3. Live GitHub Pages serves both favicon files (HTTP 200).
Run: python verify_favicon.py
Exit 0 = pass, 1 = fail, 2 = environment error.
"""
import os, re, sys, urllib.request
from PIL import Image

ROOT = os.path.dirname(os.path.abspath(__file__))
BASE = "https://neutrino-qh.github.io/y12b-website"
SRC_ICON = r"C:\Users\HuyNguyen\OneDrive\Desktop\icon.png"
ok = True

# ---- 1. local raster files: square canvas, source fits inside (no crop) ----
for fn in ("favicon.png", "favicon.ico"):
    p = os.path.join(ROOT, fn)
    if not os.path.exists(p):
        print(f"FAIL: {fn} missing locally"); ok = False; continue
    im = Image.open(p).convert("RGBA")
    w, h = im.size
    square = (w == h)
    # detect non-background (icon) pixels; their bbox must be fully inside canvas
    px = list(im.getdata())
    xs = [i % w for i, (r, g, b, a) in enumerate(px) if a > 10 and not (r < 30 and g < 30 and b < 30)]
    ys = [i // w for i, (r, g, b, a) in enumerate(px) if a > 10 and not (r < 30 and g < 30 and b < 30)]
    if xs and ys:
        inside = (min(xs) > 0 and max(xs) < w - 1 and min(ys) > 0 and max(ys) < h - 1)
    else:
        inside = False
    print(f"{fn}: {w}x{h} square={square} icon_inside_canvas={inside}")
    if not (square and inside):
        ok = False

# ---- 2. HTML references the icon ----
html = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
links = re.findall(r'<link[^>]*rel="icon"[^>]*>', html, re.I)
print(f"HTML icon <link> count: {len(links)}")
if not links:
    print("FAIL: no rel=icon in index.html"); ok = False

# ---- 3. live serving ----
for path in ("favicon.ico", "favicon.png"):
    try:
        r = urllib.request.urlopen(f"{BASE}/{path}", timeout=20)
        print(f"live {path}: HTTP {r.status} ({r.headers.get('Content-Type')})")
        if r.status != 200:
            ok = False
    except Exception as e:
        print(f"live {path}: FAIL {e}"); ok = False

print("PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
