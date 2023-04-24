animalList = ["cat", "dog", "bird", "turtle", "penguin", "crocodile"]

longest = ""
for word in animalList:
    if len(word) > len(longest):
        longest = word

# print the result
print("The longest word in the list is:", longest)
