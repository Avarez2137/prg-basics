def f(word):
    return '-'.join(word[:i].lower() + word[i].upper() + word[i+1:].lower() for i in range(len(word)))    


if __name__ == "__main__":
    print(f("water"))
    print(f("a"))
    print(f(""))
