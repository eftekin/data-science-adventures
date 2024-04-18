# Write a Python Program to find largest element in an array.


def find_largest_element(arr):
    if not arr:
        return "Array is empty"

    # initialize the first element as the largest
    largest_element = arr[0]

    # iterate through the array to find the largest element
    for element in arr:
        if element > largest_element:
            largest_element = element

    return largest_element


array = [1, 2, 3, 4, 99]
result = find_largest_element(array)
print(f"The largest element in the array is: {result}")
