# Write a Python program to solve quadratic equation.
import math

a = float(input("Enter the coefficient of x^2: "))
b = float(input("Enter the coefficient of x: "))
c = float(input("Enter the coefficient of x^0: "))

# Check the equation quadratic or not
if a == 0:
    print("Coefficient of x^2 cannot be 0")
else:
    discriminant = b**2 - 4 * a * c
    if discriminant > 0:
        # the equation has two real and distinct roots
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print("Root 1 = " + str(round(root1, 2)))
        print("Root 2 = " + str(round(root2, 2)))
    elif discriminant == 0:
        # the equation has one real root (repeated)
        root = -b / (2 * a)
        print("There is only one root: " + str(round(root, 2)))
    else:
        # the equation has complex roots
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2 * a)
        print(
            "Root 1 = "
            + str(round(real_part, 2))
            + " + "
            + str(round(imaginary_part, 2))
            + "i"
        )
        print(
            "Root 2 = "
            + str(round(real_part, 2))
            + " - "
            + str(round(imaginary_part, 2))
            + "i"
        )
