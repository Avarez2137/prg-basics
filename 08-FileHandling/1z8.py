with open("pets.txt", "r") as file:
    content = file.read()

counter = 0
conent_lines = content.splitlines()
for line in conent_lines:
    splited = line.split()
    counter += len(splited)

print("Number of words:", counter)
