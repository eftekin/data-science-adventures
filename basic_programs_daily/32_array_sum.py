# Write a Python Program to find sum of array.


def sum_of_array(arr):
    total = 0

    for element in arr:
        total += element

    return total


array = [1, 2, 3]
result = sum_of_array(array)
print(f"Sum of the array:", result)
