import scipy.stats as stats

## Checkpoint 1
# calculate prob_15
prob_15 = stats.poisson.pmf(15, 15)

# print prob_15
print(prob_15)

## Checkpoint 
# calculate prob_7_to_9
prob_7_to_9 = stats.poisson.pmf(9,15) + stats.poisson.pmf(8,15) + stats.poisson.pmf(7,15)

# print prob_7_to_9
print(prob_7_to_9)


##### Poisson Distribution
import scipy.stats as stats

## Checkpoint 1
# calculate prob_more_than_20
prob_more_than_20 = 1-stats.poisson.cdf(20,15)

# print prob_more_than_20
print(prob_more_than_20)

## Checkpoint 
# calculate prob_17_to_21
prob_17_to_21 = stats.poisson.cdf(21,15) - stats.poisson.cdf(16,15)

# print prob_17_to_21
print(prob_17_to_21)
