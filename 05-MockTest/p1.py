def f(AmountToPay):
    counter = 0
    while AmountToPay > 0:
        if AmountToPay - 5 >= 0:
            AmountToPay -= 5
            counter += 1
        elif AmountToPay - 2 >= 0:
            AmountToPay -= 2
            counter += 1
        elif AmountToPay - 1  >= 0:
            AmountToPay -= 1
            counter += 1
    return counter


if __name__ == "__main__":
    print(f(23))
    print(f(8))