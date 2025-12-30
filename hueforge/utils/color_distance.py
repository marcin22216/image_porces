from __future__ import annotations

from typing import Dict, Tuple

Rgb = Tuple[int, int, int]
Lab = Tuple[float, float, float]


def rgb_distance(a_rgb: Rgb, b_rgb: Rgb) -> float:
    return float(sum((int(x) - int(y)) ** 2 for x, y in zip(a_rgb, b_rgb)))


def lab_distance(a_lab: Lab, b_lab: Lab) -> float:
    return float(sum((float(x) - float(y)) ** 2 for x, y in zip(a_lab, b_lab)))


def color_distance(a: Dict[str, object], b: Dict[str, object]) -> float:
    a_lab = _extract_lab(a)
    b_lab = _extract_lab(b)
    if a_lab and b_lab:
        return lab_distance(a_lab, b_lab)
    if a_lab and not b_lab:
        b_lab = rgb_to_lab(_extract_rgb(b))
        return lab_distance(a_lab, b_lab)
    if b_lab and not a_lab:
        a_lab = rgb_to_lab(_extract_rgb(a))
        return lab_distance(a_lab, b_lab)
    return rgb_distance(_extract_rgb(a), _extract_rgb(b))


def rgb_to_lab(rgb: Rgb) -> Lab:
    r, g, b = [c / 255.0 for c in rgb]
    r = _srgb_to_linear(r)
    g = _srgb_to_linear(g)
    b = _srgb_to_linear(b)

    x = r * 0.4124 + g * 0.3576 + b * 0.1805
    y = r * 0.2126 + g * 0.7152 + b * 0.0722
    z = r * 0.0193 + g * 0.1192 + b * 0.9505

    x /= 0.95047
    y /= 1.00000
    z /= 1.08883

    x = _lab_f(x)
    y = _lab_f(y)
    z = _lab_f(z)

    l = 116.0 * y - 16.0
    a = 500.0 * (x - y)
    b_val = 200.0 * (y - z)
    return (l, a, b_val)


def _extract_rgb(item: Dict[str, object]) -> Rgb:
    rgb = item.get("rgb")
    if not rgb:
        return (0, 0, 0)
    return (int(rgb[0]), int(rgb[1]), int(rgb[2]))


def _extract_lab(item: Dict[str, object]) -> Lab | None:
    lab = item.get("lab")
    if not lab:
        return None
    return (float(lab[0]), float(lab[1]), float(lab[2]))


def _srgb_to_linear(value: float) -> float:
    if value <= 0.04045:
        return value / 12.92
    return ((value + 0.055) / 1.055) ** 2.4


def _lab_f(value: float) -> float:
    if value > 0.008856:
        return value ** (1.0 / 3.0)
    return (7.787 * value) + (16.0 / 116.0)
