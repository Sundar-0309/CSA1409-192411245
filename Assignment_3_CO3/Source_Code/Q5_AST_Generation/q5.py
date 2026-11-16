from Source_Code.common.expression import Parser, Node

def assignment(text):
    name, expression = (part.strip() for part in text.split('=', 1))
    if not name.isidentifier(): raise ValueError('assignment target must be an identifier')
    return Node('=', Node('id', value=name), Parser(expression).parse())

def parse_tree_nodes(ast):
    # A concrete tree retains grammar-only nodes E, T and F; this conservative count illustrates their overhead.
    return ast.count() * 2 + 1
