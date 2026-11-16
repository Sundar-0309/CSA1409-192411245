"""Generate deterministic ThreatRule test data."""
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("count", type=int)
parser.add_argument("output")
args = parser.parse_args()

with open(args.output, "w", encoding="utf-8") as out:
    for i in range(args.count):
        ip = f"10.{(i // 65536) % 256}.{(i // 256) % 256}.{i % 256}"
        out.write(
            f'RULE event_{i} IF src_ip == {ip} AND port == 443 AND attempts > 3 '
            f'THEN ALERT "generated event {i}";\n'
        )
