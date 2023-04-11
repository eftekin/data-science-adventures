# Write a program that uses nested loops to draw this pattern:
    #
    ##
    # #
    #  #
    #   #
    #    #


# loop to draw the pattern
n = 6
for row in range(n):
    text = ""
    for column in range(row + 1):
        if column == 0 or column == row:
            text += "#"
        else:
            text += " "
    print(text)

