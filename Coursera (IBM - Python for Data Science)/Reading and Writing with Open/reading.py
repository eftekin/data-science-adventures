example1 = "example1.txt"
file1 = open(example1, "r")

print("file name is " + file1.name)
print("file mode is " + file1.mode + "\n")

# read the file

fileContent = file1.read()
print(fileContent)

print(type(fileContent))

file1.close()
