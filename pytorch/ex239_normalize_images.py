#!/usr/bin/env python3
import os
from pathlib import Path
from PIL import Image, ImageOps

# === CONFIG ===
TARGET_SIZE = (320, 320)        # (width, height)
INPUT_EXT = ".png"
OUTPUT_DIR = Path("standardized_pngs_padded")
BG_COLOR = (0, 0, 0)            # padding color (R,G,B) e.g., (0,0,0)=black or (255,255,255)=white
OUTPUT_DIR.mkdir(exist_ok=True)

# === HELPERS ===
def resize_with_padding(im: Image.Image, target_size, bg_color):
    target_w, target_h = target_size
    im = im.convert("RGBA") if im.mode == "RGBA" else im.convert("RGB")
    orig_w, orig_h = im.size

    # compute scale to fit within target while preserving aspect
    scale = min(target_w / orig_w, target_h / orig_h)
    new_w = max(1, int(orig_w * scale))
    new_h = max(1, int(orig_h * scale))
    im_resized = im.resize((new_w, new_h), Image.LANCZOS)

    # create background and paste centered
    if im_resized.mode == "RGBA":
        # Flatten with bg_color to remove alpha
        background = Image.new("RGB", target_size, bg_color)
        paste_x = (target_w - new_w) // 2
        paste_y = (target_h - new_h) // 2
        background.paste(im_resized, (paste_x, paste_y), im_resized)
        return background
    else:
        background = Image.new("RGB", target_size, bg_color)
        paste_x = (target_w - new_w) // 2
        paste_y = (target_h - new_h) // 2
        background.paste(im_resized, (paste_x, paste_y))
        return background

def process_image(in_path: Path, out_path: Path, size, bg_color):
    with Image.open(in_path) as im:
        out_im = resize_with_padding(im, size, bg_color)
        out_im.save(out_path, format="PNG", optimize=True)

# === MAIN ===
def main():
    cwd = Path(".")
    png_files = list(cwd.rglob(f"*{INPUT_EXT}"))
    if not png_files:
        print("No PNG files found.")
        return

    for p in png_files:
        # skip files in output dir to avoid reprocessing outputs
        try:
            if OUTPUT_DIR.resolve() in p.resolve().parents:
                continue
        except Exception:
            pass

        out_file = OUTPUT_DIR / p.name
        try:
            process_image(p, out_file, TARGET_SIZE, BG_COLOR)
            print(f"Saved: {out_file}")
        except Exception as e:
            print(f"Failed {p}: {e}")

if __name__ == "__main__":
    main()
