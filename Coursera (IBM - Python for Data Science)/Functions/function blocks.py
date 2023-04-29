# block
a1 = 4
b1 = 5
c1 = a1 + b1 + 2 * a1 * b1 - 1
if (c1 < 0):
    c1 = 0
else:
    c1 = 5

print(c1)


# Make a function for the calculation above
def Equation(a, b):
    c = a + b + 2 * a * b - 1
    if (c < 0):
        c = 0
    else:
        c = 5
    return c


print(Equation(4, 5))
