#!/usr/bin/env python
# Python Version of fuel mileage script

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
  A pandas dataframe containing at a minimum:
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

  # QA dataset
  # #############################################

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

#fuel_data = args.data
fuel_data = "/Users/geoff/data/mileage_Captiva.txt"
fuel = pd.read_csv(fuel_data, sep="\t")

mileage_report(fuel)

# colnames
# datatypes

# BOOM!
# Now what?

# Now, I can just wrangle the data

# Create a full package template right from the get go
# coockiecutter


