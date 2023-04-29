# compare two strings using == operator and function
def compareStrings(x, y):
    if x == y:
        return 1


str1 = "Tesla is the best"
str2 = "Tesla is the best"

check = compareStrings(str1, str2)

if check == 1:
    print("\nString Matched")
else:
    print("\nString not Matched")
