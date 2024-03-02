# Write a Python program to convert kilometers to miles.

kilometers = float(input("Enter the distance in kilometers: "))

# Convert kilometers into miles (1 kilometers = 0.621371192 miles)
miles = kilometers * 0.621371192

# Display the result
print(str(kilometers) + " kilometers is equal to " + str(round(miles, 2)) + " miles")
