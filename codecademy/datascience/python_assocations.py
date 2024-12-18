import pandas as pd
import codecademylib3

npi = pd.read_csv("npi_sample.csv")

print(npi.head())

import pandas as pd
import codecademylib3

npi = pd.read_csv("npi_sample.csv")

special_authority_freq = pd.crosstab(npi.special, npi.authority)
print(special_authority_freq)

# Proportions
import pandas as pd
import numpy as np

npi = pd.read_csv("npi_sample.csv")

special_authority_freq = pd.crosstab(npi.special, npi.authority)

# save the table of proportions as special_authority_prop:
special_authority_prop = special_authority_freq / len(npi)

# print out special_authority_prop
print(special_authority_prop)


# Marginals
import pandas as pd
import numpy as np

npi = pd.read_csv("npi_sample.csv")

# save the table of frequencies as special_authority_freq:
special_authority_freq = pd.crosstab(npi.special, npi.authority)

# save the table of proportions as special_authority_prop:
special_authority_prop = special_authority_freq/len(npi)

# calculate and print authority_marginals
authority_marginals = special_authority_prop.sum(axis=0)
print(authority_marginals)

# calculate and print special_marginals
special_marginals =  special_authority_prop.sum(axis=1)
print(special_marginals)
