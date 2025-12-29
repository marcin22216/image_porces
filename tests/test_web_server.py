import io
import zipfile
from pathlib import Path

from fastapi.testclient import TestClient
from PIL import Image

from src.web.server import app


def _make_image_bytes() -> bytes:
    image = Image.new("RGB", (16, 16), (120, 120, 120))
    buf = io.BytesIO()
    image.save(buf, format="PNG")
    return buf.getvalue()


def _write_catalog(tmp_path: Path) -> Path:
    catalog = tmp_path / "catalog.json"
    catalog.write_text(
        '{"filaments":[{"id":"white","name":"White","rgb":[255,255,255],"td_mm":1.0},{"id":"black","name":"Black","rgb":[0,0,0],"td_mm":1.0}]}',
        encoding="utf-8",
    )
    return catalog


def test_health():
    client = TestClient(app)
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_preview_endpoint(tmp_path):
    client = TestClient(app)
    catalog = _write_catalog(tmp_path)
    response = client.post(
        "/preview",
        files={"file": ("input.png", _make_image_bytes(), "image/png")},
        data={"catalog": str(catalog)},
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"


def test_bundle_endpoint(tmp_path):
    client = TestClient(app)
    catalog = _write_catalog(tmp_path)
    response = client.post(
        "/bundle",
        files={"file": ("input.png", _make_image_bytes(), "image/png")},
        data={"catalog": str(catalog)},
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/zip"

    buf = io.BytesIO(response.content)
    with zipfile.ZipFile(buf, "r") as archive:
        names = set(archive.namelist())
    assert any(name.endswith(".stl") for name in names)
    assert any(name.endswith(".colorplan.txt") for name in names)
    assert "preview.png" in names
    assert "config.effective.json" in names
