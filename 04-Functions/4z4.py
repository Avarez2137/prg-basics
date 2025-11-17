###
# Calculates the sum of the digits in a number
#
def sum_digits(number):
    sum = 0
    abs_str_number = str(abs(number))
    for i in abs_str_number:
        sum += int(i)
    return sum

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')