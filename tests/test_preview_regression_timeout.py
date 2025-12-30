from pathlib import Path
import multiprocessing as mp
import tempfile
import traceback

from src.app.preview_runner import run_preview


def _run_preview_worker(pix_path, queue):
    try:
        import faulthandler
        import signal

        faulthandler.enable()
        faulthandler.register(signal.SIGUSR1, all_threads=True)
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_root = Path(tmp_dir)
            input_path = tmp_root / "input.png"
            input_path.write_bytes(Path(pix_path).read_bytes())
            debug_dir = tmp_root / "debug"
            debug_dir.mkdir()
            run_preview(
                str(input_path),
                debug_dir=str(debug_dir),
                allowed_filaments=None,
                overrides={},
            )
            preview_path = debug_dir / "preview.png"
            if not preview_path.exists() or preview_path.stat().st_size == 0:
                raise RuntimeError("preview.png missing or empty")
        queue.put(("ok", None))
    except Exception:
        queue.put(("err", traceback.format_exc()))


def test_run_preview_timeout_guard():
    pix_path = Path(__file__).resolve().parents[1] / "pix1.png"
    if not pix_path.exists():
        raise AssertionError("pix1.png fixture missing at repo root")
    ctx = mp.get_context("spawn")
    queue = ctx.Queue()
    process = ctx.Process(target=_run_preview_worker, args=(str(pix_path), queue))
    process.start()
    process.join(timeout=30)
    if process.is_alive():
        import os
        import signal
        import time

        os.kill(process.pid, signal.SIGUSR1)
        time.sleep(0.5)
        process.terminate()
        process.join(timeout=5)
        raise AssertionError(
            "run_preview hung (timeout=30s) on pix1.png (stacktrace dumped above)"
        )
    try:
        status, payload = queue.get(timeout=1)
    except Exception as exc:
        raise AssertionError("run_preview worker finished without result") from exc
    if status != "ok":
        raise AssertionError(payload)
