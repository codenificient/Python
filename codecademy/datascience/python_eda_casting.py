import codecademylib3

# Import pandas with alias
import pandas as pd

# Import dataset as a Pandas dataframe
movies = pd.read_csv("netflix_movies.csv")

# View the first five rows of the dataframe
print(movies.head())

# Print the data types
print(movies.dtypes)

# Fill in the missing cast_count values with 0
movies['cast_count'].fillna(0, inplace = True)

# Change the type of the cast_count column
movies["cast_count"] = movies["cast_count"].astype("int64")

# Check the data types of the columns again. 
print(movies.dtypes)


import codecademylib3

# Import pandas with alias
import pandas as pd

# Import dataset as a Pandas dataframe
movies = pd.read_csv("netflix_movies.csv")

# View the first five rows of the dataframe
print(movies.head())

# Print the data types of dataframe 
print(movies.dtypes)

# Add the variables you plan to change to this list
change = ['title', "rating", "country"]

# Change the title variable to a "string"
movies["title"] = movies["title"].astype("string")

# Change any other variables
movies["rating"] = movies["rating"].astype("string")
movies["country"] = movies["country"].astype("string")

# Print the data types again
print(movies.dtypes)


import codecademylib3

# Import pandas with alias
import pandas as pd

# Import dataset as a Pandas Dataframe
movies = pd.read_csv('netflix_movies.csv')

# View the first five rows of the dataframe
print(movies.head())

# Print the unique values of the rating column
print(movies['rating'].unique())

# Change the data type of `rating` to category
movies["rating"] = pd.Categorical(movies["rating"], ["NR", "G", "PG", "PG-13", "R"])

# Recheck the values of `rating` with .unique()
print(movies['rating'].unique())


import codecademylib3

# Import pandas with alias
import pandas as pd

# Import dataset as a Pandas Dataframe
cereal = pd.read_csv('cereal.csv', index_col=0)

# Show the first five rows of the `cereal` dataframe
print(cereal.head())

# Create a new dataframe with the `mfr` variable One-Hot Encoded
cereal = pd.get_dummies(data=cereal, columns=["mfr"])

# Show first five rows of new dataframe
print(cereal.head())



######### Practice Problem  #################
import codecademylib3

# Import pandas with alias
import pandas as pd

# Import dataset as a Pandas Dataframe
auto = pd.read_csv('autos.csv', index_col=0)

# Print the first 10 rows of the auto dataset
print(auto.head(10))

# Print the data types of the auto dataframe
print(auto.dtypes)

# Change the data type of price to float
auto["price"] = auto["price"].astype("float64")

# Set the engine_size data type to category
print(auto['engine_size'].unique())
auto["engine_size"] = pd.Categorical(auto["engine_size"], ["small", "medium", "large"], ordered=True)

# Create the engine_codes variable by encoding engine_size
auto['engine_codes'] = auto['engine_size'].cat.codes
print(auto.head())


# One-Hot Encode the body-style variable
auto = pd.get_dummies(data=auto, columns=["body-style"])


################# CENSUS DATA #############################

import codecademylib3

# Import pandas with alias
import pandas as pd

# Read in the census dataframe
census = pd.read_csv('census_data.csv', index_col=0)

print(census.head())
print(census.dtypes)
print(census.birth_year.unique())

census["birth_year"] = census["birth_year"].replace("missing", 1967)
print(census.birth_year.unique())

census["birth_year"] = census["birth_year"].astype("int")
print(census.dtypes)
print(census.birth_year.mean())

census["higher_tax"] = pd.Categorical(census["higher_tax"], ["strongly disagree", "disagree", "neutral", "agree", "strongly agree"], ordered=True)
print(census.higher_tax.unique())

census["higher_tax"] = census["higher_tax"].cat.codes
print(census['higher_tax'].median()) 

census = pd.get_dummies(data=census, columns=["marital_status"])
print(census.head())