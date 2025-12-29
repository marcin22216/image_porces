from src.app.image_io import ImageData, load_image, save_image


def test_round_trip_png(tmp_path):
    pixels = (
        (255, 0, 0),
        (0, 255, 0),
        (0, 0, 255),
        (255, 255, 0),
    )
    image = ImageData(width=2, height=2, pixels=pixels)
    path = tmp_path / "sample.png"

    save_image(image, path)
    loaded = load_image(path)

    assert loaded.width == 2
    assert loaded.height == 2
    assert loaded.pixels == pixels
