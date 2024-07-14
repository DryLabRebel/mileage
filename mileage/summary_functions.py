#!/usr/bin/env python
# Python Version of fuel mileage script
# Remember 'ssv' -- SlimeConfig -- Will prompt for new instance of bash, and prompt for open command!!

# Summary functions for mileage calculator

# Ah... I could add a function, which accepts the date range, and simply filters data according to those dates, and returns a dataset which can be filtered into the other functions
# In the calling script, I can check to determine if dates have been supplied, and if not, then just feed the data straight into the report as-is, otherwise filter according to the provided data

def mileage_calc(odometer, data):
  """Calculates average distance (kilometers) travelled between refills
  """
  odo = data[odometer]
  odometer_min = odo.min()
  odometer_max = odo.max()
  refills = len(data)
  mean_tank = int( round( (odometer_max - odometer_min)/refills, 0))
  return mean_tank

def petrol_L_calc(fill_L, data):
  """Calculates the average fuel consumption (liters) between refills
  """
  mean_petrol = int(round(data[fill_L].mean(),0))
  return mean_petrol

def petrol_L_per_hundred_km(fill_L, odometer, data):
  """Calculates the average petrol consumed (liters) per 100 kilometers travelled
  """
  tank = petrol_L_calc(fill_L, data)
  distance = mileage_calc(odometer, data)
  L_per_hundred_km = round((tank/distance)*100, 2)
  return L_per_hundred_km

# Cool... now I need to modify the rest to suit...

def cost_per_km(price, fill_L, odometer, data):
  """Calculates the average cost of petrol per 100 kilometers travelled
  """
  tank = petrol_L_calc(fill_L, data)
  distance = mileage_calc(odometer, data)
  mean_price = int(round(data[price].mean(), 0))
  cost_per_km = round((tank/distance)*mean_price, 2)
  return cost_per_km

def cost_per_hundred_km(price, fill_L, odometer, data):
  per_km = cost_per_km(price, fill_L, odometer, data)
  cost_per_hundred_km = per_km*100
  return cost_per_hundred_km 

