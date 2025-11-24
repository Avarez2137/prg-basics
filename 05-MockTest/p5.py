def f(binaryNumber):
    for i in binaryNumber:
        if str(i) != "1" and str(i) != "0":
            return False
    return True
    

if __name__ == "__main__":
    print(f("101101"))
    print(f("1311a10100"))
