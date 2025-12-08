# class definition
class Student():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.year = 0

def main():
    # object creation based on the class
    student1 = Student()
    student2 = Student()
    student1.name = "Dominic"
    student1.age = 19
    student1.year = 1
    student2.name = "Olivia"
    student2.age = 21
    student2.year = 2

    print('LIST OF STUDENTS')
    print('================')
    print(f'{student1.name}, {student1.age} years old, student of {student1.year} year')
    print(f'{student2.name}, {student2.age} years old, student of {student2.year} year')

if __name__ == "__main__":
    main()