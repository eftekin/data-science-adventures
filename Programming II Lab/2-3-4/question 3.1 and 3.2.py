# Write a program that asks for the length and width of two rectangles. The program should tell
# the user which rectangle has the greater area, or if the areas are the same. (The area of a rectangle
# is the rectangle’s length times its width.)
#
# Areas of Rectangles The area of a rectangle is the rectangle’s length times its width. Write a
# program that asks for the length and width of two rectangles. The program should tell the user
# which rectangle has the greater area, or if the areas are the same.

# Get input for rectangle 1
length1 = float(input("Enter the length of rectangle 1: "))
width1 = float(input("Enter the width of rectangle 1: "))

# Get input for rectangle 2
length2 = float(input("Enter the length of rectangle 2: "))
width2 = float(input("Enter the width of rectangle 2: "))

# Calculate area of rectangle 1 and rectangle 2
area1 = length1 * width1
area2 = length2 * width2

# Compare areas and print the result
if area1 > area2:
    print("The area of rectangle 1 is larger.")
elif area1 < area2:
    print("The area of rectangle 2 is larger.")
else:
    print("Both rectangles have the same area.")
