# Write a program that uses nested loops to draw this pattern:
    #
    ##
    # #
    #  #
    #   #
    #    #


# loop to draw the pattern
for i in range(6):
    for j in range(i + 1):
        if j == 0 or j == i:
            print("#", end="")
        else:
            print(" ", end="")
    print()
