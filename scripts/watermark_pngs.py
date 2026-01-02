#!/usr/bin/env python3

# EXAMPLE: python ./scripts/watermark_pngs.py ./figs --inplace

import os
import argparse
from PIL import Image, ImageDraw, ImageFont

DEFAULT_TEXT = "EXAMPLE\n------\n\n\nPLACEHOLDER"

def load_font(size: int, font_path: str | None):
    if font_path:
        return ImageFont.truetype(font_path, size)
    # Try a few common fonts; fall back to PIL default
    candidates = [
        "DejaVuSans-Bold.ttf",  # common on Linux
        "DejaVuSans.ttf",
        "Arial.ttf",            # common on Windows/macOS (may not exist)
    ]
    for name in candidates:
        try:
            return ImageFont.truetype(name, size)
        except Exception:
            pass
    return ImageFont.load_default()

def fit_font(draw: ImageDraw.ImageDraw, text: str, base_w: int, base_h: int, font_path: str | None):
    # Start size proportional to image, then shrink if needed
    size = max(18, int(min(base_w, base_h) * 0.09))
    while size > 10:
        font = load_font(size, font_path)
        bbox = draw.textbbox((0, 0), text, font=font)
        tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
        if tw <= base_w * 0.9:
            return font, (tw, th)
        size = int(size * 0.9)
    font = load_font(12, font_path)
    bbox = draw.textbbox((0, 0), text, font=font)
    return font, (bbox[2] - bbox[0], bbox[3] - bbox[1])

def add_watermark(img: Image.Image, text: str, opacity: int, angle: float, font_path: str | None):
    base = img.convert("RGBA")
    w, h = base.size

    # Draw on a larger canvas so rotation doesn’t clip
    big_w, big_h = int(w * 1.5), int(h * 1.5)
    big = Image.new("RGBA", (big_w, big_h), (0, 0, 0, 0))
    d = ImageDraw.Draw(big)


    font, (tw, th) = fit_font(d, text, big_w, big_h, font_path)
    # Split text into lines and calculate total height
    lines = text.split("\n")
    line_heights = []
    line_widths = []
    for line in lines:
        bbox = d.textbbox((0, 0), line, font=font)
        line_widths.append(bbox[2] - bbox[0])
        line_heights.append(bbox[3] - bbox[1])
    # Add spacing between lines (e.g., 30% of font size)
    line_spacing = int(font.size * 0.3)
    total_height = sum(line_heights) + line_spacing * (len(lines) - 1)
    y = (big_h - total_height) // 2
    # Draw each line centered horizontally with spacing
    for i, line in enumerate(lines):
        lw = line_widths[i]
        lh = line_heights[i]
        x = (big_w - lw) // 2
        d.text((x, y), line, font=font, fill=(128, 128, 128, opacity))
        y += lh + line_spacing

    rotated = big.rotate(angle, resample=Image.Resampling.BICUBIC, expand=False)

    # Crop back to original size (center crop)
    left = (big_w - w) // 2
    top = (big_h - h) // 2
    wm = rotated.crop((left, top, left + w, top + h))

    out = Image.alpha_composite(base, wm)
    return out

def process_dir(input_root: str, output_root: str, inplace: bool, text: str, opacity: int, angle: float, font_path: str | None):
    for dirpath, _, filenames in os.walk(input_root):
        for fn in filenames:
            if not fn.lower().endswith(".png"):
                continue

            in_path = os.path.join(dirpath, fn)
            rel = os.path.relpath(in_path, input_root)

            if inplace:
                out_path = in_path
                tmp_path = in_path + ".tmp.png"
            else:
                out_path = os.path.join(output_root, rel)
                os.makedirs(os.path.dirname(out_path), exist_ok=True)

            try:
                with Image.open(in_path) as im:
                    watermarked = add_watermark(im, text=text, opacity=opacity, angle=angle, font_path=font_path)

                if inplace:
                    watermarked.save(tmp_path, format="PNG")
                    os.replace(tmp_path, out_path)
                else:
                    watermarked.save(out_path, format="PNG")

                print(f"OK  {rel}")
            except Exception as e:
                print(f"ERR {rel}: {e}")

def main():
    p = argparse.ArgumentParser(description="Watermark all .png files in a nested directory structure.")
    p.add_argument("input_root", help="Root directory containing PNGs")
    p.add_argument("-o", "--output", default=None, help="Output root directory (default: <input>_watermarked)")
    p.add_argument("--inplace", action="store_true", help="Overwrite originals in place (use with care)")
    p.add_argument("--text", default=DEFAULT_TEXT, help="Watermark text")
    p.add_argument("--opacity", type=int, default=80, help="0-255 (default: 80)")
    p.add_argument("--angle", type=float, default=15, help="Rotation angle in degrees (default: -30)")
    p.add_argument("--font", default=None, help="Optional path to a .ttf font file")
    args = p.parse_args()

    input_root = os.path.abspath(args.input_root)
    output_root = os.path.abspath(args.output) if args.output else (input_root + "_watermarked")

    if args.inplace:
        output_root = input_root

    process_dir(
        input_root=input_root,
        output_root=output_root,
        inplace=args.inplace,
        text=args.text,
        opacity=max(0, min(255, args.opacity)),
        angle=args.angle,
        font_path=args.font
    )

if __name__ == "__main__":
    main()
