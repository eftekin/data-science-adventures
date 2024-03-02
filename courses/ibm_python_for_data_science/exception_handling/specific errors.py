a = 1

try:
    b = int(input("Please enter a number to divide a: "))
    a = a/b
    print("Success a =",a)
except ZeroDivisionError:
    print("The number you provided can't divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")