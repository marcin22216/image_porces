# CODEX OPERATING RULES (MUST FOLLOW)

This file defines NON-NEGOTIABLE rules for this project.
If these rules are violated, the work is considered invalid.

## CORE PRINCIPLES
1. ONE CHANGE PER ITERATION
2. TESTS ARE MANDATORY
3. NO LOGIC IN GUI
4. PURE OPERATIONS
5. STABLE DATA CONTRACTS
6. REPORT EVERY ITERATION
7. IF ITERATION IS DONE AND TESTS PASS, UPDATE ROADMAP CHECKBOX IN THE SAME ITERATION (NO EXCEPTIONS)

## ITERATION RITUAL
Follow the 7-step ritual described in this file at all times.

## STARTUP RITUAL
Read CODEX_RULES.md, REPORT.md, ROADMAP.md, then run:
python -m src.app.main doctor

Nie używaj python -m ... bez jawnej wersji. Zawsze python3 -m ....

Canonical commands:

python3 -m src.app.main doctor

python3 -m pytest -q
