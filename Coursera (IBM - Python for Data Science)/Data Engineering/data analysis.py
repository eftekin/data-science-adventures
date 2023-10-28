import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/diabetes.csv"
df = pd.read_csv(path)

# show the first 5 rows using dataframe.head() method
print("The first 5 rows of the dataframe")
print(df.head(5))

print("dimension:")
print(df.shape)

print("info about dataframe")
print(df.info())
print(df.describe())

# Identify and handle missing values
missing_data = df.isnull()
missing_data.head(5)

# Count missing values in each column
for column in missing_data.columns.values.tolist():
    print(column)
    print(missing_data[column].value_counts())
    print("")

# Correct data format
print(df.dtypes)

# Visualization

labels = "Diabetic", "Not Diabetic"
plt.pie(df['Outcome'].value_counts(), labels=labels, autopct='%0.02f%%')
plt.legend()
plt.show()
