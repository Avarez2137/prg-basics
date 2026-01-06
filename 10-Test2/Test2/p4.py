def f(subjects):
    sub = None
    avg = 0

    for key, grades in subjects.items():
        gradesAvg = sum(grades)/len(grades)
        if gradesAvg > avg:
            sub = key
            avg = gradesAvg

    return sub


if __name__ == "__main__":
    subjects = {"math":[3,4,4],"geo":[5,4,4,4],"comp":[5,4]}
    print(f(subjects))