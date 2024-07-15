import pandas as pd
from helper_functions import (
    choose_statistic,
    population_distribution,
    sampling_distribution,
)
from scipy import stats

# load in spotify_data.csv into a variable
spotify_data = pd.read_csv("csv/spotify_data.csv")

# preview the dataset
print(spotify_data.head())

# select the relevant column
song_tempos = spotify_data.tempo

# plot the population distribution with the mean labeled
population_distribution(song_tempos)

# sampling distribution of the sample mean
sampling_distribution(song_tempos, 30, "Mean")

# sampling distribution of the sample minimum
sampling_distribution(song_tempos, 30, "Minimum")

# sampling distribution of the sample variance
sampling_distribution(song_tempos, 30, "Variance")

# calculate the population mean and standard deviation
population_mean = choose_statistic(song_tempos, "Mean")
population_std = choose_statistic(song_tempos, "Std")

# calculate the standard error
standart_error = population_std / (30**0.5)

# calculate the probability of observing an average tempo of 140bpm or lower from a sample of 30 songs
print(stats.norm.cdf(140, population_mean, standart_error))

# calculate the probability of observing an average tempo of 150bpm or higher from a sample of 30 songs
print(1 - stats.norm.cdf(150, population_mean, standart_error))
