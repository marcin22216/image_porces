import numpy as np

from ops.scale_to_canvas import scale_image_to_canvas


def test_scale_width_only_preserves_aspect():
    image = np.zeros((4, 8, 3), dtype=np.uint8)

    scaled, mm_per_pixel = scale_image_to_canvas(image, target_width_mm=80.0, target_height_mm=None)

    assert scaled.shape == image.shape
    assert scaled.dtype == np.uint8
    assert mm_per_pixel == 10.0


def test_scale_height_only_preserves_aspect():
    image = np.zeros((10, 5, 3), dtype=np.uint8)

    scaled, mm_per_pixel = scale_image_to_canvas(image, target_width_mm=None, target_height_mm=50.0)

    assert scaled.shape == image.shape
    assert scaled.dtype == np.uint8
    assert mm_per_pixel == 5.0


def test_scale_both_dimensions_contain_mm_per_pixel():
    image = np.zeros((10, 20, 3), dtype=np.uint8)

    scaled, mm_per_pixel = scale_image_to_canvas(
        image, target_width_mm=30.0, target_height_mm=10.0
    )

    assert scaled.shape == image.shape
    assert scaled.dtype == np.uint8
    assert mm_per_pixel == 1.0
