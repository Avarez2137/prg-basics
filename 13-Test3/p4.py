class C:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self):
        lname = self.name[:2]
        lsurname = self.surname[:2]

        if self.age < 18:
            lname = lname.lower()
            lsurname = lsurname.lower()
        else:
            lname = lname.upper()
            lsurname = lsurname.upper()

        return f"{lname}-{lsurname}-{str(self.age)}"



if __name__ == "__main__":
    print(C("John", "May", 18))
    print(C("Anna", "Brown", 17))