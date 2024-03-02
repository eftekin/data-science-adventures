# Load libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import data
students = pd.read_csv("./students.csv")

# Print first few rows of data
print(students.head())

# Print summary statistics for all columns
print(students.describe(include="all"))

# Calculate mean
print(students.math_grade.mean())

# Calculate median
print(students.math_grade.median())

# Calculate mode
print(students.math_grade.mode()[0])

# Calculate range
print(students.math_grade.max() - students.math_grade.min())

# Calculate standard deviation
print(students.math_grade.std())

# Create a histogram of math grades
sns.histplot(x="math_grade", data=students)

plt.show()
plt.clf()

# Create a box plot of math grades
sns.boxplot(x="math_grade", data=students)

plt.show()
plt.clf()

# Calculate number of students with mothers in each job category
print(students["Mjob"].value_counts())

# Calculate proportion of students with mothers in each job category
print(students["Mjob"].value_counts(normalize="True"))

# Create bar chart of Mjob
sns.countplot(x="Mjob", data=students)

plt.show()
plt.clf()

# Create pie chart of Mjob
students["Mjob"].value_counts().plot.pie()

plt.show()
