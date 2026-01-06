import re

def f(email):
    emailarray = email.split()
    check = True
    n = 0 
    list = {}
    for word in emailarray:
        for i in word:
            if i in "0123456789":
                check = True
            else:
                check = False
        if check == True:
            list[emailarray[n+1]] = int(word)
        n+=1
        
    return list
    
    
        
if __name__ == "__main__":
    email = "To buy for the office: 5 blinders, 14 highlighters and 21 ballpens"
    print(f(email))