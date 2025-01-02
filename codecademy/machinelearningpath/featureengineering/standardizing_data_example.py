import pandas as pd
import numpy as np

coffee = pd.read_csv('starbucks_customers.csv')
ages = coffee['age']

## add code below
## set up your variables
mean_age = np.mean(ages)


## standardize ages
std_dev_age = np.std(ages)
ages_standardized = (ages - mean_age) / std_dev_age

## print the results 
print(np.mean(ages_standardized), np.std(ages_standardized))

