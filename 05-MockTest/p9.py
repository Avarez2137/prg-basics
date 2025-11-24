def f(sentence):
    counter = 0
    toCheck = "aeiouy"
    for i in sentence:
        for j in toCheck:
            if i == j:
                counter += 1
    return counter


if __name__ == "__main__":
    print(f("water"))
    print(f("hello world"))
    print(f("hello aeiouy"))