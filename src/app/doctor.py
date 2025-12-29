from pathlib import Path

def run_doctor():
    print("=== PROJECT DOCTOR ===")
    for f in ["CODEX_RULES.md", "ROADMAP.md", "REPORT.md"]:
        print(f, "OK" if Path(f).exists() else "MISSING")
