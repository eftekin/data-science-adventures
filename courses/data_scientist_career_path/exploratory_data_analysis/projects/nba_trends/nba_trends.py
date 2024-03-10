import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy.stats import chi2_contingency, pearsonr

np.set_printoptions(suppress=True, precision=2)

nba = pd.read_csv("./nba_games.csv")
print(nba.head())

nba_2010 = nba[nba.year_id == 2010]
nba_2014 = nba[nba.year_id == 2014]

knicks_pts = nba_2010[nba_2010.fran_id == "Knicks"]["pts"]
nets_pts = nba_2010[nba_2010.fran_id == "Nets"]["pts"]

diff_means_2010 = knicks_pts.mean() - nets_pts.mean()  # output: 9.73

# compare the points scored for the Knicks compared to the Nets
plt.hist(knicks_pts, color="blue", label="knicks", density=True, alpha=0.5)
plt.hist(nets_pts, color="red", label="nets", density=True, alpha=0.5)
plt.title("2010 Season")
plt.legend()
plt.show()

knicks_pts_2014 = nba_2014[nba_2014.fran_id == "Knicks"]["pts"]
nets_pts_2014 = nba_2014[nba_2014.fran_id == "Nets"]["pts"]

diff_means_2014 = knicks_pts_2014.mean() - nets_pts_2014.mean()  # output: 0.44

plt.clf()
sns.boxplot(data=nba_2010, x="fran_id", y="pts")
plt.show()


location_result_freq = pd.crosstab(nba_2010.game_result, nba_2010.game_location)
# 133  105
# 92  120

location_result_proportions = location_result_freq / len(nba_2010)
# 0.295556  0.233333
# 0.204444  0.266667

chi2, pval, dof, expected = chi2_contingency(location_result_freq)
print(expected)
# [119. 119.]
# [106. 106.]
print(chi2)
# 6.501704455367053

np.set_printoptions(suppress=True, precision=1)
point_diff_forecast_cov = np.cov(nba_2010.forecast, nba_2010.point_diff)
# [  0.1   1.4]
# [  1.4 186.6]

point_diff_forecast_corr = pearsonr(nba_2010.forecast, nba_2010.point_diff)
# PearsonRResult(statistic=0.44020887084680854, pvalue=9.410391573138663e-23)

plt.clf()
plt.scatter(x="forecast", y="point_diff", data=nba_2010)
plt.xlabel("Forecasted Win Prob.")
plt.ylabel("Point Differential")
plt.show()
