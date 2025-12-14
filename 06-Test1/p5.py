def f(t):
    time_split = t.split(":")

    if len(time_split) > 3:
        return False
    
    for i in time_split:
        if i.isdigit() == False:
            return False
        
    if int(time_split[0]) > 23:
        return False
    
    if int(time_split[1]) > 59:
        return False
    
    if int(time_split[2]) > 59:
        return False
        
    return True


if __name__ == "__main__":
    print(f("17:38:25"))
    print(f("11:61:43"))
    print(f("23:05:19:46"))
    print(f("23:AB:10"))
    print(f("11:11:59"))
    print(f("11:11:60"))