# Write a Python Program to Display the multiplication Table.

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(str(num) + " x " + str(i) + " = " + str(i * num))
