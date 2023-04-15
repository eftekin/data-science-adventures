# Create a list with includes 5, 9, 10, 12, 7, 3, 11 numbers. Write the code that finding the length,
# biggest-smallest element, sum, average and sort the list

# list of numbers
numbers = [5, 9, 10, 12, 7, 3, 11]

# length of the numbers
length = len(numbers)

# biggest and smallest numbers
biggest = max(numbers)
smallest = min(numbers)

# sum of the numbers
total = sum(numbers)

# calculation of the average
average = total / length

# sort the list
sorted_numbers = sorted(numbers)

# print the results
print(f"Length: {length}")
print(f"Biggest number: {biggest}")
print(f"Smallest number: {smallest}")
print(f"Sum: {total}")
print(f"Average: {average:.2f}")
print(f"Sorted list: {sorted_numbers}")


