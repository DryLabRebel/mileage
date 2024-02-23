#!/usr/bin/env python
# Python Version of fuel mileage script
# Remember 'ssv' -- SlimeConfig -- Will prompt for new instance of bash, and prompt for open command!!

import pandas as pd
import numpy as np
import argparse

# Can, I get argparse to take 1 argument? *check*
# Can, I pass that argument to a variable? *check*

parser = argparse.ArgumentParser()
parser.add_argument("--data")
args = parser.parse_args()

def mileage_report(data):
  """Takes a data set of fuel consumption history, and produces a mileage report.

  A mileage report, including 
    - average liters consumed per 100 kilometers
    - average liters consumed between refills
    - average kilometers travelled per liter
    - average cost in dollars per kilometer (given the date range)

  Parameters
  ----------

  data : Pandas dataframe
    A pandas dataframe containing at minimum the following columns:
      - date: refill date (dd-mm-yy)
      - petrol_L: refill amount (L)
      - cost_perL: fuel price ($/L)
      - total: refill price ($ total)
      - odometer: odometer readings

  Returns
  -------

  A printed summary containing:
  - data object type
  - object contents
  - list of columns and their data type
  - a summary of the listed columns
  """

  # Summarize dataset 
  # #############################################

  print("object type:\n")
  print("	",type(data))
  print("\n")
  print("object contents:")
  print(data)
  print("\n")
  print("no of records:", len(data))
  print("\n")
  # data.columns[0]

  for cols in data.columns:
    print(cols, "\t", type(data[cols][0]))
  print("\n")

  ## summarise numeric columns

  data_summary = data.describe()
  print(data_summary)

  ## summarise the store column

  print("\nSummary of stores column:","\n") # Could produce a histogram of these values
  print(data['store'].describe(),"\n")
  print("Summary of unique stores values:","\n") # Could produce a histogram of these values
  print(data['store'].value_counts()) # Could produce a histogram of these values

  ## summarise the date column

  print(data['date'].describe())

def mileage_calc(data):
  """Calculates mean number of liters
  """
  # TODO: code an iterator which compares consecutive odometer readings
    # any difference between non-null values, which is greater than one sd above sample mean is excluded
      # Track these and record the number of excluded rows
    # then simply (max-min)/(len(odo)+N.excluded)
    # This should *mostly* correct for any missing odometer readings!
    # NOTE: This also assumes you have only small fraction of missing readings (i.e. your sample mean has a small sample standard error)
  # In summary - we simply want to know how many odometer readings have been missed, and add that to len(data)
  odometer_min = data['odometer'].min()
  odometer_max = data['odometer'].max()
  mean_tank = int(round((odometer_max - odometer_min)/len(data), 0))
  return mean_tank

def petrol_L_calc(data):
  # TODO: Ensure this calculation excludes NaN values
  mean_petrol = int(round(data['petrol_L'].mean(),0))
  return mean_petrol

def petrol_L_per_100km(data):
  tank = petrol_L_calc(data)
  distance = mileage_calc(data)
  L_per_100km = (tank/distance)*100
  return L_per_100km

def cost_per_km(data):
  tank = petrol_L_calc(data)
  distance = mileage_calc(data)
  mean_price = int(round(data['cost_perL'].mean(), 0))
  # (L/km)*mean(cost_perL)
  cost_per_km = round((tank/distance)*mean_price, 2)
  cost_per_100km = round(((tank/distance)*mean_price)*100, 2)
  return cost_per_km, cost_per_100km 

fuel_data = args.data
#fuel_data = "/Users/geoff/data/mileage_Captiva.txt"
#fuel_data = "/Users/geoff/data/mileage_Corolla.txt"
fuel = pd.read_csv(fuel_data, sep="\t")

tank = petrol_L_calc(fuel)
distance = mileage_calc(fuel)
L_per_100km = petrol_L_per_100km(fuel)
mean_price_per_km = cost_per_km(fuel)

mileage_report(fuel)

print(
    "\nL per 100km:", L_per_100km,
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

# r1 = round(83/49, 2)
# r2 = round(53/48, 2)
# r3 = round(46/33, 2)
# r4 = round(42/14, 2)
# r5 = round(41/43, 2)
# r6 = round(35/25, 2)
# r7 = round(34/21, 2)
# r8 = round(29/9, 2)
# r9 = round(27/12, 2)
# r10 = round(24/10, 2)
# r11 = round(28/21, 2)
# r12 = round(21/1, 2)
# r13 = round(36/24, 2)
# r14 = round(19/11, 2)
# r15 = round(19/45, 2)
# r16 = round(17/18, 2)
# r17 = round(16/7, 2)
# r18 = round(16/4, 2)
# r19 = round(14/1, 2)
# r20 = round(14/3, 2)
# r21 = round(13/1, 2)
# r22 = round(13/2, 2)
# r23 = round(11/2, 2)
# r24 = round(11/6, 2)
# r25 = round(11/9, 2)
# r26 = round(11/7, 2)
# r27 = round(9/32, 2)
# r28 = round(9/3, 2)
# r29 = round(9/2, 2)
# r30 = round(8/6, 2)
# 
# ractios <- c(r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15, r16, r17, r18, r19, r20, r21, r22, r23, r24, r25, r26, r27, r28, r29, r30)
# 
# as.data.frame(ractios)
