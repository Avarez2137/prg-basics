def f(n):
    a1 = 0
    a2 = 1
    if n == 1:
        return 0 
    elif n == 2:
        return 1
    else:
        w = 0
        i = 3
        while i <= n:
            w = a1 + a2
            a1 = a2
            a2 = w
            i += 1
        return w



if __name__ == "__main__":
    print(f(1))
    print(f(5))
    print(f(9))