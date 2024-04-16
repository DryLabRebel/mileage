#!/usr/bin/env python
# Python Version of fuel mileage script
# Remember 'ssv' -- SlimeConfig -- Will prompt for new instance of bash, and prompt for open command!!

import pandas as pd
import numpy as np
import argparse
#import summary_functions 
from summary_functions import (
    petrol_L_per_100km, cost_per_km
    )

# How do I import functions??

# Can, I get argparse to take 1 argument? *check*
# Can, I pass that argument to a variable? *check*

parser = argparse.ArgumentParser()
parser.add_argument("--data")
args = parser.parse_args()

#fuel = args.data
#fuel_data = "/Users/geoff/data/auto_mileage_Captiva.txt"
fuel_data = "/Users/geoff/data/auto_mileage_Corolla.txt"
fuel = pd.read_csv(fuel_data, sep="\t")

# Summarize dataset 
# #############################################

print("object type:\n")
print("	",type(fuel))
print("\n")
print("object contents:")
print(fuel)
print("\n")
print("no of records:", len(fuel))
print("\n")
# data.columns[0]

for cols in fuel.columns:
  print(cols, "\t", type(fuel[cols][0]))
  print("\n")

## Be Good if this script ascertained the data types of each column, and then provided a summary of each data type, based on this

## summarise numeric columns

data_summary = fuel.describe()
print(data_summary)

## summarise the store column

print("\nSummary of stores column:","\n") # Could produce a histogram of these values
print(fuel['store'].describe(),"\n")
print("Summary of unique stores values:","\n") # Could produce a histogram of these values
print(fuel['store'].value_counts()) # Could produce a histogram of these values

## summarise the date column

print(fuel['date'].describe())

#tank = petrol_L_calc(fuel)
#mean_tank_distance = mileage_calc(fuel)
fuel_per_100km = petrol_L_per_100km(fuel)
mean_price_per_km = cost_per_km(fuel)

print(
    "\naverage fuel consumed per 100km:", fuel_per_100km,
    "\nAverage price ($) per kilometer:", mean_price_per_km[0],
    "\nAverage price ($) per 100 kilometers:", mean_price_per_km[1]
    )

# BOOM!
# Now what?
# Make it executable
  # Print data summary

# colnames
# datatypes

# Now, I can just wrangle the data

# Create a full package template right from the get go
# coockiecutter
