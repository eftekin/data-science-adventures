numbers = []

for i in range(20):
    num = float(input("Enter a number: "))
    numbers.append(num)

lowest = min(numbers)
highest = max(numbers)
total = sum(numbers)
average = total / len(numbers)

print("The lowest number is:", lowest)
print("The highest number is:", highest)
print("The total of the numbers is:", total)
print("The average of the numbers is:", average)
