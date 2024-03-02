with open("example2.txt", "r+") as testwritefile:
    testwritefile.seek(0, 0)  # write at beginning of file
    testwritefile.write("Line 1" + "\n")
    testwritefile.write("Line 2" + "\n")
    testwritefile.write("Line 3" + "\n")
    testwritefile.write("Line 4" + "\n")
    testwritefile.write("finished\n")
    # This will reduce the file to your data and delete everything that follows.
    testwritefile.truncate()
    testwritefile.seek(0, 0)
    print(testwritefile.read())
