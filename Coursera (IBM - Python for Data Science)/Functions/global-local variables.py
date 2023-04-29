def square(a):
    # Local variable b
    b = 1
    c = a * a + b
    print(a, "if you square +1", c)
    return c


x = 2  # global variable
z = square(x)
