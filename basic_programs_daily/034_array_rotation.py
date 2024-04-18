# Write a Python Program for array rotation.


def rotate_array(arr, d):
    n = len(arr)

    # check if 'd' is valid
    if d < 0 or d >= n:
        return "Invalid value"

    # create a new array to store the rotated elements.
    rotated_arr = [0] * n

    # perform the rotation
    for i in range(n):
        rotated_arr[i] = arr[(i + d) % n]

    return rotated_arr


# input array
arr = [1, 2, 3, 4, 5]

# number of positions to rotate
d = 2

# call the rotate_array function
result_arr = rotate_array(arr, d)

# print the results
print("Original Array:", arr)
print("Rotated Array:", result_arr)
