# Performance analysis

Run `scripts/run_tests.ps1` on the assessment computer. Record each reported elapsed time in `results.csv` together with the operating system, processor, and date. Do not invent timing values: measurements vary by computer.

Test sizes are 100, 1,000, 10,000, and 100,000 syntactically valid rules. The expected error count is zero. The scanner is a Flex DFA, so its time should grow approximately linearly with the amount of input. Use `../Graphs/generate_performance_svg.py` after filling the CSV to produce a chart.
