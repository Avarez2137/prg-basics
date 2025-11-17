###
# Sums numbers entered by user
#
total_sum = 0
counter = 0

while True:
    number = int(input("Enter a number (0 to stop): "))
    
    if number == 0:
        break  # Exit the loop when 0 is entered
    counter += 1
    total_sum += number
    mean = total_sum / counter

print(f"The total sum of the numbers is: {mean}")