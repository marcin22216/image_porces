from __future__ import annotations

import json
import tempfile
from pathlib import Path
from typing import Optional

from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from fastapi.responses import HTMLResponse, Response
from fastapi.staticfiles import StaticFiles

from src.app.bundle_runner import run_bundle
from src.app.cli_overrides import parse_id_list, validate_overrides
from src.app.preview_runner import run_preview

FILE_SIZE_LIMIT = 20 * 1024 * 1024

app = FastAPI(title="Image-to-3D CLI wrapper")
STATIC_DIR = Path(__file__).resolve().parent / "static"
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.get("/ui", response_class=HTMLResponse)
def ui() -> HTMLResponse:
    index_path = STATIC_DIR / "index.html"
    return HTMLResponse(index_path.read_text(encoding="utf-8"))


@app.post("/preview")
def preview(
    file: UploadFile = File(...),
    catalog: Optional[str] = Form(None),
    n_colors: Optional[int] = Form(None),
    blend_depth: Optional[float] = Form(None),
    sequence_mode: Optional[str] = Form(None),
    allowed_filaments: Optional[str] = Form(None),
    base_filament_id: Optional[str] = Form(None),
    layer_sequence_ids: Optional[str] = Form(None),
) -> Response:
    if file is None:
        raise HTTPException(status_code=400, detail="missing file")
    content = _read_upload(file)
    overrides, allowed = _build_overrides(
        catalog=catalog,
        n_colors=n_colors,
        blend_depth=blend_depth,
        sequence_mode=sequence_mode,
        base_filament_id=base_filament_id,
        layer_sequence_ids=layer_sequence_ids,
        allowed_filaments=allowed_filaments,
    )

    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        input_path = temp_path / "input.png"
        input_path.write_bytes(content)
        debug_dir = temp_path / "debug"
        debug_dir.mkdir(parents=True, exist_ok=True)
        try:
            run_preview(
                str(input_path),
                debug_dir=str(debug_dir),
                allowed_filaments=allowed,
                overrides=overrides,
            )
        except ValueError as exc:
            raise HTTPException(status_code=400, detail=str(exc)) from exc
        preview_path = debug_dir / "preview.png"
        return Response(preview_path.read_bytes(), media_type="image/png")


@app.post("/bundle")
def bundle(
    file: UploadFile = File(...),
    catalog: Optional[str] = Form(None),
    n_colors: Optional[int] = Form(None),
    blend_depth: Optional[float] = Form(None),
    sequence_mode: Optional[str] = Form(None),
    allowed_filaments: Optional[str] = Form(None),
    base_filament_id: Optional[str] = Form(None),
    layer_sequence_ids: Optional[str] = Form(None),
) -> Response:
    if file is None:
        raise HTTPException(status_code=400, detail="missing file")
    content = _read_upload(file)
    overrides, allowed = _build_overrides(
        catalog=catalog,
        n_colors=n_colors,
        blend_depth=blend_depth,
        sequence_mode=sequence_mode,
        base_filament_id=base_filament_id,
        layer_sequence_ids=layer_sequence_ids,
        allowed_filaments=allowed_filaments,
    )

    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        input_path = temp_path / "input.png"
        input_path.write_bytes(content)
        output_zip = temp_path / "bundle.zip"
        try:
            run_bundle(
                str(input_path),
                str(output_zip),
                allowed_filaments=allowed,
                overrides=overrides,
            )
        except ValueError as exc:
            raise HTTPException(status_code=400, detail=str(exc)) from exc
        data = output_zip.read_bytes()
        headers = {"Content-Disposition": "attachment; filename=bundle.zip"}
        return Response(data, media_type="application/zip", headers=headers)


def _read_upload(file: UploadFile) -> bytes:
    data = file.file.read(FILE_SIZE_LIMIT + 1)
    if len(data) > FILE_SIZE_LIMIT:
        raise HTTPException(status_code=400, detail="file too large (limit 20MB)")
    return data


def _build_overrides(
    *,
    catalog: Optional[str],
    n_colors: Optional[int],
    blend_depth: Optional[float],
    sequence_mode: Optional[str],
    allowed_filaments: Optional[str],
    base_filament_id: Optional[str],
    layer_sequence_ids: Optional[str],
) -> tuple[dict, Optional[list]]:
    overrides: dict = {}
    if catalog:
        overrides.setdefault("print", {})["filament_catalog"] = catalog
    elif Path("data/filament_catalog_filamentcolors.json").exists():
        overrides.setdefault("print", {})["filament_catalog"] = "data/filament_catalog_filamentcolors.json"
    if n_colors is not None:
        overrides.setdefault("palette", {})["n_colors"] = int(n_colors)
    if blend_depth is not None:
        overrides.setdefault("print", {})["blend_depth"] = float(blend_depth)
    if sequence_mode is not None:
        overrides.setdefault("print", {})["sequence_mode"] = sequence_mode
    if base_filament_id:
        overrides.setdefault("print", {})["base_filament_id"] = base_filament_id
    if layer_sequence_ids is not None:
        overrides.setdefault("print", {})["layer_sequence_ids"] = parse_id_list(layer_sequence_ids)
    try:
        validate_overrides(overrides)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    allowed = parse_id_list(allowed_filaments)
    return overrides, allowed


def main() -> None:
    import uvicorn

    uvicorn.run("src.web.server:app", host="0.0.0.0", port=8000, reload=False)


if __name__ == "__main__":
    main()
