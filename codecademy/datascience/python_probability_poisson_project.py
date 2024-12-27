# Product Defects Project
import scipy.stats as stats
import numpy as np

### Task Group 1 ###
## Task 1: 
lam = 7
## Task 2:
print(stats.poisson.pmf(lam, lam))
## Task 3:
print(stats.poisson.pmf(4, lam))
## Task 4:
print(stats.poisson.pmf(9, lam))

### Task Group 2 ###
## Task 5:
year_defects = stats.poisson.rvs(lam,size=365)
## Task 6:
print(year_defects[:20])
## Task 7:
print(lam*365)
## Task 8:
print(sum(year_defects))
## Task 9:
print(sum(year_defects) / len(year_defects))
## Task 10:
print(max(year_defects))
## Task 11:
print(stats.poisson.pmf(16, lam))

### Extra Bonus ###
# Task 12
print(stats.poisson.ppf(0.9,lam))
# Task 13
myproportion = 0
for deff in year_defects:
  if deff > 10:
    myproportion += 1

print(myproportion / len(year_defects) * 100)
