with open("example2.txt", "r") as readfile:
    with open("example3.txt", "w") as writefile:
        for line in readfile:
            writefile.write(line)

# Verify if the copy is successfully executed
with open("example3.txt", "r") as testwritefile:
    print(testwritefile.read())
