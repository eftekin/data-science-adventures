with open("example2.txt", "r") as readfile:
    with open("example3.txt", "w") as writefile:
        for line in readfile:

            writefile.write(line)
