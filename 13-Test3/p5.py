class C:
    def __init__(self, sektory):
        self.sektory = sektory

    def m1(self, s, n):
        self.sektory[s] = n

    def m2(self, s):
        sum = 0
        for i in s:
            if i in self.sektory.keys():
                sum += self.sektory[i]
        return sum



if __name__ == "__main__":
    stadium = C({"A": 120, "D": 150, "G": 90, "K":110})
    stadium.m1("G", 130)
    print(stadium.m2("GD"))
    print(stadium.m2("KEJ"))