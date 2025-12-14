def f(thing_to_wash, extra_rinse, extra_spin):
    time = 0
    if thing_to_wash == "J":
        time =+ 40
    elif thing_to_wash == "U":
        time += 70
    elif thing_to_wash == "S":
        time += 20

    if extra_rinse == True:
        time += 15

    if extra_spin == True:
        time += 9

    return time


if __name__ == "__main__":
    print(f("U", False, True))
    print(f("J", True, True))
    print(f("S", False, False))
