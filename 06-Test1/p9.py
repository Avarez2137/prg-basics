def f(sizes):
    array = sizes.split(",")
    Ss = 0
    Ms = 0
    Ls = 0
    for i in array:
        if i == "L":
            Ls += 1
        elif i == "M":
            Ms += 1
        elif i == "S":
            Ss += 1

    if Ss <= Ms and Ss <= Ls:
        return "S"
    if Ms < Ss and Ms <= Ls:
        return "M"
    if Ls < Ss and Ls < Ms:
        return "L"

    return "L"


if __name__ == "__main__":
    print(f("L,S,L,M,L,S,S,L"))
    print(f("M,L,L,L,M"))
    print(f("M,L,M,L,S,S,S"))
    print(f("S,M,L"))
    print(f("S,M"))