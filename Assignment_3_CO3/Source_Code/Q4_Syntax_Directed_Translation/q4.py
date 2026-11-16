import re

PRECEDENCE = {'+': 1, '-': 1, '*': 2, '/': 2}
def postfix(text):
    output, stack = [], []
    for token in re.findall(r'[A-Za-z_]\w*|\d+|[()+*/-]', text):
        if re.match(r'[A-Za-z_\d]', token): output.append(token)
        elif token == '(': stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(': output.append(stack.pop())
            if not stack: raise ValueError('unmatched closing parenthesis')
            stack.pop()
        else:
            while stack and stack[-1] != '(' and PRECEDENCE[stack[-1]] >= PRECEDENCE[token]: output.append(stack.pop())
            stack.append(token)
    while stack:
        if stack[-1] == '(': raise ValueError('unmatched opening parenthesis')
        output.append(stack.pop())
    return ' '.join(output)
