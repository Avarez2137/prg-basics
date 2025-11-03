###
# Checks if the given day number of the month is correct
#
month = int(input('Enter month number (1..12): '))
day = int(input('Enter the day number of the month: '))
day_ok = False

if month==1 or month==3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    days = 31 ## months with 31 days
elif month == 4 or month == 6 or month == 9 or month == 11:
    days = 30 ## months with 30 days
elif month  == 2:
    days = 28 ## February 28 days
else:
    print("incorrect month!")
    exit()

if month==1 or month==3 or ...:
    if day >=1 and day <= 31:
        day_ok = True
elif month== ...:
    if day >=1 and day <= ...:
        ...
...

message = f'Day {...} for the month {...}'
if day_ok:
    print('{message} is correct')
else
    print(...)