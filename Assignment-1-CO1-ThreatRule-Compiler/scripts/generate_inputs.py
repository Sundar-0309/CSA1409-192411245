"""Generate deterministic large ThreatRule input files for performance testing."""
from pathlib import Path

root = Path(__file__).resolve().parents[1]
output = root / "Input_Files"
output.mkdir(exist_ok=True)
for count in (100, 1_000, 10_000, 100_000):
    path = output / f"rules_{count}.tr"
    with path.open("w", encoding="utf-8") as handle:
        for number in range(count):
            address = f"10.{(number >> 16) & 255}.{(number >> 8) & 255}.{number & 255}"
            handle.write(
                f'RULE generated_{number} IF src_ip == {address} AND port == 443 '
                f'AND attempts > 3 THEN ALERT "generated rule {number}";\n'
            )
    print(f"wrote {path.name}")
