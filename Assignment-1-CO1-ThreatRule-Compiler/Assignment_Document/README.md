# Assignment document and submission guide

## Problem addressed

ThreatRule is a small domain-specific language used to describe security detections exchanged between branch Security Operations Centers and a central SOC. The project implements the lexical-analysis stage using Flex.

## Submission evidence

The implementation evidence is organised by purpose. `src/threatrule.l` is the canonical source. `Input_Files` provides representative valid, invalid, and live-feed inputs. `Output_Files` specifies the observable scanner behaviour. `Diagrams` explains the compiler design. `Performance_Analysis` supplies the reproducible measurement process. `Test_Cases` records pass conditions.

## Build evidence

Run `scripts/run_tests.ps1` from the project root on a system with working Flex and GCC. It generates `build/lex.yy.c`, compiles the scanner, tests fixed inputs, and generates data sets containing 100 through 100,000 rules.
