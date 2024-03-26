import numpy as np  # noqa: F401
import scipy.stats as stats

# the rate parameter of distribution
lam = 7

# the probability of observing exactly lam defects on a given day.
print(stats.poisson.pmf(lam, lam))

# our boss said that having 4 or fewer defects on a given day is an exceptionally good day. You are curious about how often that might happen.
print(stats.poisson.cdf(4, lam))

# n the other hand, our boss said that having more than 9 defects on any given day is considered a bad day.
print(1 - stats.poisson.cdf(9, lam))

year_defects = stats.poisson.rvs(lam, size=365)
print(year_defects[:20])

# if we expect 7 defects on a given day, what is the total number of defects we would expect over 365 days
print(lam * 365)

# calculate and print the total sum of the dataset `year_defects`
print(sum(year_defects))

# calculate and print the average number of defects per day from our simulated dataset.
print(np.mean(year_defects))

# print the maximum value of `year_defects`.
print(year_defects.max())

# calculate and print the probability of observing that maximum value or more from the Poisson(7) distribution.
print(1 - stats.poisson.cdf(year_defects.max(), lam))
