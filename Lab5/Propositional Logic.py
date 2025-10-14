from itertools import product

def evaluate(expr, model):
    if isinstance(expr, str):
        return model[expr]
    op = expr[0]
    if op == 'not':
        return not evaluate(expr[1], model)
    elif op == 'and':
        return evaluate(expr[1], model) and evaluate(expr[2], model)
    elif op == 'or':
        return evaluate(expr[1], model) or evaluate(expr[2], model)
    else:
        raise ValueError(f"Unknown operator: {op}")

def get_symbols(expr):
    if isinstance(expr, str):
        return {expr}
    op = expr[0]
    if op == 'not':
        return get_symbols(expr[1])
    else:
        return get_symbols(expr[1]) | get_symbols(expr[2])

def tt_entails(KB, alpha):
    symbols = list(get_symbols(KB) | get_symbols(alpha))
    for values in product([False, True], repeat=len(symbols)):
        model = dict(zip(symbols, values))
        if evaluate(KB, model) and not evaluate(alpha, model):
            return False
    return True

def print_truth_table(KB, alpha):
    symbols = sorted(list(get_symbols(KB) | get_symbols(alpha)))
    print(f"{' | '.join(symbols)} | A∨C | B∨¬C | KB | A∨B |")
    print('-' * 47)
    for values in product([False, True], repeat=len(symbols)):
        model = dict(zip(symbols, values))
        A, B, C = model['A'], model['B'], model['C']
        val_AorC = A or C
        val_BorNotC = B or (not C)
        val_KB = evaluate(KB, model)
        val_alpha = evaluate(alpha, model)
        row = ' | '.join(['T' if model[s] else 'F' for s in symbols])
        row += f" | {'T' if val_AorC else 'F'} | {'T' if val_BorNotC else 'F'} | {'T' if val_KB else 'F'} | {'T' if val_alpha else 'F'} |"
        print(row)

KB = ('and', ('or', 'A', 'C'), ('or', 'B', ('not', 'C')))
alpha = ('or', 'A', 'B')

print("Truth Table:")
print_truth_table(KB, alpha)
print()
print(f"Does KB entail alpha? {tt_entails(KB, alpha)}")
