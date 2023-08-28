# a+ : Appending and Reading. Creates a new file, if none exists.

with open("example2.txt", "a+") as testwritefile:
    print("Initial Location: {}".format(testwritefile.tell()))
    data = testwritefile.read()

    if (not data):  # empty strings return false in python
        print("Read nothing")
    else:
        print(testwritefile.read())

    testwritefile.seek(0, 0)  # move 0 bytes from beginning.

    print("\nNew Location: {}".format(testwritefile.tell()))
    data = testwritefile.read()
    if (not data):
        print("Read nothing")
    else:
        print(data)

    print("Location after read: {}".format(testwritefile.tell()))
