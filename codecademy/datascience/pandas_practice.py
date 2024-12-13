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

import codecademylib3
import pandas as pd

inventory = pd.read_csv("inventory.csv")
print(inventory.head(10))

staten_island = inventory[inventory.location == "Staten Island"]

product_request = staten_island["product_description"]

seed_request = inventory[(inventory.location == "Brooklyn") & (inventory.product_type == "seeds")]

inventory["in_stock"] = inventory["quantity"] > 0

# print(inventory)
inventory["total_value"] = inventory["quantity"] * inventory["price"]
# print(inventory)
combine_lambda = lambda row: \
    '{} - {}'.format(row.product_type,
                     row.product_description)

inventory["full_description"] = inventory.apply(combine_lambda, axis=1)

import codecademylib3
import pandas as pd

orders = pd.read_csv('orders.csv')
print(orders.head(10))

most_expensive = orders.price.max()
num_colors = orders.shoe_color.nunique()

import codecademylib3
import pandas as pd

orders = pd.read_csv('orders.csv')
pricey_shoes = orders.groupby("shoe_type").price.max()
print(pricey_shoes)

print(type(pricey_shoes))

import codecademylib3
import pandas as pd

orders = pd.read_csv('orders.csv')

pricey_shoes = orders.groupby('shoe_type').price.max()
pricey_shoes = orders.reset_index()
print(pricey_shoes)
print(type(pricey_shoes))

import codecademylib3
import numpy as np
import pandas as pd

orders = pd.read_csv('orders.csv')
cheap_shoes = orders.groupby("shoe_color").price.apply(lambda x: np.percentile(x,25)).reset_index()
print(cheap_shoes)


import codecademylib3
import numpy as np
import pandas as pd

orders = pd.read_csv('orders.csv')
shoe_counts = orders.groupby(["shoe_type", "shoe_color"]).id.count().reset_index()
print(shoe_counts)

import codecademylib3
import numpy as np
import pandas as pd

orders = pd.read_csv('orders.csv')

shoe_counts = orders.groupby(['shoe_type', 'shoe_color']).id.count().reset_index()

shoe_counts_pivot = shoe_counts.pivot(columns="shoe_color", index="shoe_type", values="id").reset_index()
# print(shoe_counts)
print(shoe_counts_pivot)

import codecademylib3
import pandas as pd

user_visits = pd.read_csv('page_visits.csv')

print(user_visits.head())

click_source = user_visits.groupby("utm_source").id.count().reset_index()
print(click_source)

click_source_by_month = user_visits.groupby(["utm_source", "month"]).id.count().reset_index()

click_source_by_month_pivot = click_source_by_month.pivot(columns="month", index="utm_source", values="id").reset_index()
print(click_source_by_month_pivot)



import codecademylib3
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')
print(ad_clicks.head())

click_source = ad_clicks.groupby("utm_source").user_id.count().reset_index()
# print(click_source)

ad_clicks["is_click"] = ~ad_clicks["ad_click_timestamp"].isnull()
# print(ad_clicks)

clicks_by_source = ad_clicks.groupby(["utm_source", "is_click"]).user_id.count().reset_index()
# print(clicks_by_source)

clicks_pivot = clicks_by_source.pivot(columns="is_click", index="utm_source", values="user_id").reset_index()
# print(clicks_pivot)

clicks_pivot["percent_clicked"] = clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False])
# print(clicks_pivot)

adgroups = ad_clicks.groupby("experimental_group").user_id.count().reset_index()
# print(adgroups)

ads_clicks_groups = ad_clicks.groupby(["experimental_group", "is_click"]).user_id.count().reset_index()
# print(ads_clicks_groups)

a_clicks = ad_clicks[ad_clicks.experimental_group == "A"]
b_clicks = ad_clicks[ad_clicks.experimental_group == "B"]
print(a_clicks)
print(b_clicks)

a_clicks_by_day = a_clicks.groupby("day").user_id.count().reset_index()
b_clicks_by_day = b_clicks.groupby("day").user_id.count().reset_index()
# print(a_clicks_by_day)
# print(b_clicks_by_day)


# Does not work
import codecademylib3
import pandas as pd

orders = pd.read_csv('orders.csv')

products = pd.read_csv('products.csv')

customers = pd.read_csv('customers.csv')

print(orders)
print(products)
# print(customers)

current_order = orders[orders.order_id == 3]
# print(current_order)

order_3_description = products[products["product_id"] == current_order["product_id"]]
print(order_3_description)


import codecademylib3
import pandas as pd

sales = pd.read_csv('sales.csv')
print(sales)
targets = pd.read_csv('targets.csv')
print(targets)

sales_vs_targets = pd.merge(sales,targets)
print(sales_vs_targets)

crushing_it = sales_vs_targets[sales_vs_targets["revenue"] > sales_vs_targets["target"]]


import codecademylib3
import pandas as pd

sales = pd.read_csv('sales.csv')
print(sales)
targets = pd.read_csv('targets.csv')
print(targets)

men_women = pd.read_csv("men_women_sales.csv")
all_data = sales.merge(targets).merge(men_women)
print(all_data)

results = all_data[(all_data.revenue > all_data.target) & (all_data.women > all_data.men) ]
print(results)



import codecademylib3
import pandas as pd

orders = pd.read_csv('orders.csv')
print(orders)
products = pd.read_csv('products.csv')
print(products)

orders_products = orders.merge(products.rename(columns={"id": "product_id"}))

print(orders_products)
