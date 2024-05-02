import time
import random
import datetime
import csv
import math
#Global variables

#Simulator variables
water_bacteria_level = 2000.0
water_solids_level = 50
outside_temp = 24.0
buthane = 0
methane = 0

#World variables
is_raining = False
hour = 0
day = 1
month = 3
year = 2024
day_str = f'0{day}'
mth_str = f'0{month}'
hour_str = f'0{hour}:00:00'
all_animals = []

#Schedules
temp_schedule = [0,3,6,15,18,20]
gas_schedule = [0,1,2,3,4,5,6,13,16,18,20,22,23]
solids_schedule = [13]

#Data
rows = 1

class Animal:
  def __init__(self, id, temp, lat, lon, is_sick, is_pregnant, species):
    self.id = id
    self.temp = temp
    self.lat = lat
    self.lon = lon
    self.is_sick = is_sick
    self.is_pregnant = is_pregnant
    self.species = species

  global is_raining

  def get_id(self):
    return self.id

  def set_id(self,id):
    self.id = id

  def get_temp(self):
    return self.temp

  def set_temp(self,temp):
    self.temp = temp

  def get_lat(self):
    return self.lat

  def set_lat(self,lat):
    self.lat = lat

  def get_lon(self):
    return self.lon

  def set_lon(self,lon):
    self.lon = lon

  def get_is_sick(self):
    return self.is_sick

  def set_is_sick(self,is_sick):
    self.is_sick = is_sick

  def get_is_pregnant(self):
    return self.is_pregnant

  def set_is_pregnant(self,is_pregnant):
    self.is_pregnant = is_pregnant

  def ingest_fecal_matter(self):
    decider = round(random.uniform(0,100), 0)
    if decider < 5:
      self.set_is_sick(True)
    else:
      self.set_is_sick(False)

  def move(self):
    self.set_lat(round(random.uniform(-7, -6), 2))
    self.set_lon(round(random.uniform(-52, -51), 2))

  def body_temp_change(self):
    if self.is_sick:
      high_limit_temp = 43.0
      low_limit_temp = 39.4
    elif not self.is_sick and is_raining:
      high_limit_temp = 38.7
      low_limit_temp = 37.0
    else:
      high_limit_temp = 39.3
      low_limit_temp = 38.0
    self.set_temp(round(random.uniform(low_limit_temp, high_limit_temp), 1))

  def drink_water(self):
    if water_bacteria_level > 10000:
      self.is_sick = True

  def wellfare_check(self):
    if self.is_sick:
      decider = round(random.uniform(0,10),0)
      if decider > 5:
        self.is_sick = False


# Time

def add_hour():
  global hour, day, month, year, day_str, mth_str, hour_str
  hour+=1
  if hour >23:
    day+=1
    hour = 0
  if day >30:
      day =1
      month+=1
  if month >12:
      month =1
      year+=1
  if day >=10:
      day_str = f'{day}'
  else:
      day_str = f'0{day}'
  if month >=10:
      mth_str = f'{month}'
  else:
      mth_str = f'0{month}'
  if hour >=10:
    hour_str = f'{hour}:00:00'
  else:
    hour_str = f'0{hour}:00:00'
 
  return f"{year}-{mth_str}-{day_str} {hour_str}"


#Random events

def rain():
  global water_bacteria_level, water_solids_level, is_raining
  is_it_raining = round(random.uniform(0,10), 0)
  if is_it_raining > 7:
    is_raining = True
    water_bacteria_level += 700
    water_solids_level +=200
  else:
    is_raining = False

#Scheduled events

def water_cleaning():
  global water_bacteria_level, water_solids_level
  water_bacteria_level = round(random.uniform(800,2000),1)
  water_solids_level = random.uniform(40,75)

def routine_wellfare_check(animal: Animal):
  animal.wellfare_check()

def sleep_time():
  global methane
  if hour > 22 or hour < 6:
    methane +=20
  elif hour == 7:
    methane -= 180

#Conditioned events

def epidemic(animals: list[Animal]):
  someone_is_sick = False
  for animal in animals:
    if animal.get_is_sick():
      someone_is_sick = True
    if not animal.get_is_sick() and someone_is_sick:
      animal.set_is_sick(True)

#Constant events
def change_in_outside_temp():
  global outside_temp
  high_temperature_range = 26
  low_temperature_range = 22
  if month in range(3,5) or month in range(9,11):
    low_temperature_range = random.uniform(18, 22)
    high_temperature_range = random.uniform(24, 28)
  elif month == 12 or month == 1 or month == 2:
    low_temperature_range = random.uniform(24, 26)
    high_temperature_range = random.uniform(28, 30)
  else:
    low_temperature_range = random.uniform(14, 16)
    high_temperature_range = random.uniform(20, 24)
  if is_raining:
    low_temperature_range = random.uniform(low_temperature_range-4, low_temperature_range)
  if hour not in range(7, 19):
    low_temperature_range = random.uniform(low_temperature_range-4, low_temperature_range)
    high_temperature_range = random.uniform(high_temperature_range-4, high_temperature_range)

  def change_temperature():
    new_temp = round(random.uniform(low_temperature_range, high_temperature_range),1)
    return new_temp

  outside_temp = change_temperature()

