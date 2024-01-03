import pandas as pd
import numpy as np

diabetes = pd.read_csv("./diabetes.csv")
print(diabetes.head())

print(diabetes.info())
# 9 columns 768 rows

print(diabetes.describe())

# replace instances of 0 with NaN
diabetes[["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]] = diabetes[
    ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]
].replace(0, np.NaN)

print(diabetes.isnull().sum())

# Print out all of the rows that contain missing (null) values.

print(diabetes[diabetes.isnull().any(axis=1)])

print(diabetes.info())

# print unique values of Outcome column
print(diabetes.Outcome.unique())

diabetes["Outcome"] = diabetes["Outcome"].replace("O", 0)
diabetes["Outcome"] = diabetes["Outcome"].astype(int)
print(diabetes.Outcome.unique())

print(diabetes.info())

print(diabetes.value_counts())

# TO-DO: Instead of changing the 0 values in the five columns to NaN, try replacing the values with the median or mean of each column.
