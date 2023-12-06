# potential code before try catch
a = 10

try:
    # code to try to execute
    b = int(input("Please enter a number to divide a: "))
    a = a/b
except ZeroDivisionError:
    # code to execute if there is a ZeroDivisionError
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    # code to execute if there is a NameError
    print("You did not provide a number")
except:
    # code to execute if there is any exception
    print("Something went wrong")
else:
    # code to execute if there is no exception
    print("Success!\na =", a)
finally:
    # code to execute at the end of the try except no matter what
    print("Processing Complete")