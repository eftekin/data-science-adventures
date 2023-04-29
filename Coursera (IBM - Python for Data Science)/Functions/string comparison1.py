# compare two strings directly
string = "Tesla is the best"


def check_string(text):
    # use if else statement and 'in' operator to compare the string
    if text in string:
        return "\nString matched"
    else:
        return "\nString not matched"


print(check_string("Tesla is the best"))
