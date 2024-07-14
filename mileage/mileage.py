#!/usr/bin/env python3
# Python Version of fuel mileage script
# Remember 'ssv' -- SlimeConfig -- Will prompt for new instance of bash, and prompt for open command!!

import summary_functions as sf
from summary_functions import (
    petrol_L_calc,
    petrol_L_per_hundred_km, 
    cost_per_km, 
    cost_per_hundred_km
    )

parser = argparse.ArgumentParser()
parser.add_argument("--data")
args = parser.parse_args()

fuel_data = args.data
fuel = pd.read_csv(fuel_data, sep="\t")
#workingdir = "/Users/geoff/data"
#fuel = pd.read_csv(f"{workingdir}/auto_mileage_Corolla.txt", sep="\t")
#fuel = pd.read_csv(f"{workingdir}/auto_mileage_Captiva.txt", sep="\t")

# Summarize dataset 
# #############################################

#mean_tank_distance = mileage_calc('odometer', fuel)
tank = petrol_L_calc('petrol_L', fuel)
fuel_per_hundred_km = petrol_L_per_hundred_km('petrol_L', 'odometer', fuel)
mean_price_per_km = cost_per_km('cost_perL', 'petrol_L', 'odometer', fuel)
mean_price_per_hundred_km = cost_per_hundred_km('cost_perL', 'petrol_L', 'odometer', fuel)

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

print(
    "\naverage fuel consumed per 100km:", fuel_per_hundred_km,
    "\nAverage price ($) per kilometer:", mean_price_per_km,
    "\nAverage price ($) per 100 kilometers:", mean_price_per_hundred_km
    )

# So what do you want to know when you feed your data in?
    # How many records do I have?
    # How fuel efficient is my vehicle?
    # How expensive is my vehicle to run?
    # How much does it cost to travel a certain distance in my vehicle?

# colnames
# datatypes

# Now, I can just wrangle the data

# Create a full package template right from the get go
# coockiecutter
