import codecademylib3
import pandas as pd
import numpy as np

# code goes here
diabetes = pd.read_csv("diabetes.csv")
print(diabetes.head())

print(diabetes.info())

# print number of columns
print(len(diabetes.columns))

# print number of rows
print(len(diabetes))


# Checking for missing values using isnull()
print(diabetes.isnull().any())

# Count missing values
missing_value_count = diabetes.isna().sum() 

print(missing_value_count)

# perform summary statistics
print(diabetes.describe())

"""
`The zero values do not make sense for Glucose, BloodPressure, SkinThickness, Insulin or BMI. There is surely some missing values which were converted or encoded to 0.0`
"""

"""
`BMI of 67 is too high and 17 pregnancies seem to high as well. I am not well-versed in the normal range for the other variables`
"""

# replace instances of 0 with NaN
diabetes[['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']] = diabetes[['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']].replace(0, np.NaN)

# find whether columns contain null values after replacements are made
print(diabetes.isnull().any())


# Count missing values
missing_value_count = diabetes.isna().sum() 

print(missing_value_count)

# print rows with missing values
print(diabetes[diabetes.isnull().any(axis=1)])

# print data types using .info() method
print(diabetes.info())

# print unique values of Outcome column
print(diabetes.Outcome.unique())

# First replace all O's with zeros
diabetes["Outcome"] = diabetes.Outcome.replace("O", 0)

# Then convert the data type
diabetes["Outcome"] = diabetes.Outcome.astype("int")

print(diabetes.Outcome.unique())




"""
`After replacing the letter o with zeros, we are able to convert the column to the integer data type`
"""
