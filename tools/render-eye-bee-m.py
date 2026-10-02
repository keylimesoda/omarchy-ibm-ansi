#!/usr/bin/env python3
"""Render the checked-in vector directly to a lossless 4K wallpaper.

Install CairoSVG 2.9.1 and Pillow 12.3.0 in a virtual environment first.
No downloads, raster upscaling, palette quantization, or JPEG encoding.
"""
from io import BytesIO
from pathlib import Path
import cairosvg
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / 'backgrounds/5-eye-bee-m-color.png'
svg = ROOT / 'artwork/eye-bee-m-color.svg'
render = cairosvg.svg2png(url=str(svg), output_width=3840, output_height=2160)
image = Image.open(BytesIO(render)).convert('RGB')
image.save(TARGET, optimize=True)
print(TARGET)
