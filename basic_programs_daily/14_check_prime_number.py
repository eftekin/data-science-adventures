# Write a Python Program to Check Prime Number.

num = int(input("Enter a number: "))

# define a boolean prime variable
not_prime = False

if num == 1:
    not_prime = True
elif num > 1:
    for i in range(2, num):
        if num % i == 0:
            not_prime = True  # break the loop if the number is divisible by another number smaller than itself.
            break

if not_prime:
    print(str(num) + " is not a prime number.")
else:
    print(str(num) + " is a prime number.")
