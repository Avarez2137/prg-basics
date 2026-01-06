def f(n):
    if n == 0:
        return ""
    x = "*"
    while n > 1:
        x += "/*"
        n -= 1
    return x


if __name__ == "__main__":
    print(f(4))
    print(f(1))
    print(f(0))