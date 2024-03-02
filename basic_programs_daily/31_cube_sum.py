# Write a Python Program for cube sum of first n natural numbers?


def cube_sum(n):
    if n <= 0:
        return 0
    else:
        total = sum([i**3 for i in range(1, n + 1)])
        return total


# user input
n = int(input("Enter the value of n: "))

if n <= 0:
    print("Please enter a positive integer.")
else:
    result = cube_sum(n)
    print(f"The cube sum of the first {n} natural number is: {result}")
