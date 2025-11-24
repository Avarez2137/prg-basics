def f(cardNumber):
    maskedNumber = "" + cardNumber[0:2]
    for i in range(0,10):
        maskedNumber += "*"
    maskedNumber = maskedNumber + cardNumber[12:]
    return maskedNumber

if __name__ == "__main__":
    print(f("5290312400019022"))