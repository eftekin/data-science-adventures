# You have a group of friends coming to visit for your high school reunion, and you want to take
# them out to eat at a local restaurant. You aren’t sure if any of them have dietary restrictions, but
# your restaurant choices are as follows:
# Joe’s Gourmet Burgers—Vegetarian: No, Vegan: No, Gluten-Free: No
# Main Street Pizza Company—Vegetarian: Yes, Vegan: No, Gluten-Free: Yes
# Corner Café—Vegetarian: Yes, Vegan: Yes, Gluten-Free: Yes
# Mama’s Fine Italian—Vegetarian: Yes, Vegan: No, Gluten-Free: No
# The Chef’s Kitchen—Vegetarian: Yes, Vegan: Yes, Gluten-Free: Yes
# Write a program that asks whether any members of your party are vegetarian, vegan, or gluten-
# free, to which then displays only the restaurants to which you may take the group.


# restaurants
restaurants = {
    "Joe's Gourmet Burgers": {"Vegetarian": False, "Vegan": False, "Gluten-Free": False},
    "Main Street Pizza Company": {"Vegetarian": True, "Vegan": False, "Gluten-Free": True},
    "Corner Café": {"Vegetarian": True, "Vegan": True, "Gluten-Free": True},
    "Mama's Fine Italian": {"Vegetarian": True, "Vegan": False, "Gluten-Free": False},
    "The Chef's Kitchen": {"Vegetarian": True, "Vegan": True, "Gluten-Free": True}
}

# user input for dietary restrictions
vegetarian = input("Is anyone in your party vegetarian? (yes/no): ")
vegan = input("Is anyone in your party vegan? (yes/no): ")
gluten_free = input("Is anyone in your party gluten-free? (yes/no): ")

# restaurants based on dietary restrictions
suggested_restaurants = []
for restaurant, dietary_info in restaurants.items():
    if not (vegetarian.lower() == "yes" and not dietary_info["Vegetarian"]):
        if not (vegan.lower() == "yes" and not dietary_info["Vegan"]):
            if not (gluten_free.lower() == "yes" and not dietary_info["Gluten-Free"]):
                suggested_restaurants.append(restaurant)

# print the suggested restaurants
if suggested_restaurants:
    print("Here are your restaurant choices:")
    for restaurant in suggested_restaurants:
        print("- " + restaurant)
else:
    print("There are no restaurants that meet all the dietary restrictions of your party.")
