## Checkpoint 1
expected_baskets = 0.85 * 20
print(expected_baskets)

## Checkpoint 2
expected_late = 0.02  * 180
print(expected_late)


## Checkpoint 1
variance_baskets = 20 * 0.85 * 0.15
print(variance_baskets)

## Checkpoint 2
variance_late = 180 * 0.98 * 0.02
print(variance_late)


import scipy.stats as stats
import numpy as np

## Checkpoint 1
expected_bonus = 0.08 * 75000
print(expected_bonus)

## Checkpoint 2
num_goals = stats.poisson.rvs(4, size=100)


## Checkpoint 3
print(np.var(num_goals))

## Checkpoint 4
num_goals_2 = num_goals * 2
print(np.var(num_goals_2))


