# Write a Python Program to Check Armstrong Number

# Armstrong Number:
# It is a number that is equal to the sum of its own digits, each raised to a power equal to the
# number of digits in the number.
# For example, let's consider the number 153:
# It has three digits (1, 5, and 3).
# If we calculate + , we get , which is equal to .
# So, 153 is an Armstrong number because it equals the sum of its digits raised to the power
# of the number of digits in the number.

num = int(input("Enter a number: "))

# Calculate the number of digits in num
num_str = str(num)
num_digits = len(num_str)

# initialize variables
sum_of_powers = 0
temp_num = num

# calculate the sum of digits raised to the power of num_digits

while temp_num > 0:
    digit = temp_num % 10
    sum_of_powers += digit**num_digits
    temp_num //= 10

# check if it's an Armstrong number
if sum_of_powers == num:
    print(str(num) + " is an Armstrong number.")
else:
    print(str(num) + " is not an Armstrong number.")
