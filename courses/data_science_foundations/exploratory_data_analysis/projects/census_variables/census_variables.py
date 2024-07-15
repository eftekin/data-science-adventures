import pandas as pd

census = pd.read_csv("./census_data.csv", index_col=0)
# print(census.head())
# print(census.dtypes)

census["birth_year"] = census["birth_year"].replace(["missing"], 1967)
# print(census["birth_year"].unique())

census["birth_year"] = census["birth_year"].astype(int)
print(census.dtypes)

print("The average birth year: " + str(census["birth_year"].mean()))

census["higher_tax"] = pd.Categorical(
    census["higher_tax"],
    ["strongly disagree", "disagree", "neutral", "agree", "strongly agree"],
    ordered=True,
)
print(census["higher_tax"].unique())

census["higher_tax"] = census["higher_tax"].cat.codes
print(census["higher_tax"].median())

census_1 = pd.get_dummies(census, columns=["marital_status"])
print(census_1.head())

census["marital_status"] = pd.Categorical(
    census["marital_status"],
    ["single", "divorced", "married", "widowed"],
    ordered=False,
)
print(census.head())
census["marital_status"] = census["marital_status"].cat.codes
print(census.head())
