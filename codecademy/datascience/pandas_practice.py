import codecademylib3
import pandas as pd

orders = pd.read_csv("shoefly.csv")

print(orders.head())

emails = orders["email"]

frances_palmer = orders[orders.first_name == "Frances"]
print(frances_palmer)

comfy_shoes = orders[(orders.shoe_type == "clogs") | (orders.shoe_type == "boots") | (orders.shoe_type == "ballet flats")]

import codecademylib3
import pandas as pd

df = pd.DataFrame([
  [1, '3 inch screw', 0.5, 0.75],
  [2, '2 inch nail', 0.10, 0.25],
  [3, 'hammer', 3.00, 5.50],
  [4, 'screwdriver', 2.50, 3.00]
],
  columns=['Product ID', 'Description', 'Cost to Manufacture', 'Price']
)

# Add columns here
df["Sold in Bulk?"] = ["Yes", "Yes", "No", "No"]
print(df)


import codecademylib3
import pandas as pd

df = pd.DataFrame([
  [1, '3 inch screw', 0.5, 0.75],
  [2, '2 inch nail', 0.10, 0.25],
  [3, 'hammer', 3.00, 5.50],
  [4, 'screwdriver', 2.50, 3.00]
],
  columns=['Product ID', 'Description', 'Cost to Manufacture', 'Price']
)

# Add columns here
df["Is taxed?"] = ["Yes", "Yes", "Yes", "Yes"]
print(df)

import codecademylib3
import pandas as pd

df = pd.DataFrame([
  [1, '3 inch screw', 0.5, 0.75],
  [2, '2 inch nail', 0.10, 0.25],
  [3, 'hammer', 3.00, 5.50],
  [4, 'screwdriver', 2.50, 3.00]
],
  columns=['Product ID', 'Description', 'Cost to Manufacture', 'Price']
)

# Add column here
df["Margin"] = df.Price - df['Cost to Manufacture'] 
print(df)

import codecademylib3
import pandas as pd

df = pd.DataFrame([
  [1, '3 inch screw', 0.5, 0.75],
  [2, '2 inch nail', 0.10, 0.25],
  [3, 'hammer', 3.00, 5.50],
  [4, 'screwdriver', 2.50, 3.00]
],
  columns=['Product ID', 'Description', 'Cost to Manufacture', 'Price']
)

# Add column here
df["Margin"] = df.Price - df['Cost to Manufacture'] 
print(df)

import codecademylib3
import pandas as pd

df = pd.DataFrame([
  ['JOHN SMITH', 'john.smith@gmail.com'],
  ['Jane Doe', 'jdoe@yahoo.com'],
  ['joe schmo', 'joeschmo@hotmail.com']
],
columns=['Name', 'Email'])

# Add columns here
df["Lowercase Name"] = df.Name.apply(str.lower)
print(df)

mylambda = lambda strng: strng[0] + strng[-1]


import codecademylib3

mylambda = lambda age: "Welcome to BattleCity!" if age >= 13 else "You must be 13 or older"

import codecademylib3
import pandas as pd

df = pd.read_csv('employees.csv')

# Add columns here
get_last_name = lambda strng: strng.split()[-1]
print(df)

df["last_name"] = df.name.apply(get_last_name)

import codecademylib3
import pandas as pd

df = pd.read_csv('employees.csv')

total_earned = lambda row: (40 * row["hourly_wage"]) + ((row["hours_worked"] - 40) * row["hourly_wage"] * 1.5) if row["hours_worked"] > 40 else row["hours_worked"] * row["hourly_wage"]

df["total_earned"] = df.apply(total_earned,axis=1)

import codecademylib3
import pandas as pd

df = pd.read_csv('imdb.csv')

# Rename columns here
df.columns = ["ID", "Title", "Category", "Year Released", "Rating"]
print(df)


import codecademylib3
import pandas as pd

df = pd.read_csv('imdb.csv')

# Rename columns here
df.rename(columns={
  "name": "movie_title"
}, inplace=True)
print(df)

import codecademylib3
import pandas as pd

orders = pd.read_csv('shoefly.csv')

print(orders.head())

mylambda = lambda x: "animal" if x == "leather" else "vegan"

orders["shoe_source"] = orders.shoe_material.apply(mylambda)

salulambda = lambda row: "Dear Mr. " + row["last_name"] if row["gender"] == "male" else "Dear Ms. " + row["last_name"]

orders["salutation"] = orders.apply(salulambda,axis=1)

print(orders.head())

