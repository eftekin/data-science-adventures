def printAll(*args):
    print("No of arguments: ", len(args))
    for argument in args:
        print(argument)


printAll("iPhone", "iPad", "Mac")


def printDictionary(**hab):
    for key in hab:
        print(key + " : " + hab[key])


printDictionary(Country="Canada", Province="Ontario", City="Toronto")


def addItems(list):
    list.append("Three")
    list.append("Four")


myList = ["One", "Two"]

addItems(myList)

print(myList)
