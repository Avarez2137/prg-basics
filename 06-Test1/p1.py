def f(x,y):
    result = x % y
    return hex(result)

if __name__ == "__main__":
    print(f(118,20))
    print(f(210,100))