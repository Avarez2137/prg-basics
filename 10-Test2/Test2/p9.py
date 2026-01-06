def f(post1, post2):
    arraypost1 = post1.split()
    arraypost2 = post2.split()
    hashtags1 = []
    hashtags2 = []
    finalhash = []

    check = True
    for word in arraypost1:
        if word[0] == "#" and word[1] != "":
            for i in word:
                if i not in "01234567890123456789QWERTYUIOPASDFGHJKLZXCVBNM":
                    check = True
                else:
                    check = False
            if check == True:
                hash = word.split("#")[1]
                hashtags1.append(hash)

    check = True
    for word in arraypost2:
        if word[0] == "#" and word[1] != "":
            for i in word:
                if i not in "0123456789QWERTYUIOPASDFGHJKLZXCVBNM":
                    check = True
                else:
                    check = False
            if check == True:
                hash = word.split("#")[1]
                hashtags2.append(hash)
    for hash1 in hashtags1:
        for hash2 in hashtags2:
            if hash1 == hash2:
                finalhash.append(hash1)
    finalhash = sorted(finalhash)
    return finalhash



if __name__ == "__main__":
    post1 = "#1 in quick #coding in #python #learning #automation"
    post2 = "quick #learning so much with #python #coding #1 #script #vscode"
    print(f(post1, post2))