# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 15:50:26 2024

@author: christian.tioye
"""
import requests

r = requests.get('https://api.census.gov/data/2020/acs/acs5?get=NAME,B08303_001E,B08303_013E&for=county:*&in=state:36') 

r_text = r.text
# print(r_text)

r_json = r.json()
#print(r_json)


# Converting JSON to CSV

# From <https://www.codecademy.com/paths/machine-learning-ai-engineering-foundations/tracks/mlef-python-fundamentals-for-ml-ai-engineering-partii/modules/mlef-data-acquisition/lessons/overview-data-acquisition-methods/exercises/converting-json-to-csv> 

import requests
import csv

r = requests.get('https://api.census.gov/data/2020/acs/acs5?get=NAME,B08303_001E,B08303_013E&for=county:*&in=state:36')

r_json = r.json()

with open('commute_data.csv', mode='w', newline='') as file:
  writer = csv.writer(file)
  writer.writerows(r_json)


# Exploring data using pandas

# From <https://www.codecademy.com/paths/machine-learning-ai-engineering-foundations/tracks/mlef-python-fundamentals-for-ml-ai-engineering-partii/modules/mlef-data-acquisition/lessons/overview-data-acquisition-methods/exercises/exploring-data-using-pandas> 


import pandas

commute_df = pandas.read_csv("commute_data.csv")

print(commute_df.head())

commute_df.columns = ['name', 'total_commuters',"commuters_90_plus", 'state', "county"]
print(commute_df.head())
