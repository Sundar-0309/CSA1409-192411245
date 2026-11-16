from Source_Code.common.expression import Parser, Node

def annotated(node: Node, indent=0):
    label = f"{node.tag} val={node.value}" if node.tag in '+-*/' else f"{node.tag}={node.value}"
    lines = ['  ' * indent + label]
    for child in (node.left, node.right):
        if isinstance(child, Node): lines.extend(annotated(child, indent + 1))
    return lines

def evaluate(text):
    tree = Parser(text).parse()
    return {'expression': text, 'value': tree.value, 'height': tree.height(), 'nodes': tree.count(), 'tree': annotated(tree)}
