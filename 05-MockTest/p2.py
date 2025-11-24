def f(n1,n2,n3):
    if n1 != n2 and n2 != n3 and n3 != n1:
        return True
    else:
        return False


if __name__ == "__main__":
    print(f(4,8,5))
    print(f(2,9,2))