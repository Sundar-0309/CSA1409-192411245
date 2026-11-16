"""Run scanner regression tests and preserve an explicit pass/fail result."""
from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
scanner = Path(sys.argv[1]) if len(sys.argv) > 1 else root / "build" / "threatrule"
tests = [
    ("valid", "Input_Files/valid_rules.tr", True),
    ("boundary", "Input_Files/boundary_cases.tr", True),
    ("live feed", "Input_Files/hash_cve_url_feed.tr", True),
    ("invalid", "Input_Files/invalid_rules.tr", False),
]
if not scanner.exists():
    raise SystemExit(f"Scanner not found: {scanner}. Build it first.")
failed = 0
for name, relative, should_pass in tests:
    completed = subprocess.run([str(scanner), str(root / relative)], text=True, capture_output=True)
    passed = (completed.returncode == 0) == should_pass
    print(f"{name}: {'PASS' if passed else 'FAIL'}")
    if completed.stdout:
        print(completed.stdout)
    if completed.stderr:
        print(completed.stderr, file=sys.stderr)
    failed += not passed
raise SystemExit(1 if failed else 0)
