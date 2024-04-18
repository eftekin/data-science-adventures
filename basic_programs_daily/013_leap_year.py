# Write a Python Program to Check Leap Year.

# Get user input
year = int(input("Enter a year: "))


# If a year is divisible by 100, but not 400, then it is not a leap year.
if (year % 400 == 0) and (year % 100 == 0):
    print(str(year) + " is a leap year.")
# See if the number is evenly divisible by 4 and not a century year.
elif (year % 4 == 0) and (year % 100 != 0):
    print(str(year) + " is a leap year.")
# Otherwise the year is not a leap year.
else:
    print(str(year) + " is not a leap year")
