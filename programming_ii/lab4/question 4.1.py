# The distance a vehicle travels can be calculated as follows:
# distance = speed x time
# For example, if a train travels 40 miles per hour for three hours, the distance traveled is
# 120 miles. Write a program that asks the user for the speed of a vehicle (in miles per hour)
# and the number of hours it has traveled. It should then use a loop to display the distance
# the vehicle has traveled for each hour of that time period.


# user input for speed and time
speed = int(input("What is the speed of the vehicle in mph? "))
hours = int(input("How many hours has it traveled? "))

# table header
print("Hour | Distance Traveled")
print("------------------------")

# loop to calculate and print distance for each hour
for hour in range(1, hours+1):
    distance = speed * hour
    print(hour, "\t", distance)
