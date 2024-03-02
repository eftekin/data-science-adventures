# Write a Python program to calculate the product, multiplying all the numbers in a
# given tuple.
# tuple1 = (4, 3, 2, 1, 0)
# tuple2 = (5, 10, 2, 4)

def calculateProduct(t):
    product = 1
    for i in t:
        product *= i
    return product


tuple1 = (4, 3, 2, 1, 0)
tuple2 = (5, 10, 2, 4)

print("Product of elements in tuple1:", calculateProduct(tuple1))
print("Product of elements in tuple2:", calculateProduct(tuple2))
