import pandas as pd 

coffee = pd.read_csv("starbucks_customers.csv")

print(coffee.columns)

print(coffee.info())

