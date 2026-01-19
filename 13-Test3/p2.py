def f(expression):
    stack = []
    tokens = expression.split()

    for token in tokens:
        if token in ["+", "-"]:
            b = int(stack.pop())
            a = int(stack.pop())
            if token == "+":
                result = a + b
            if token == "-":
                result = a - b
            stack.append(result)
        else:
            stack.append(token)
    return stack[0]



if __name__ == "__main__":
    print(f("2 3 4 5 + - +"))
    print(f("11 7 + 15 - 14 +"))