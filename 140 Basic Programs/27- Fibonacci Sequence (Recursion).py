# Write a Python Program to Print the Fibonacci sequence with recursion.

# Fibonacci sequence:
# The Fibonacci sequence is a series of numbers where each number is the sum of the two
# preceding ones, typically starting with 0 and 1. So, the sequence begins with 0 and 1, and
# the next number is obtained by adding the previous two numbers. This pattern continues
# indefinitely, generating a sequence that looks like this:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, and so on.
# Mathematically, the Fibonacci sequence can be defined using the following recurrence
# relation:
# 𝐹(0) = 0 𝐹(1) = 1 𝐹(𝑛) = 𝐹(𝑛 − 1) + 𝐹(𝑛 − 2) 𝑓𝑜𝑟 𝑛 > 1

n_terms = int(input("How many terms?\n"))

if n_terms < 0:
    print("Please enter a positive number")
else:

    # get fibonacci sequence function
    def fibonacci(n):
        if n == 0 or n == 1:
            return n
        elif n < 0:
            return -1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    for i in range(n_terms):
        print(fibonacci(i))
