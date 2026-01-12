import math

class C:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def m1(self):
        if self.x == 0 or self.y == 0:
            return 0
        elif self.x > 0 and self.y > 0:
            return 1
        elif self.x < 0 and self.y > 0:
            return 2
        elif self.x < 0 and self.y < 0:
            return 3
        elif self.x > 0 and self.y < 0:
            return 4
    
    def m2(self, a, b):
        if (self.x == 0 and b == 0) or (self.y == 0 and a == 0): 
            return True
        
        return (self.x > 0 and a > 0 and self.y > 0 and b > 0) or \
               (self.x < 0 and a < 0 and self.y > 0 and b > 0) or \
               (self.x < 0 and a < 0 and self.y < 0 and b < 0) or \
               (self.x > 0 and a > 0 and self.y < 0 and b < 0)

    def m3(self, a, b):
        return math.sqrt((self.x - a) ** 2 + (self.y - b) ** 2) > 5
