import re
from Source_Code.Q2_Inherited_Attributes.q2 import declarations
from Source_Code.Q6_Advanced_Attributes.q6 import tac

def translate(program):
    symbols, errors, code, asts = {}, [], [], []
    statements = [part.strip() for part in program.split(';') if part.strip()]
    for statement in statements:
        if re.match(r'^(int|float)\b', statement):
            table, found = declarations(statement + ';')
            for name, typ in table.items():
                if name in symbols: errors.append(f'duplicate declaration: {name}')
                else: symbols[name] = typ
            errors.extend(found); continue
        if '=' not in statement:
            errors.append(f'unsupported statement: {statement}'); continue
        target, expression = (part.strip() for part in statement.split('=', 1))
        if target not in symbols: errors.append(f'undeclared identifier: {target}'); continue
        for name in re.findall(r'\b[A-Za-z_]\w*\b', expression):
            if name not in symbols: errors.append(f'undeclared identifier: {name}')
        try:
            generated = tac(statement); code.extend(generated); asts.append(statement)
        except ValueError as exc: errors.append(str(exc))
    return {'symbols': symbols, 'errors': errors, 'tac': code, 'asts': asts}
