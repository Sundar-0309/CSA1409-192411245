# Source code inventory

| File | Function |
| --- | --- |
| `../src/threatrule.l` | Canonical Flex specification, actions, error recovery, symbol table, and driver |
| `../scripts/generate_rules.py` | Deterministic performance-input generator |
| `../scripts/run_tests.ps1` | Build and regression-test automation |
| `../Graphs/generate_performance_svg.py` | Chart generator for measured results |

The scanner is kept in one canonical location to prevent two copies from drifting apart.
