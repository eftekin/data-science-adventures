import glob

import matplotlib.pyplot as plt
import pandas as pd

# Using `glob`, loop through the census files available and load them into DataFrames.
files = glob.glob("states*.csv")

states_list = []
for filename in files:
    data = pd.read_csv(filename)
    states_list.append(data)

us_census = pd.concat(states_list)

# Inspect the Data Frame
print("US Census Columns:\n", us_census.columns, "\n")
print("Data Types of DF:\n", us_census.dtypes)
print(us_census.head())

# Use regex to turn the `Income` column into a format that is ready for conversion into a numerical type.
for index in range(0, len(us_census["Income"])):
    string = str(us_census["Income"].iat[index])
    replace_dol = string.replace("$", "")
    replace_com = replace_dol.replace(",", "")
    us_census["Income"].iat[index] = replace_com

us_census["Income"] = pd.to_numeric(us_census["Income"])
print(us_census["Income"])

# GenderPop column into two columns (Men and Women)
print(us_census["GenderPop"].head())

Men = []
Women = []
for index in range(0, len(us_census["GenderPop"])):
    string = str(us_census["GenderPop"].iat[index])
    replace = string.split("_")
    Men.append(replace[0])
    Women.append(replace[1])

us_census["Men"] = Men
us_census["Women"] = Women

print(us_census.head())

# Convert both of the columns (Men and Women) into numerical datatypes.
for index in range(0, len(us_census["Men"])):
    string = str(us_census["Men"].iat[index])
    replace = string.replace("M", "")
    us_census["Men"].iat[index] = replace

for index in range(0, len(us_census["Women"])):
    string = str(us_census["Women"].iat[index])
    replace = string.replace("F", "")
    us_census["Women"].iat[index] = replace

us_census["Men"] = pd.to_numeric(us_census["Men"])
us_census["Women"] = pd.to_numeric(us_census["Women"])

print(us_census.head())


# Scatter Plot of Income
plt.scatter(us_census["Women"], us_census["Income"])
plt.title("Scatter Plot of Income vs. Number of Women per State")
plt.xlabel("Population of Women per State")
plt.ylabel("Income (in US Dollars)")
plt.show()
plt.clf()

print(us_census["Women"])

us_census["Women"] = us_census["Women"].fillna(us_census["TotalPop"] - us_census["Men"])
print(us_census["Women"])

# Drop duplicates

print(us_census.duplicated(subset=us_census.columns[1:]))
census = us_census.drop_duplicates(subset=us_census.columns[1:])
print(census)

# Check the plot
plt.scatter(census["Women"], census["Income"])
plt.title("Scatter Plot of Income vs. Number of Women per State")
plt.xlabel("Population of Women per State")
plt.ylabel("Income (in US Dollars)")
plt.show()
plt.clf()

# Histogram of Races
for race in ["Hispanic", "White", "Black", "Native", "Asian", "Pacific"]:
    for index in range(0, len(us_census)):
        string = str(us_census[race].iat[index])
        replace = string.replace("%", "")
        if replace == "nan":
            replace = ""
        us_census[race].iat[index] = replace
    us_census[race] = pd.to_numeric(us_census[race])

us_census["Pacific"] = us_census["Pacific"].fillna(
    100
    - us_census["Hispanic"]
    - us_census["White"]
    - us_census["Black"]
    - us_census["Native"]
    - us_census["Asian"]
)

census = us_census.drop_duplicates(subset=us_census.columns[1:])
census

for race in ["Hispanic", "White", "Black", "Native", "Asian", "Pacific"]:
    plt.hist(census[race])
    plt.title("Histogram of the Percentage of {} People per State".format(race))
    plt.xlabel("Percentage")
    plt.ylabel("Frequency")
    plt.show()
    plt.clf()
