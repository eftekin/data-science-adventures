NestedT = (1, 2, ("pop", "rock"), (3,4), ("disco", (1,2)))

print("Element 2, 0 of Tuple:", NestedT[2][0])
print("Element 2, 1 of Tuple:", NestedT[2][1])
print("Element 3, 0 of Tuple:", NestedT[3][0])
print("Element 3, 1 of Tuple:", NestedT[3][1])
print("Element 4, 0 of Tuple:", NestedT[4][0])
print("Element 4, 1 of Tuple:", NestedT[4][1])

print("The first element in the second nested tuples:", NestedT[2][1][0])
print("The second element in the second nested tuples:", NestedT[2][1][1])

# length of tuple
print(len(NestedT))

# find the first index of 1
print(NestedT.index(1))
