example1 = "example1.txt"
with open(example1, "r") as file1:
    i = 0
    for line in file1:
        print("Iteration", str(i), ": ", line)
        i = i + 1
