with open("abc.txt", "r") as file:
    content = file.read()
    print(content)

plik = open("abc.txt")
print(plik)
plik.close()
plik = open("abc.txt", "r")
print(plik)
plikContent = plik.read()
plik.close()
print(plikContent)