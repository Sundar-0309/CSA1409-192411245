"""Expression parser shared by Q1, Q4, Q5, Q6 and Q7."""
from dataclasses import dataclass
import re

TOKENS = re.compile(r"\s*(?:(\d+)|([A-Za-z_]\w*)|(.))")

@dataclass
class Node:
    tag: str
    left: object = None
    right: object = None
    value: object = None
    def height(self):
        return 1 + max(self.left.height() if isinstance(self.left, Node) else 0,
                       self.right.height() if isinstance(self.right, Node) else 0)
    def count(self):
        return 1 + sum(child.count() for child in (self.left, self.right) if isinstance(child, Node))
    def prefix(self):
        if self.tag in '+-*/=': return f"({self.tag} {self.left.prefix()} {self.right.prefix()})"
        return str(self.value)

class Parser:
    def __init__(self, text, values=None):
        parts = [part for part in TOKENS.findall(text) if any(part)]
        self.tokens = [next(x for x in part if x) for part in parts] + ['EOF']
        self.i, self.values = 0, values or {}
    def peek(self): return self.tokens[self.i]
    def take(self):
        token = self.peek(); self.i += 1; return token
    def parse(self):
        node = self.expr()
        if self.peek() != 'EOF': raise ValueError(f"unexpected token {self.peek()}")
        return node
    def expr(self):
        node = self.term()
        while self.peek() in ('+', '-'):
            op = self.take(); right = self.term(); node = Node(op, node, right, self.eval(op, node, right))
        return node
    def term(self):
        node = self.factor()
        while self.peek() in ('*', '/'):
            op = self.take(); right = self.factor(); node = Node(op, node, right, self.eval(op, node, right))
        return node
    def factor(self):
        token = self.take()
        if token == '(':
            node = self.expr()
            if self.take() != ')': raise ValueError('missing closing parenthesis')
            return node
        if token.isdigit(): return Node('number', value=int(token))
        if re.match(r'^[A-Za-z_]', token): return Node('id', value=token)
        raise ValueError(f"expected factor, received {token}")
    def eval(self, op, left, right):
        if not isinstance(left.value, (int, float)) or not isinstance(right.value, (int, float)): return None
        return {'+': left.value + right.value, '-': left.value - right.value,
                '*': left.value * right.value, '/': left.value // right.value}[op]
