"""Prepare the profile avatar as a high-contrast grayscale image for ASCII rendering."""
import os
import sys

from PIL import Image, ImageEnhance, ImageOps

HERE = os.path.dirname(os.path.abspath(__file__))
INP = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "source-photo.png")
OUT = sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, "..", "source-prepped.png")

image = Image.open(INP).convert("RGB")
image = ImageOps.fit(image, (512, 512), method=Image.Resampling.LANCZOS)
image = ImageOps.grayscale(image)
image = ImageOps.autocontrast(image, cutoff=1)
image = ImageEnhance.Contrast(image).enhance(1.25)
image.save(OUT, optimize=True)
print("wrote", OUT, image.size)
