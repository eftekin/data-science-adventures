import pandas as pd

x = {"Name": ["Mustafa", "Mehmet", "Arda", "Dila", "Baki"],
     "ID": [1, 2, 3, 4, 5],
     "Department": ["Software Group", "Infrastructure", "Architect Group", "Design Team", "Pharmacy"],
     "Salary": [1000000, 90000, 50000, 80000, 85000]}

# casting the dictionary to a DataFrame
df = pd.DataFrame(x)

# display the result of df
print(df)

# retrieving the "ID" column
y = df[["ID"]]
print(y)

# check the type of x
print(type(x))

# Retrieving the Department, Salary and ID columns and assigning it to a variable z
z = df[["Department", "Salary", "ID"]]
print(z)

################################
#  loc() and iloc() functions
################################

# Access the value on the first row and the first column
print(df.iloc[0, 0])

# Access the value on the first row and the third column
print(df.iloc[0, 2])

# Access the column using the name
print(df.loc[0, "Salary"])

df2 = df
df2 = df2.set_index("Name")
# To display the first 5 rows of new dataframe
df2.head()
print(df2.loc["Mustafa", "Salary"])

################################
#           Slicing
###############################

# let us do the slicing using old dataframe df
print(df.iloc[0:2, 0:3])

# let us do the slicing using loc() function on old dataframe df where index column is having labels as 0,1,2
print(df.loc[0:2, "ID":"Department"])

# let us do the slicing using loc() function on new dataframe df2 where index column is Name having labels: Mustafa, Mehmet, Arda
print(df2.loc["Mustafa":"Arda", "ID":"Department"])

# exercise

print(df.loc[2:3, "Name":"Department"])
