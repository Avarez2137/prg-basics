def f(student1, student2):
    grades1 = student1.split(",")
    grades2 = student2.split(",")
    count1 = 0
    count2 = 0
    for i in grades1:
        if i == "3" or i == "4" or i == "5":
            count1 += 1

    for i in grades2:
        if i == "3" or i == "4" or i == "5":
            count2 += 1

    if count1 > count2:
        return 1
    elif count2 > count1:
        return 2
    return 0


if __name__ == "__main__":
    print(f("3,4,5","4,3"))
    print(f("3,2,5","5,5,2,5"))
    print(f("3,2,5,2,2","4,4"))
