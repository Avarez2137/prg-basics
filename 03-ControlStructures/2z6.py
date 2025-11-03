number = float(input("Podaj liczbę do sprawdzenia: "))

if number == 0:
    print("Number is 0")
elif number>0:
    print(f'Number {number} is positive')
elif number<0:
    print(f'Number {number} is negative')