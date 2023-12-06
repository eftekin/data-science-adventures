# sample set

cities = set(["London", "Istanbul", "Amsterdam"])
print(cities)

# add element to set
cities.add("Milano")
print(cities)

# try to duplicate element to the set
cities.add("Milano")
print(cities)

# remove element from set
cities.remove("Istanbul")
print(cities)

# verify if the element is in the set
print("Istanbul" in cities)
print("Milano" in cities)

# ------------------------
# sets logic operations
# ------------------------

albumSet1 = {"Thriller", "AC/DC", "Back in Black"}
albumSet2 = {"Thriller", "Back in Black", "The Dark Side of the Moon"}

print(albumSet1, albumSet2)

# find the intersections
intersection = albumSet1 & albumSet2
print("The intersection of sets:", intersection)
# another method
print(albumSet1.intersection(albumSet2))

# find the difference in set1 but not set2
print(albumSet1.difference(albumSet2))
print(albumSet2.difference(albumSet1))

# find the union of two sets
print("The union of two sets",albumSet1.union(albumSet2))

# check if superset
print(set(albumSet1).issuperset(albumSet2))

# check if subset
print(set(albumSet2).issubset(albumSet1))