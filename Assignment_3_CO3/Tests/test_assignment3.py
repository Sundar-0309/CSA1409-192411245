import sys
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from Source_Code.Q1_Synthesized_Attributes.q1 import evaluate
from Source_Code.Q2_Inherited_Attributes.q2 import declarations
from Source_Code.Q3_Dependency_Graphs.q3 import kahn
from Source_Code.Q4_Syntax_Directed_Translation.q4 import postfix
from Source_Code.Q5_AST_Generation.q5 import assignment
from Source_Code.Q6_Advanced_Attributes.q6 import tac
from Source_Code.Q7_MiniLang_Translator.q7 import translate

class AssignmentThreeTests(unittest.TestCase):
    def test_q1_value_and_height(self):
        result = evaluate('3*(4+5)-6/2')
        self.assertEqual(result['value'], 24)
        self.assertGreater(result['height'], 1)
    def test_q2_duplicate(self):
        table, errors = declarations('float a,b; int a;')
        self.assertEqual(table['a'], 'float')
        self.assertTrue(errors)
    def test_q3_order_and_cycle(self):
        self.assertEqual(kahn({'a': ['b'], 'b': []}), ['a', 'b'])
        with self.assertRaises(ValueError): kahn({'a': ['b'], 'b': ['a']})
    def test_q4_postfix(self): self.assertEqual(postfix('a+b*(c-d)'), 'a b c d - * +')
    def test_q5_ast(self): self.assertEqual(assignment('a=b+c*d').prefix(), '(= a (+ b (* c d)))')
    def test_q6_tac(self): self.assertEqual(tac('x=a+b*c-d')[-1], 'x = t3')
    def test_q7_semantics(self):
        result = translate('int x, a; x = a + 1; y = x + 1;')
        self.assertEqual(result['symbols']['x'], 'int')
        self.assertTrue(any('undeclared identifier: y' in error for error in result['errors']))

if __name__ == '__main__': unittest.main()
