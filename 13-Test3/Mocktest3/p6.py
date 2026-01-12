class C:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def __str__(self):
        initials = (self.first_name[0] + self.last_name[0]).lower() if self.age < 18 else (self.first_name[0] + self.last_name[0]).upper()
        return f"{initials}{self.age}"
