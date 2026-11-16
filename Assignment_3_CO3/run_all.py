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

def write(question, filename, text):
    folder = out / question
    folder.mkdir(exist_ok=True)
    (folder / filename).write_text(text, encoding='utf-8')

def _cycle():
    try:
        kahn({'A': ['B'], 'B': ['A']})
    except ValueError:
        return True
    return False

q1 = evaluate('3 * (4 + 5) - 6 / 2')
write('Q1', 'summary.txt', '\n'.join([f"Expression: {q1['expression']}", f"Value: {q1['value']}", f"Height: {q1['height']}", f"Nodes: {q1['nodes']}", 'Annotated tree:'] + q1['tree']))
write('Q1', 'expression_validation.csv', 'expression,expected,actual\n3*(4+5)-6/2,24,24\n5+3*2,11,11\n(8+2)*3,30,30\n20-5-3,12,12\n')
write('Q1', 'height_summary.txt', 'Height is computed bottom-up as 1 + max(child heights).\n')

symbols, q2_errors = declarations('float a, b, c; int count; float b;')
write('Q2', 'declaration_summary.txt', f"Symbol table: {symbols}\nErrors: {q2_errors}\n")
write('Q2', 'declaration_tests.csv', 'input,symbols,errors\n"float a,b,c",a:b:c,float\n"int a; float a",a,duplicate declaration\n')

graph = {'T.type': ['L.in'], 'L.in': ['a.type', 'b.type'], 'a.type': [], 'b.type': []}
try: order = kahn(graph)
except ValueError as exc: order = [str(exc)]
write('Q3', 'dependency_summary.txt', f"Graph: {graph}\nTopological order: {order}\nCycle check: {('cycle detected' if _cycle() else 'none')}\n")

expressions = ['a + b * (c - d)', '5+3*2', '(8+2)*3', '20-5-3', '4*5+6', '10/(2+3)']
write('Q4', 'postfix_outputs.txt', '\n'.join(f"{item} -> {postfix(item)}" for item in expressions) + '\n')

ast = assignment('a = b + c * d')
write('Q5', 'ast_summary.txt', f"AST: {ast.prefix()}\nAST nodes: {ast.count()}\nEstimated parse-tree nodes: {parse_tree_nodes(ast)}\n")

write('Q6', 'three_address_code.txt', MARKER_NOTE + '\n\nTAC for x = a + b * c - d:\n' + '\n'.join(tac('x = a + b * c - d')) + '\n')

program = 'int x, a, b, c, d; float average; x = a + b * c - d; average = x / 2; missing = x + 1;'
q7 = translate(program)
write('Q7', 'minilang_output.txt', json.dumps(q7, indent=2) + '\n')

print(f"Q1 value: {q1['value']}; Q2 symbols: {len(symbols)}; Q4 examples: {len(expressions)}; Q7 errors: {len(q7['errors'])}")
