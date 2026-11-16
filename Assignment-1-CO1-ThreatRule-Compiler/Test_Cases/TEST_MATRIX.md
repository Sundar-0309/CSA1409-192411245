# Test matrix

| ID | Input | Expected result | Pass condition |
| --- | --- | --- | --- |
| T01 | `Input_Files/valid_rules.tr` | Valid keyword, identifier, IP, string, and operator tokens | Exit 0; summary has 0 errors |
| T02 | `Input_Files/invalid_rules.tr` | Three diagnostics and recovery | Exit non-zero; all three error classes reported |
| T03 | `Input_Files/live_feed_rules.tr` | SHA-256, CVE, and URL each form one token | Exit 0; summary has 0 errors |
| T04 | Generated 100 rules | Linear scan baseline | Exit 0; record real time |
| T05 | Generated 1,000 rules | Medium scale scan | Exit 0; record real time |
| T06 | Generated 10,000 rules | Large scale scan | Exit 0; record real time |
| T07 | Generated 100,000 rules | Stress scan | Exit 0; record real time |

Run all rows through `scripts/run_tests.ps1`. The script treats a clean invalid-input run as a failure because valid error reporting must produce a non-zero exit status.
