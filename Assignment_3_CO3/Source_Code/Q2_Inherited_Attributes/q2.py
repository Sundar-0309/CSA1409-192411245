import re

def declarations(text):
    table, errors = {}, []
    for statement in filter(None, (part.strip() for part in text.split(';'))):
        match = re.fullmatch(r'(int|float)\s+([A-Za-z_]\w*(?:\s*,\s*[A-Za-z_]\w*)*)', statement)
        if not match:
            errors.append(f"invalid declaration: {statement}"); continue
        typ, names = match.groups()
        for name in re.split(r'\s*,\s*', names):
            if name in table: errors.append(f"duplicate declaration: {name}")
            else: table[name] = typ
    return table, errors
