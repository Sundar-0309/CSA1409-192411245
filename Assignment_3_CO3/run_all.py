"""Run every Assignment 3 demonstration and write evidence files."""
from pathlib import Path
import json
from Source_Code.Q1_Synthesized_Attributes.q1 import evaluate
from Source_Code.Q2_Inherited_Attributes.q2 import declarations
from Source_Code.Q3_Dependency_Graphs.q3 import kahn
from Source_Code.Q4_Syntax_Directed_Translation.q4 import postfix
from Source_Code.Q5_AST_Generation.q5 import assignment, parse_tree_nodes
from Source_Code.Q6_Advanced_Attributes.q6 import tac, MARKER_NOTE
from Source_Code.Q7_MiniLang_Translator.q7 import translate

root = Path(__file__).resolve().parent
out = root / "Output_Files"
out.mkdir(exist_ok=True)

def _cycle():
    try:
        kahn({'A': ['B'], 'B': ['A']})
    except ValueError:
        return True
    return False

q1 = evaluate('3 * (4 + 5) - 6 / 2')
(out / 'Q1_synthesized.txt').write_text('\n'.join([f"Expression: {q1['expression']}", f"Value: {q1['value']}", f"Height: {q1['height']}", f"Nodes: {q1['nodes']}", 'Annotated tree:'] + q1['tree']), encoding='utf-8')

symbols, q2_errors = declarations('float a, b, c; int count; float b;')
(out / 'Q2_declarations.txt').write_text(f"Symbol table: {symbols}\nErrors: {q2_errors}\n", encoding='utf-8')

graph = {'T.type': ['L.in'], 'L.in': ['a.type', 'b.type'], 'a.type': [], 'b.type': []}
try: order = kahn(graph)
except ValueError as exc: order = [str(exc)]
(out / 'Q3_dependency.txt').write_text(f"Graph: {graph}\nTopological order: {order}\nCycle check: {('cycle detected' if _cycle() else 'none')}\n", encoding='utf-8')

expressions = ['a + b * (c - d)', '5+3*2', '(8+2)*3', '20-5-3', '4*5+6', '10/(2+3)']
(out / 'Q4_postfix.txt').write_text('\n'.join(f"{item} -> {postfix(item)}" for item in expressions) + '\n', encoding='utf-8')

ast = assignment('a = b + c * d')
(out / 'Q5_ast.txt').write_text(f"AST: {ast.prefix()}\nAST nodes: {ast.count()}\nEstimated parse-tree nodes: {parse_tree_nodes(ast)}\n", encoding='utf-8')

(out / 'Q6_tac.txt').write_text(MARKER_NOTE + '\n\nTAC for x = a + b * c - d:\n' + '\n'.join(tac('x = a + b * c - d')) + '\n', encoding='utf-8')

program = 'int x, a, b, c, d; float average; x = a + b * c - d; average = x / 2; missing = x + 1;'
q7 = translate(program)
(out / 'Q7_minilang.json').write_text(json.dumps(q7, indent=2), encoding='utf-8')

print(f"Q1 value: {q1['value']}; Q2 symbols: {len(symbols)}; Q4 examples: {len(expressions)}; Q7 errors: {len(q7['errors'])}")
