with open("example2.txt", "w") as writefile:
    writefile.write("Overwrite\n")
with open("example2.txt", "r") as testwritefile:
    print(testwritefile.read())
