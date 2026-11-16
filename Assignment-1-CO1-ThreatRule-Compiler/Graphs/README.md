# Graphs

After recording real measurements in `../Performance_Analysis/results.csv`, create an SVG chart:

```powershell
python generate_performance_svg.py ../Performance_Analysis/results.csv performance.svg
```

The generator refuses to create a chart with missing measurements, so the repository never presents invented performance evidence.
