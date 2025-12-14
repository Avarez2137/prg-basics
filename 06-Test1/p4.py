def f(wysokosc_startowa, wspolczynnik_odbicia, wysokosc_docelowa):
    height = wysokosc_startowa
    counter = 0
    while height >= wysokosc_docelowa:
        height = height * wspolczynnik_odbicia
        counter += 1
    return counter


if __name__ == "__main__":
    print(f(12, 0.9, 10))
    print(f(10, 0.6, 1))
    print(f(25, 0.85, 7))