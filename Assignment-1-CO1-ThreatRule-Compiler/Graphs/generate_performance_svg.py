"""Create an SVG performance chart from measured CSV data; uses only the standard library."""
import csv
import sys
from pathlib import Path

source = Path(sys.argv[1] if len(sys.argv) > 1 else "../Performance_Analysis/results.csv")
target = Path(sys.argv[2] if len(sys.argv) > 2 else "performance.svg")
with source.open(newline="", encoding="utf-8") as handle:
    rows = [r for r in csv.DictReader(handle) if r.get("rules") and r.get("elapsed_milliseconds")]
if not rows:
    raise SystemExit("No measured rows found. Fill results.csv first.")
points = [(int(r["rules"]), float(r["elapsed_milliseconds"])) for r in rows]
width, height, left, bottom = 800, 420, 75, 55
plot_w, plot_h = width - left - 30, height - bottom - 35
max_x, max_y = max(x for x, _ in points), max(y for _, y in points)
def pos(x, y):
    return left + x / max_x * plot_w, height - bottom - y / max_y * plot_h
polyline = " ".join(f"{x:.1f},{y:.1f}" for x, y in (pos(x, y) for x, y in points))
labels = "".join(f'<text x="{pos(x, 0)[0]:.1f}" y="390" text-anchor="middle">{x}</text>' for x, _ in points)
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="800" height="420" viewBox="0 0 800 420">
<style>text{{font:14px Arial;fill:#222}} .axis{{stroke:#333}} .line{{fill:none;stroke:#1769aa;stroke-width:3}} .dot{{fill:#1769aa}}</style>
<text x="400" y="25" text-anchor="middle" font-weight="bold">ThreatRule Scanner Performance</text>
<line class="axis" x1="75" y1="20" x2="75" y2="365"/><line class="axis" x1="75" y1="365" x2="770" y2="365"/>
<text x="400" y="415" text-anchor="middle">Rules scanned</text><text x="18" y="210" transform="rotate(-90 18 210)" text-anchor="middle">Elapsed milliseconds</text>
<polyline class="line" points="{polyline}"/>{''.join(f'<circle class="dot" cx="{pos(x,y)[0]:.1f}" cy="{pos(x,y)[1]:.1f}" r="4"/>' for x,y in points)}{labels}
</svg>'''
target.write_text(svg, encoding="utf-8")
print(f"Wrote {target}")
