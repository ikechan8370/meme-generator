from pathlib import Path
from typing import List

from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.utils import make_jpg_or_gif

img_dir = Path(__file__).parent / "images"


def need(images: List[BuildImage], texts, args):
    frame = BuildImage.open(img_dir / "out.png")

    def make(img: BuildImage) -> BuildImage:
        img = img.convert("RGBA")
        out = frame.copy().resize_width(int(img.width * 0.5), keep_ratio=True)
        return img.paste(out, (min(img.width - out.width - 20, int(img.width * 0.4)), min(img.height - out.height - 20, int(img.height * 0.7))), alpha=True)

    return make_jpg_or_gif(images[0], make)


add_meme("out", need, min_images=1, max_images=1, keywords=["out"])
