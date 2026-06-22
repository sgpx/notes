#!/usr/bin/env python3
import os, glob
from PIL import Image

INPUT_DIR = "./frames"
PATTERN = "*.png"
THRESHOLD = 0.30
G_MIN = 80
GB_MARGIN = 30

def is_green_pixel(r, g, b):
    return (g >= G_MIN) and (g - r >= GB_MARGIN) and (g - b >= GB_MARGIN)

def green_fraction(path, thumb_size=256):
    with Image.open(path) as im:
        im = im.convert("RGB")
        im.thumbnail((thumb_size, thumb_size))
        px = im.getdata()
        total = 0
        green = 0
        for r, g, b in px:
            total += 1
            if is_green_pixel(r, g, b):
                green += 1
        return (green / total) if total else 0.0

def main():
    os.makedirs(INPUT_DIR, exist_ok=True)
    paths = sorted(glob.glob(os.path.join(INPUT_DIR, PATTERN)))
    for p in paths:
        frac = green_fraction(p)
        if frac < THRESHOLD:
            os.remove(p)
            print(f"DELETED {p} (green {frac:.2%})")

if __name__ == "__main__":
    main()
