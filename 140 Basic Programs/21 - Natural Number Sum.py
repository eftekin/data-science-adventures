# Write a Python Program to Find the Sum of Natural Numbers.

limit = int(input("Enter the limit: "))

sum = 0

for i in range(1, limit + 1):
    sum += i


print("The sum of natural numbers up to " + str(limit) + " is " + str(sum))
