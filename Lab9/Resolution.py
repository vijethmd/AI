from itertools import product

def is_variable(x):
    return x[0].islower()

def substitute(clause, subs):
    new_clause = []
    for pred, args in clause:
        new_args = []
        for arg in args:
            new_args.append(subs.get(arg, arg))
        new_clause.append((pred, tuple(new_args)))
    return tuple(new_clause)

def unify(a, b, subs=None):
    if subs is None:
        subs = {}
    if a == b:
        return subs
    if is_variable(a):
        subs[a] = b
        return subs
    if is_variable(b):
        subs[b] = a
        return subs
    return None

def resolve(ci, cj):
    resolvents = []
    for (pi, args_i) in ci:
        for (pj, args_j) in cj:
            if pi == pj.replace("¬", "") or pj == pi.replace("¬", ""):
                neg_i = pi.startswith("¬")
                neg_j = pj.startswith("¬")
                if neg_i != neg_j:
                    subs = {}
                    for ai, aj in zip(args_i, args_j):
                        subs = unify(ai, aj, subs)
                        if subs is None:
                            break
                    if subs is not None:
                        new_ci = [p for p in ci if (p[0], p[1]) != (pi, args_i)]
                        new_cj = [p for p in cj if (p[0], p[1]) != (pj, args_j)]
                        resolvent = substitute(new_ci + new_cj, subs)
                        resolvents.append(tuple(resolvent))
    return resolvents

def resolution(kb, query):
    query = tuple([("¬Likes", ("John","Peanuts"))])
    clauses = kb + [query]

    while True:
        new = set()
        pairs = [(clauses[i], clauses[j])
                 for i in range(len(clauses))
                 for j in range(i+1, len(clauses))]
        for ci, cj in pairs:
            resolvent = resolve(ci, cj)
            if () in resolvent:
                return True
            for r in resolvent:
                new.add(r)
        if new.issubset(set(clauses)):
            return False
        clauses.extend(list(new))

# Knowledge Base Clauses
KB = [
    (("¬Food",("x",)), ("Likes",("John","x"))),
    (("Food",("Apple",)),),
    (("Food",("Vegetable",)),),
    (("¬Eats",("x","y")), ("Killed",("x",)), ("Food",("y",))),
    (("Eats",("Anil","Peanuts")),),
    (("Alive",("Anil",)),),
    (("¬Eats",("Anil","y")), ("Eats",("Harry","y"))),
    (("¬Alive",("x",)), ("¬Killed",("x",))),
    (("Killed",("x",)), ("Alive",("x",))),
]

if resolution(KB, ("Likes",("John","Peanuts"))):
    print("Conclusion: John likes peanuts ")
else:
    print("Could not prove the statement.")
