def f(a, b):
    ciag = [0,1]
    i = 1
    while i < b:
        i = ciag[-2] + ciag[-1]
        ciag.append(i)

    sum = 0
    for i in ciag:
        if i >= a and i <= b:
            sum += i

    return sum


if __name__ == "__main__":
    print(f(1,5))
    print(f(6,21))