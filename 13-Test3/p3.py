import re

def f(vname):
    test = r'^[a-zA-Z_][a-zA-Z0-9_]{0-4}$'

    #if re.match(test, vname):
    if re.match('^[a-zA-Z_][a-zA-Z0-9_]{0}$', vname):
        return True
    elif re.match('^[a-zA-Z_][a-zA-Z0-9_]{1}$', vname):
        return True
    elif re.match('^[a-zA-Z_][a-zA-Z0-9_]{2}$', vname):
        return True
    elif re.match('^[a-zA-Z_][a-zA-Z0-9_]{3}$', vname):
        return True
    elif re.match('^[a-zA-Z_][a-zA-Z0-9_]{4}$', vname):
        return True
    else:
        return False



if __name__ == "__main__":
    print(f("aBC"))
    print(f("_ab_c"))
    print(f("abcdef"))
    print(f("8abc"))
    print(f("_aB8_"))
    print(f("a"))
    print(f("ab"))
    print(f("abc"))
    print(f("abcd"))
    print(f("abcde"))
    print(f("abcdef"))
