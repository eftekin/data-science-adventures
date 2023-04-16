# Create a sample dictionary

release_year_dict = {"Thriller": "1982", "Back in Black": "1980", \
                    "The Dark Side of the Moon": "1973", "The Bodyguard": "1992", \
                    "Bat Out of Hell": "1977", "Their Greatest Hits (1971-1975)": "1976", \
                    "Saturday Night Fever": "1977", "Rumours": "1977"}

# Get value by keys
print(release_year_dict["Thriller"])

# Get all the keys
print(release_year_dict.keys())

# Get all the values
print(release_year_dict.values())

# Append value into dictionary
release_year_dict["Graduation"] = "2007"
print(release_year_dict)

# Delete entries
del(release_year_dict["Thriller"])
del(release_year_dict["Graduation"])

print(release_year_dict)

# Verify the key
print("The Bodyguard"  in release_year_dict)


