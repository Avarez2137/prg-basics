person = {
   "name": "Marek",
   "surname": "Banach",
   "age": 25,
   "hobby": ["swimming","excursions"],
   "married": True,
   "phone":{"landline":"123444321","mobile":"777888999"}
}

print(person["name"])

for hobby in person["hobby"]:
    print(hobby)

print(person)

person["surname"] = "Nowak"

person["married"] = False

person["gender"] = "Male"
print(person)

person["hobby"].append("bicycle")
print(person)
