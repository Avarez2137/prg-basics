def f(fnc, prods):
    return ','.join(fnc(prod) for prod in prods)
