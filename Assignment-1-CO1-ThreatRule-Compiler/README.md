# ThreatRule Compiler Front End

This is an original Assignment 1 implementation for CSA1409 Compiler Design. It implements the lexical-analysis stage of a small, case-insensitive language for Security Operations Center (SOC) detection rules.

## Project contents

| Path | Purpose |
| --- | --- |
| `src/threatrule.l` | Flex/LEX specification and scanner implementation |
| `examples/` | Valid, invalid, and live-feed sample rules |
| `scripts/generate_rules.py` | Reproducible test-file generator |
| `scripts/run_tests.ps1` | Builds and runs all supplied tests |
| `REPORT.md` | Task-by-task design, evaluation, and defence |

## Rule example

```text
RULE ssh_attack IF src_ip == 10.0.0.5 AND port == 22 AND attempts > 5 THEN ALERT "SSH brute force";
```

## Build and run on Windows

Install Flex and GCC, then run the following from this directory:

```powershell
flex -o build/lex.yy.c src/threatrule.l
gcc -std=c11 -Wall -Wextra -O2 build/lex.yy.c -o build/threatrule.exe
./build/threatrule.exe examples/valid_rules.tr
```

For the complete reproducible test run:

```powershell
./scripts/run_tests.ps1
```

The scanner prints one token per line, installs identifiers in a small symbol table, reports recoverable lexical errors with line numbers, and returns a non-zero exit code if errors are found.

## Supported token classes

Keywords (`RULE`, `IF`, `THEN`, `ALERT`, `AND`, `OR`, `NOT`), identifiers, IPv4 addresses, integers, quoted strings, comparison operators, punctuation, SHA-256 hashes, CVE identifiers, and HTTP/HTTPS URLs are recognized. IP address octets and port values are range-checked in the action code.
