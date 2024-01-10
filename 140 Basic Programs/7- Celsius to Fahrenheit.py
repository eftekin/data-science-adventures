# Write a Python program to convert Celsius to Fahrenheit.

celsius = float(input("Enter the temperature in Celsius: "))

# F = (C * 9/5) + 32
fahrenheit = (celsius * 9 / 5) + 32

print(
    str(celsius)
    + " degrees in celsius equals to "
    + str(fahrenheit)
    + " degrees in fahrenheit."
)
