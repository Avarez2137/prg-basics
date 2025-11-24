def f(sentence):
    sum = 0
    for i in sentence:
        sum += ord(i)
    if sum % 3 == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    print(f("hello world"))    
    print(f("university"))
    print(f("student"))