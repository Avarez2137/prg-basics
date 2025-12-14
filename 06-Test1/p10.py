def f(time1, time2):
    t1 = time1.split(":")
    t2 = time2.split(":")

    t1time = 0
    t2time = 0

    if t1[1][-2::] == "pm":
        t1time += int(t1[0])+12 + int(t1[1][0:2])
    else:
        t1time += int(t1[0]) + int(t1[1][0:2])
    
    if t2[1][-2::] == "pm":
        t2time += int(t2[0])+12 + int(t2[1][0:2])
    else:
        t2time += int(t2[0]) + int(t2[1][0:2])
    
    if t1time > t2time:
        return time2
    elif t2time > t1time:
        return time1
    elif t1time == t2time:
        return time1
    return time1


if __name__ == "__main__":
    print(f("13:06","13:12"))
    print(f("1:38pm","13:31"))
    print(f("08:08","8:01am"))
    print(f("6:00pm","18:00"))