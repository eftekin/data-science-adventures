
# Write a program that asks the user to enter a number of seconds and works as follows:
# • There are 60 seconds in a minute. If the number of seconds entered by the user is greater
# than or equal to 60, the program should convert the number of seconds to minutes and seconds.
# • There are 3,600 seconds in an hour. If the number of seconds entered by the user is
# greater than or equal to 3,600, the program should convert the number of seconds to
# hours, minutes, and seconds.
# • There are 86,400 seconds in a day. If the number of seconds entered by the user is
# greater than or equal to 86,400, the program should convert the number of seconds to
# days, hours, minutes, and seconds.

# input for number of seconds
seconds = int(input("Enter the number of seconds: "))

# calculate days, hours, minutes, and remaining seconds
days = seconds // 86400
seconds %= 86400
hours = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60

# print the result
if days > 0:
    print(f"{days} day(s), {hours} hour(s), {minutes} minute(s), {seconds} second(s)")
elif hours > 0:
    print(f"{hours} hour(s), {minutes} minute(s), {seconds} second(s)")
elif minutes > 0:
    print(f"{minutes} minute(s), {seconds} second(s)")
else:
    print(f"{seconds} second(s)")
