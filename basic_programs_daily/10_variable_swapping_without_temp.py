# Write a Python program to swap two variables without temp variable.

# input two values from user
a = input("Enter the value of the first variable (a): ")
b = input("Enter the value of the first variable (b): ")

# print original values
print("Original Values: a = " + str(a) + " and b = " + str(b))

# swap the values using a temporary variable
a, b = b, a

# print swapped values
print("Swapped values: a = " + str(a) + " and b = " + str(b))
