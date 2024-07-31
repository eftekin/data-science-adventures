# Load libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import statsmodels.api as sm

# Read in the data
codecademy = pd.read_csv("./codecademy.csv")

# Print the first five rows
print(codecademy.head())

# Create a scatter plot of score vs completed
plt.scatter(codecademy.score, codecademy.completed)

# Show then clear plot
plt.show()
plt.clf()

# Fit a linear regression to predict score based on prior lessons completed
model = sm.OLS.from_formula("score ~ completed", data=codecademy)
results = model.fit()
print(results.params)

# Intercept interpretation:
# A learner who has previously completed 0 content items is expected to earn a quiz score of 13.2 points.

# Slope interpretation:
# Students who have completed one additional prior content item are expected to score 1.3 points higher on the quiz.

# Plot the scatter plot with the line on top
plt.scatter(codecademy.score, codecademy.completed)
plt.plot(codecademy.completed, results.predict(codecademy))

# Show then clear plot
plt.show()
plt.clf()

# Predict score for learner who has completed 20 prior lessons
new_data = {"completed": [20]}
pred20 = results.predict(new_data)
print("predicted score for learner who has completed 20 prior lessons: ", pred20)

# Calculate fitted values
fitted_values = results.predict(codecademy)

# Calculate residuals
residuals = codecademy.score - fitted_values

# Check normality assumption
plt.hist(residuals)
plt.title("normality assumption")

# Show then clear the plot
plt.show()
plt.clf()

# Check homoscedasticity assumption
plt.scatter(fitted_values, residuals)
plt.title("homoscedasticity assumption")

# Show then clear the plot
plt.show()
plt.clf()

# Create a boxplot of score vs lesson
sns.boxplot(x="lesson", y="score", data=codecademy)
plt.title("score vs lesson")

# Show then clear plot
plt.show()
plt.clf

# Fit a linear regression to predict score based on which lesson they took
model = sm.OLS.from_formula("score ~ lesson", codecademy)
results = model.fit()
print(results.params)

# Calculate and print the group means and mean difference (for comparison)
mean_score_lessonA = np.mean(codecademy.score[codecademy.lesson == "Lesson A"])
mean_score_lessonB = np.mean(codecademy.score[codecademy.lesson == "Lesson B"])

print("Mean Score (A):", mean_score_lessonA)
print("Mean Score (B):", mean_score_lessonB)
print("Mean score difference:", mean_score_lessonA - mean_score_lessonB)

# Use `sns.lmplot()` to plot `score` vs. `completed` colored by `lesson`
sns.lmplot(x="completed", y="score", hue="lesson", data=codecademy)
plt.show()
