import subprocess
import sys
from pathlib import Path


def test_cli_version_flag():
    repo_root = Path(__file__).resolve().parents[1]
    result = subprocess.run(
        [sys.executable, "-m", "src.app.main", "--version"],
        cwd=repo_root,
        capture_output=True,
        text=True,
        check=True,
    )

    assert "1.0.0" in result.stdout
