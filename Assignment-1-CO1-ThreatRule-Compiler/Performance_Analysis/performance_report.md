# Performance report

The benchmark input generator creates 100, 1,000, 10,000, and 100,000-rule files. Record a measured elapsed time, token count, error count, execution environment, and date in `results.csv` after running the scanner. The repository intentionally contains no invented timing values.

Interpret the result by comparing input-size growth with elapsed-time growth. Because Flex emits a deterministic finite automaton, ordinary valid inputs should exhibit approximately linear scanning cost with input length.
