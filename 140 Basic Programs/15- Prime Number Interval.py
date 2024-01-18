# Write a Python Program to Print all Prime Numbers in an Interval of 1-100.

lower = 1
upper = 100

print("Prime numbers between " + str(lower) + " and " + str(upper) + " are: ")

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)
