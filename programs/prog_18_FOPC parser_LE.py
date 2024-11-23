import re

def parse_fopc(expression):
    pattern = r"\b(All|Some|Exists|Not|And|Or|Implies|Equals)\b"
    tokens = re.findall(pattern, expression)
    return tokens

# Input logical expression
expression = "All x (Exists y (Loves(x, y)) Implies Loves(y, x))"
tokens = parse_fopc(expression)

print(f"Parsed tokens: {tokens}")
