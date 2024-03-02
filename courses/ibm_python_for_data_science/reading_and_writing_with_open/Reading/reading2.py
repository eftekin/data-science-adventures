example1 = "example1.txt"
with open(example1, "r") as file1:
    fileContent = file1.read()
    print(fileContent)

print(file1.closed)  # prints true

with open(example1, "r") as file1:
    fileContent = file1.read(4)  # prints first four characters
    print(fileContent)

with open(example1, "r") as file1:
    fileContent = file1.read(4)
    fileContent = file1.read(4)
    fileContent = file1.read(7)
    fileContent = file1.read(15)
    print(fileContent)

# read one line
with open(example1, "r") as file1:
    print("first line: " + file1.readline())

with open(example1, "r") as file1:
    print(file1.readline(20))  # does not read past the end of line
    print(file1.read(20))  # Returns the next 20 chars
