# Assuming there are no accidents or delays, the distance that a car travels down the interstate
# can be calculated with the following formula:
# Distance 5 Speed 3 Time
# A car is traveling at 70 miles per hour. Write a program that displays the following:
# • The distance the car will travel in 6 hours
# • The distance the car will travel in 10 hours
# • The distance the car will travel in 15 hours


# car speed in mph
speed = 70

# time variables by hour
time1 = 6
time2 = 10
time3 = 15

# distance calculation with speed*time formula
distance1 = speed * time1
distance2 = speed * time2
distance3 = speed * time3

# print calculated data
print("The car traveled", distance1, "miles in", time1, "hours.")
print("The car traveled", distance2, "miles in", time2, "hours.")
print("The car traveled", distance3, "miles in", time3, "hours.")
