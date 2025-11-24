def f(name):
    array = name.split()
    firstLetters = ""
    for a in array:
        firstLetters += a[0:1]
    return firstLetters



if __name__ == "__main__":
    print(f("Internet of Things"))
    print(f("For Your Information"))
    print(f("Python"))