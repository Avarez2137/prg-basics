def f(cars, order):
    if order == 1:
        return sorted(cars, key=lambda x: list(x.keys())[0])
    elif order == 2:
        return sorted(cars, key=lambda x: list(x.values())[0], reverse=True)
