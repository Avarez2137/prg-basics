###
# Prints some array elements
#
arr = [2, 3, 7, 5, 4]

def f9(array):
    array = str(array)
    all = ""
    for i in array:
        all += i + " "
    return all

print(arr)
print('Number of elements', len(arr))
print('First value', arr[0])
print('Second value', arr[1])
print('Last value', arr[-1])
print('last but one value', arr[len(arr)-2])
print('sum of the first and last value', (arr[0] + arr[-1]))
print('middle value', arr[len(arr)//2])
print('all array values separated by a single space', f9(arr))
