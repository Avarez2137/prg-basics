def f(d):
    avg_passengers = sum(d.values()) / len(d)
    return sum(1 for passengers in d.values() if passengers > avg_passengers)


if __name__ == "__main__":
    print(f({"LO231":150,"BA787":120,"NZ15":30}))
    print(f({"LO231":150,"BA787":20,"NZ15":30}))