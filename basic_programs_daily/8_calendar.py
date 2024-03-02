# Write a Python program to display calendar.

import calendar

year = int(input("Enter year (YYYY): "))
month = int(input("Enter month (MM): "))

cal = calendar.month(year, month)
print(cal)
