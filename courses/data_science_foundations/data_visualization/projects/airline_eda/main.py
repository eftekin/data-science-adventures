import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

## Read in Data
flight = pd.read_csv("flight.csv")
print(flight.head())

# What do coach ticket prices look like? What are the high and low values?
# What would be considered the average? Does $500 seem like a good price for a coach ticket?

print(np.mean(flight.coach_price))
print(np.median(flight.coach_price))

sns.histplot(flight.coach_price)
plt.show()
plt.clf()

# Now visualize the coach ticket prices for flights that are 8 hours long.

print(np.mean(flight.coach_price[flight.hours == 8]))
print(np.median(flight.coach_price[flight.hours == 8]))

sns.histplot(flight.coach_price[flight.hours == 8])

plt.show()
plt.clf()

# How are flight delay times distributed?
# Let's say there is a short amount of time between two connecting flights, and a flight delay would put the client at risk of missing their connecting flight.

sns.histplot(flight.delay[flight.delay <= 500])
plt.show()
plt.clf()

# Create a visualization that shows the relationship between coach and first-class prices

perc = 0.1
flight_sub = flight.sample(n=int(flight.shape[0] * perc))

sns.lmplot(
    x="coach_price",
    y="firstclass_price",
    data=flight_sub,
    line_kws={"color": "black"},
    lowess=True,
)
plt.show()
plt.clf()

# What is the relationship between coach prices and inflight features - inflight meal, inflight entertainment, and inflight WiFi?
# Which features are associated with the highest increase in price?

# Inflight Meals
sns.histplot(flight, x="coach_price", hue=flight.inflight_meal)
plt.show()
plt.clf()

# Inflight Entertainment
sns.histplot(flight, x="coach_price", hue=flight.inflight_entertainment)
plt.show()
plt.clf()

# Inflight WiFi
sns.histplot(flight, x="coach_price", hue=flight.inflight_wifi)
plt.show()
plt.clf()

# How does the number of passengers change in relation to the length of flights?

sns.lmplot(
    x="hours",
    y="passengers",
    data=flight_sub,
    x_jitter=0.25,
    scatter_kws={"s": 5, "alpha": 0.2},
    fit_reg=False,
)
plt.show()
plt.clf()


# Visualize the relationship between coach and first-class prices on weekends compared to weekdays.

sns.lmplot(
    x="coach_price", y="firstclass_price", hue="weekend", data=flight_sub, fit_reg=False
)
plt.show()
plt.clf()


# How do coach prices differ for redeyes and non-redeyes on each day of the week?

sns.boxplot(x="day_of_week", y="coach_price", hue="redeye", data=flight)
plt.show()
plt.clf()