# Simulators

def proteus(): #colonies

  global water_bacteria_level

  def generate_bacteria_data(last_number, range_width): #creates a new value inside a range based on the last used value
    min_val = max(0, last_number - range_width)
    max_val = last_number + range_width
    new_val = random.uniform(min_val, max_val)
    return new_val

  water_bacteria_level = round(generate_bacteria_data(water_bacteria_level, random.uniform(-1000,1000)))

  return water_bacteria_level

def mq4(): #gases
  def generate_gases_level():
    buthane = round(random.uniform(200, 500), 2)
    methane = round(random.uniform(200, 5000), 2)
    return buthane, methane

  global buthane, methane

  buthane, methane = generate_gases_level()

  return buthane, methane

# def gyneo(animal: Animal): #gps
#   lat = []
#   lon = []
#   for a in all_animals:
#     lat.append(a.get_lat())
#     lon.append(a.get_lon())
    
#   return lat, lon

def keyestudio(): #solids
  global water_solids_level
  water_solids_level = random.randint(int(water_solids_level), int(water_solids_level) + 100)
  print(water_solids_level)
  return water_solids_level

def gydci(animals: list[Animal]): #temp
  global outside_temp
  animals_temp = []
  print(f"Outside temp: {outside_temp}")
  for animal in animals:
    animal.body_temp_change()
    animals_temp.append(animal.get_temp())
  
  return outside_temp, animals_temp


#Animal creation

for n in range(0,10):
    animal = Animal(n, 38.0, -6, -51, False, False, "cow")
    all_animals.append(animal)



data_matrix = [["data_hora", "sdt", "ufc", "butano", "metano", "temp_ambiente"]]

for a in range(len(all_animals)):
  data_matrix[0].append(f"temp{a}")

# for a in range(len(all_animals)):
#   data_matrix[0].append(f"lat{a}")
# for a in range(len(all_animals)):
#   data_matrix[0].append(f"lon{a}")
# for a in data_matrix:
#   print(a)



#Unified simulator

def unified_simulator():

  global is_raining, hour, day, month, year, day_str, mth_str, hour_str, temp_schedule, solids_schedule, gas_schedule, all_animals, rows

#Scheduled events
  if day % 7 == 0:
    water_cleaning()

  if day % 3 == 0:
    for animal in all_animals:
      routine_wellfare_check(animal)

  sleep_time()

  def random_event():
    decider = random.uniform(0,100)
    if decider in range(0,7):
      chosen_animals = []
      for animal in all_animals:
        number = random.uniform(0,10)
        if number < 3:
          chosen_animals.append(animal)
      epidemic(chosen_animals)
    elif decider in range(5, 40):
      rain()
    elif decider in range(5, 30):
      for animal in all_animals:
        number = random.uniform(0,10)
        if number < 6:
          animal.drink_water
    elif decider in range(35, 80):
      for animal in all_animals:
        number = random.uniform(0,10)
        if number < 6:
          animal.move()
    elif decider in range(97, 100):
      for animal in all_animals:
        number = random.uniform(0,10)
        if number < 1:
          animal.ingest_fecal_matter()

  change_in_outside_temp()

  t=len(data_matrix)
  data_matrix.append([add_hour()])
  
  random_event()

  if hour in solids_schedule:
    data_matrix[t].append(keyestudio())
  else:
    data_matrix[t].append(0)
  data_matrix[t].append(proteus())
  if hour in gas_schedule:
    butano, metano = mq4()
    data_matrix[t].append(butano)
    data_matrix[t].append(metano)
  else:
    data_matrix[t].append(0)
    data_matrix[t].append(0)
  if hour in temp_schedule:
      out_temp, animals_temp = gydci(all_animals)
      data_matrix[t].append(out_temp)
      for a in animals_temp:
        data_matrix[t].append(a)
  else:
    data_matrix[t].append(0)
  

#   if hour % 4 == 0:
#     for animal in all_animals:
#       latitude, longitude = gyneo(animal)
#       for l in latitude:
#         data_matrix[t].append(l)
#       for l in longitude:
#         data_matrix[t].append(l)
#   else:
#     for l in range(len(all_animals)):
#         data_matrix[t].append(0)
#     for l in range(len(all_animals)):
#         data_matrix[t].append(0)
  
with open("dados_gerados.csv", mode="w", newline='') as arquivo:
  escritor = csv.writer(arquivo)
  while(True):
    print(data_matrix[len(data_matrix)-1])
    escritor.writerow(data_matrix[len(data_matrix)-1])
    unified_simulator()
    time.sleep(0.01)

 
  
  
