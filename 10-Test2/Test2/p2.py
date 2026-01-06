def f(h0,r,h):
    height = h0
    counter = 0
    while height >= h:
        height *= r
        counter += 1
    return counter



if __name__ == "__main__":
    print(f(10,0.8,5))
    print(f(10,0.95,5))
    print(f(12,0.7,2))
