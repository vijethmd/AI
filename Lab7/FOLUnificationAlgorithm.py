def is_variable(x):
    return isinstance(x, str) and x[0].islower()

def occurs_check(var, term):
    if var == term:
        return True
    if isinstance(term, tuple):
        for t in term[1]:
            if occurs_check(var, t):
                return True
    return False

def substitute(S, term):
    if is_variable(term):
        return S.get(term, term)
    if isinstance(term, tuple):
        pred, args = term
        new_args = [substitute(S, a) for a in args]
        return (pred, new_args)
    return term

def unify(x1, x2, S=None):
    if S is None:
        S = {}

    x1 = substitute(S, x1)
    x2 = substitute(S, x2)

    if is_variable(x1):
        if x1 == x2:
            return S
        if occurs_check(x1, x2):
            return "FAILURE"
        S[x1] = x2
        return S

    if is_variable(x2):
        if occurs_check(x2, x1):
            return "FAILURE"
        S[x2] = x1
        return S

    if isinstance(x1, tuple) and isinstance(x2, tuple):
        p1, args1 = x1
        p2, args2 = x2
        if p1 != p2:
            return "FAILURE"
        if len(args1) != len(args2):
            return "FAILURE"
        for a1, a2 in zip(args1, args2):
            S = unify(a1, a2, S)
            if S == "FAILURE":
                return "FAILURE"
        return S

    if x1 == x2:
        return S

    return "FAILURE"


expr1 = ("Eats", ["x", "Apple"])
expr2 = ("Eats", ["Riya", "y"])

S = unify(expr1, expr2)
print("Substitution:", S)
