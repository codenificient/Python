import numpy as np
import pandas as pd
from scipy.stats import pearsonr, chi2_contingency
import matplotlib.pyplot as plt
import seaborn as sns

import codecademylib3
np.set_printoptions(suppress=True, precision = 2)

nba = pd.read_csv('./nba_games.csv')

# Subset Data to 2010 Season, 2014 Season
nba_2010 = nba[nba.year_id == 2010]
nba_2014 = nba[nba.year_id == 2014]

print(nba_2010.head())
print(nba_2014.head())

print(nba.columns)

knicks_pts = nba_2010[nba_2010.fran_id == "Knicks"]
print(knicks_pts)

nets_pts = nba_2010[nba_2010.fran_id == "Nets"]
print(nets_pts)

knicks_avg_pts = knicks_pts.pts.mean()
nets_avg_pts = nets_pts.pts.mean()
diff_pts = knicks_avg_pts - nets_avg_pts
print(diff_pts)

plt.hist(knicks_pts["pts"], alpha=0.4, label='knicks')
plt.hist(nets_pts["pts"], alpha=0.4, label='nets')
plt.legend()
plt.title("2010 Season")
plt.show()

knicks_pts_14 = nba_2014[nba_2014.fran_id == "Knicks"]
print(knicks_pts_14)

nets_pts_14 = nba_2014[nba_2014.fran_id == "Nets"]
print(nets_pts_14)
knicks_avg_pts14 = knicks_pts_14.pts.mean()
nets_avg_pts14 = nets_pts_14.pts.mean()
diff_pts14 = knicks_avg_pts14 - nets_avg_pts14
print(diff_pts14)

plt.hist(knicks_pts_14["pts"], alpha=0.4, label='knicks')
plt.hist(nets_pts_14["pts"], alpha=0.4, label='nets')
plt.legend()
plt.title("2014 Season")
plt.show()

sns.boxplot(x="fran_id",y="pts", data=nba_2010)
plt.show()

location_result_freq = pd.crosstab(nba_2010.game_result, nba_2010.game_location)
print(location_result_freq)

location_result_proportions = location_result_freq / len(nba_2010)
print(location_result_proportions)

# calculate the expected contingency table if there's no association and save it as expected
chi2, pval, dof, expected = chi2_contingency(location_result_freq)

# print out the expected frequency table
print("expected contingency table (no association):", np.round(expected))
print(chi2, pval, dof)

point_diff_forecast_cov = np.cov(nba_2010.forecast, nba_2010.point_diff)
print(point_diff_forecast_cov)

forecast_diff_covariance = point_diff_forecast_cov[0][1]
print(forecast_diff_covariance)

point_diff_forecast_corr = pearsonr(nba_2010.forecast, nba_2010.point_diff)
print(point_diff_forecast_corr)

plt.scatter(nba_2010.forecast, nba_2010.point_diff)
plt.show()


