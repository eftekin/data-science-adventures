# Write a Python program to do arithmetical operations addition and division.


def addition(a, b):
    c = a + b
    return c


def division(a, b):
    c = a / b
    return c


num1 = float(input("Please enter the first number for addition: "))
num2 = float(input("Please enter the second number for addition: "))

print("Sum of two numbers: " + str(addition(num1, num2)))

num3 = float(input("Please enter the first number for division: "))
num4 = float(input("Please enter the second number for division: "))

print("Division of two numbers: " + str(division(num3, num4)))
