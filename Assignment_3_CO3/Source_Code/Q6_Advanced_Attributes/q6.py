from Source_Code.common.expression import Node
from Source_Code.Q5_AST_Generation.q5 import assignment

def tac(text):
    root = assignment(text); lines = []; serial = 0
    def visit(node):
        nonlocal serial
        if node.tag in ('number', 'id'): return str(node.value)
        left, right = visit(node.left), visit(node.right)
        if node.tag == '=': lines.append(f"{left} = {right}"); return left
        serial += 1; temp = f"t{serial}"; lines.append(f"{temp} = {left} {node.tag} {right}"); return temp
    visit(root); return lines

MARKER_NOTE = 'A marker nonterminal has an empty production and executes an action without consuming input; it preserves the accepted language.'
