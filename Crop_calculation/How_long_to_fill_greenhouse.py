'''
This script can be used to calculate how long it takes to fill the greenhouse with a certain crop.
It needs to know how long a crop takes to mature, how many products it produces and if it produces once or more times.
It assumes the products are put into a seed maker and that the seed maker produces X seeds on average.
'''

import math

TOTAL_SPACES = 100
STARTING_SEEDS = 1
MATURITY_AGE = 28
FRUIT_INTERVAL = 7

class Plant:
    def __init__(self):
        self.age = 0
        self.mature = False

    def increase_age(self, maturity_age):
        self.age += 1
        if self.age >= maturity_age:
            self.mature = True

def age_plants(plant_list, maturity_age):
    for plant in plant_list:
        plant.increase_age(maturity_age)

# TO DO: Make the amount of seeds generated changeable
# Take into account the amount of fruits produced
# Take into account the amount of seeds per fruit produced
def generate_new_seeds(plant_list, fruit_interval, maturity_age):
    seeds = 0
    for plant in plant_list:
        if plant.mature == True and (plant.age - maturity_age) % fruit_interval == 0:
            seeds += 1
    return seeds

def plant_new_seeds(plant_list, new_seeds):
    for seed in range(new_seeds):
        plant_list.append(Plant())

# TO DO: 
def simulate_greenhouse(starting_seeds, greenhouse_spaces, maturity_age, fruit_interval):
    plant_list = [Plant() for i in range(starting_seeds)]
    greenhouse_full = False
    while greenhouse_full == False:
        age_plants(plant_list, maturity_age)
        new_seeds = generate_new_seeds(plant_list, fruit_interval, maturity_age)
        plant_new_seeds(plant_list, new_seeds)
        if len(plant_list) >= greenhouse_spaces:
            greenhouse_full = True
    if greenhouse_full == True:
        print(f"It will take {plant_list[0].age} days or {math.ceil(plant_list[0].age / 7)} weeks to fill the greenhouse with {greenhouse_spaces} plants")
        print(f"It will take {plant_list[0].age + maturity_age} days or {math.ceil((plant_list[0].age + maturity_age) / 7)} weeks for all plants to reach maturity")

def main():
    simulate_greenhouse(STARTING_SEEDS, TOTAL_SPACES, MATURITY_AGE, FRUIT_INTERVAL)

if __name__ == "__main__":
    main()