# import libraries
import numpy as np
import pandas as pd
from scipy.stats import binomtest, ttest_1samp

# load data
heart = pd.read_csv("./heart_disease.csv")
yes_hd = heart[heart.heart_disease == "presence"]
no_hd = heart[heart.heart_disease == "absence"]

# get cholesterol levels for patients with heart disease
chol_hd = yes_hd.chol

# calculate mean cholesterol level for patients with hd
print("mean cholesterol level for patients with hd:", np.mean(chol_hd))

# compare to cut-off for high cholesterol

tstat, pval = ttest_1samp(chol_hd, 240)
print(pval / 2)

# get cholesterol levels for patients without heart disease
chold_no_hd = no_hd.chol

# calculate mean cholesterol level for patients wo hd
print("mean cholesterol level for patients wo hd:", np.mean(chold_no_hd))

# compare to cut-off for high cholesterol
tstat, pval = ttest_1samp(chold_no_hd, 240)
print(pval / 2)

# calculate number of patients total
num_patients = len(heart)
print("number of patients total:", num_patients)

# calculate number of patients with fbs > 120
num_highfbs_patients = np.sum(heart.fbs)
print("number of patients with fbs:", num_highfbs_patients)

# calculate 8% of sample size
print(0.08 * num_patients)

# run binomial test
pval = binomtest(int(num_highfbs_patients), num_patients, 0.08, alternative="greater")
print(pval)
