def f(d):
    counter = 0

    for i in d:
        if i == "-":
            counter -= 1
        if i == "+":
            counter += 1
    return counter



if __name__ == "__main__":
    print(f(""))
    print(f("+-+"))
    print(f("+-+++-+---"))
    print(f("+-+++++-"))