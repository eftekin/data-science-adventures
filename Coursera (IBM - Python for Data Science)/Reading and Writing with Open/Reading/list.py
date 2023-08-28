example1 = "example1.txt"
with open(example1, "r") as file1:
    FileasList = file1.readlines()

# print the first line

print(FileasList[0])

# print the third line

print(FileasList[2])
