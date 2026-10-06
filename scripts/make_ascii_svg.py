import sys
from html import escape
from pathlib import Path

from PIL import Image, ImageOps

SRC = sys.argv[1] if len(sys.argv) > 1 else "img/image.png"
COLS, CW, LH = 80, 4.6, 8.4  # glyph grid; CW/LH = monospace cell size
RAMP = " .`:-=+*cs#%@"  # light to dark; the white wall maps to space
# ponytail: no rembg/CLAHE, the photo's wall is already plain, autocontrast is enough. Add rembg for busy backgrounds.
img = ImageOps.autocontrast(ImageOps.grayscale(Image.open(SRC)), cutoff=2)
rows = round(COLS * img.height / img.width * CW / LH)
img = img.resize((COLS, rows), Image.LANCZOS)
tone = lambda p: (
    min(max((p / 255 - 0.2) / 0.62, 0), 1) ** 1.1
)  # push the wall to pure white, keep face tones
text = [
    "".join(
        RAMP[int((1 - tone(img.getpixel((x, y)))) * (len(RAMP) - 1))]
        for x in range(COLS)
    ).rstrip()
    for y in range(rows)
]
W, H = round(COLS * CW), round(rows * LH)
body = "".join(
    f'<text class="r" x="0" y="{(i + 1) * LH:.1f}" textLength="{len(t) * CW:.1f}" xml:space="preserve" '
    f'style="animation-delay:{i * 45}ms">{escape(t)}</text>'
    for i, t in enumerate(text)
    if t
)
Path("img/avi-ascii.svg").write_text(
    f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="monospace" font-size="{LH * 0.9:.1f}" fill="#c9d1d9">
<style>.r{{white-space:pre;clip-path:inset(0 100% 0 0);animation:w .9s steps(24) forwards}}@keyframes w{{to{{clip-path:inset(0)}}}}@media (prefers-reduced-motion:reduce){{.r{{animation:none;clip-path:none}}}}</style>
<rect width="100%" height="100%" rx="8" fill="#0d1117"/>
{body}
</svg>"""
)
print(W, H)
