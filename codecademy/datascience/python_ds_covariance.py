import pandas as pd
import matplotlib.pyplot as plt 
import codecademylib3

housing = pd.read_csv('housing_sample.csv')

print(housing.head())

#create your scatter plot here:
plt.scatter(x=housing.beds, y = housing.sqfeet)
plt.show()


plt.show()

# Covariance
import numpy as np
import pandas as pd
np.set_printoptions(suppress=True, precision = 1) 

housing = pd.read_csv('housing_sample.csv')

# calculate and print covariance matrix:
cov_mat_sqfeet_beds = np.cov(housing.sqfeet, housing.beds)
print(cov_mat_sqfeet_beds)

# store the covariance as cov_sqfeet_beds
cov_sqfeet_beds = cov_mat_sqfeet_beds[0][1]
print(cov_sqfeet_beds)

import pandas as pd
import matplotlib.pyplot as plt 
import codecademylib3
from scipy.stats import pearsonr

housing = pd.read_csv('housing_sample.csv')

# calculate corr_sqfeet_beds and print it out:
corr_sqfeet_beds, p = pearsonr(housing.beds, housing.sqfeet)
print(corr_sqfeet_beds)

# create the scatter plot here:
plt.xlabel('Number of beds')
plt.ylabel('Number of sqfeet')
plt.scatter(x=housing.beds, y=housing.sqfeet)
plt.show()

# Correlation p2
import pandas as pd
import matplotlib.pyplot as plt 
import codecademylib3
from scipy.stats import pearsonr

sleep = pd.read_csv('sleep_performance.csv')

# create your scatter plot here:
print(sleep.head())

plt.scatter(x=sleep.hours_sleep,y=sleep.performance)
plt.show()


# calculate the correlation for `hours_sleep` and `performance`:
corr_sleep_performance, p = pearsonr(sleep.hours_sleep, sleep.performance)


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import codecademylib3
from scipy.stats import pearsonr
np.set_printoptions(suppress=True, precision = 1) 

penguins = pd.read_csv('penguins.csv')


