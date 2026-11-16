# Assignment 3 report

## Q1 Synthesized attributes

For `E -> E1 + T`, the rule is `E.val = E1.val + T.val`; multiplication, subtraction, and division are analogous. The implementation computes values after both children are available, so the definition is S-attributed and a post-order traversal is valid. The height attribute follows `height(node) = 1 + max(height(children))`.

## Q2 Inherited declarations

In `D -> T L`, `T.type` is synthesized by `T -> int | float`, while `L.in = T.type` is inherited because the type must travel from the declaration context to each identifier. The declaration module installs each identifier with this type and reports duplicate entries.

## Q3 Dependency graphs

Graph edges run from prerequisite attributes to dependent attributes. Kahn's algorithm evaluates zero-indegree nodes first. If nodes remain after the ready queue is exhausted, the graph contains a cycle and the SDD is ill-defined. Q1 is S-attributed; Q2 is L-attributed because each inherited attribute comes from the parent or a left sibling.

## Q4 SDT and postfix

An SDD specifies semantic rules; an SDT embeds their actions in grammar productions. Postfix output emits an operator after its operands. For `a + b * (c - d)`, the correct sequence is `a b c d - * +`.

## Q5 AST construction

The AST keeps operators and operands but removes grammar-only E, T, F, parentheses, and punctuation nodes. Thus its node count is lower than the concrete parse tree. In a top-down grammar, an inherited accumulator can carry the left subtree through an eliminated-recursion suffix.

## Q6 Advanced evaluation

An LR parser cannot directly evaluate an inherited attribute until required context is on its stack. An empty marker production can execute at that point without changing the language. The TAC generator assigns temporaries bottom-up: `t1 = b * c`, `t2 = a + t1`, `t3 = t2 - d`, `x = t3`.

## Q7 MiniLang design

MiniLang supports typed declarations and arithmetic assignments. Its translator uses a symbol table to catch duplicates and undeclared identifiers, reuses the expression AST, and emits TAC. Future work can add block scope, relational operators, and structured `if`/`while` parsing while retaining the same attribute-flow principles.
