# Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal.

dec_num = int(input("Enter a decimal number: "))

print("The decimal value of " + str(dec_num) + " is:")
print(str(bin(dec_num) + " in binary."))
print(str(oct(dec_num) + " in octal."))
print(str(hex(dec_num) + " in hexadecimal."))
