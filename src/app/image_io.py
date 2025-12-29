from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Tuple, Union

from PIL import Image

Pixel = Tuple[int, int, int]
PathLike = Union[str, Path]


@dataclass(frozen=True)
class ImageData:
    width: int
    height: int
    pixels: Tuple[Pixel, ...]

    def at(self, x: int, y: int) -> Pixel:
        return self.pixels[y * self.width + x]


def load_image(path: PathLike) -> ImageData:
    with Image.open(path) as image:
        rgb = image.convert("RGB")
        width, height = rgb.size
        pixels = tuple(rgb.getdata())
    return ImageData(width=width, height=height, pixels=pixels)


def save_image(image: ImageData, path: PathLike) -> None:
    expected = image.width * image.height
    if len(image.pixels) != expected:
        raise ValueError("pixel data length does not match width*height")
    out = Image.new("RGB", (image.width, image.height))
    out.putdata(image.pixels)
    out.save(path)
