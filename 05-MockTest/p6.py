def f(number, even):
    sum = 0
    number = str(number)
    if even == True:
        for n in number:
            n = int(n)
            if n % 2 == 0:
                sum += n
    else:
        for n in number:
            n = int(n)
            if n % 2 != 0:
                sum += n
    return sum


if __name__ == "__main__":
    print(f(3124, True))
    print(f(3124, False))
    print(f(20576, False))
    print(f(20576, True))
    print(f(13115, True))