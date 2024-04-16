#!/usr/bin/env python
# Python Version of fuel mileage script
# Remember 'ssv' -- SlimeConfig -- Will prompt for new instance of bash, and prompt for open command!!

import pandas as pd
import numpy as np
import argparse

# Summary functions for mileage calculator

def mileage_calc(data):
  """Calculates mean number of liters
  """
  odometer_min = data['odometer'].min()
  odometer_max = data['odometer'].max()
  mean_tank = int(round((odometer_max - odometer_min)/len(data), 0))
  return mean_tank

def petrol_L_calc(data):
    # TODO: Ensure this calculation excludes NaN values
    mean_petrol = int(round(data['petrol_L'].mean(),0))
    return mean_petrol

def petrol_L_per_hundred_km(data):
    tank = petrol_L_calc(data)
    distance = mileage_calc(data)
    L_per_hundred_km = round((tank/distance)*100, 2)
    return L_per_hundred_km

def cost_per_km(data):
    tank = petrol_L_calc(data)
    distance = mileage_calc(data)
    mean_price = int(round(data['cost_perL'].mean(), 0))
    cost_per_km = round((tank/distance)*mean_price, 2)
    return cost_per_km

def cost_per_hundred_km(data):
    tank = petrol_L_calc(data)
    distance = mileage_calc(data)
    mean_price = int(round(data['cost_perL'].mean(), 0))
    cost_per_hundred_km = round(((tank/distance)*mean_price)*100, 2)
    return cost_per_hundred_km 
