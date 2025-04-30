'''
This script can be used to calculate how long it takes to fill the greenhouse with a certain crop.
It needs to know how long a crop takes to mature, how many products it produces and if it produces once or more times.
It assumes the products are put into a seed maker and that the seed maker produces X seeds on average.
'''

import math
import json
from tkinter import *
from tkinter import ttk

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

# TO DO: Take into account the amount of fruits produced
def generate_new_seeds(plant_list, fruit_interval, maturity_age):
    seeds = 0
    for plant in plant_list:
        if plant.mature == True and (plant.age - maturity_age) % fruit_interval == 0:
            seeds += 2
    return seeds

def plant_new_seeds(plant_list, new_seeds):
    for seed in range(new_seeds):
        plant_list.append(Plant())

# TO DO: 
def simulate_greenhouse(crop_list):
    crop_name = crop.get()
    maturity_age = crop_list["crops"][crop_name]["maturity_age"]
    fruit_interval = crop_list["crops"][crop_name]["fruit_interval"] 
    number_of_seeds = int(starting_seeds.get())
    print(number_of_seeds)
    greenhouse_spaces = int(available_spaces.get())
    plant_list = [Plant() for i in range(number_of_seeds)]
    greenhouse_full = False
    while greenhouse_full == False:
        age_plants(plant_list, maturity_age)
        new_seeds = generate_new_seeds(plant_list, fruit_interval, maturity_age)
        plant_new_seeds(plant_list, new_seeds)
        if len(plant_list) >= greenhouse_spaces:
            greenhouse_full = True
    if greenhouse_full == True:
        days_until_full.set(plant_list[0].age)
        days_until_mature.set(plant_list[0].age + maturity_age)
        print(f"It will take {plant_list[0].age} days or {math.ceil(plant_list[0].age / 7)} weeks to fill the greenhouse with {greenhouse_spaces} plants")
        print(f"It will take {plant_list[0].age + maturity_age} days or {math.ceil((plant_list[0].age + maturity_age) / 7)} weeks for all plants to reach maturity")

def main():
        with open("crops.json") as json_file:
            crop_list = json.load(json_file)
        simulate_greenhouse(crop_list)

root = Tk()
root.geometry("400x150")
root.title("Greenhouse calculator")

main_window = ttk.Frame(root, padding="3 3 12 12")
main_window.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

with open("crops.json") as json_file:
        crop_list = json.load(json_file)
crop_names = []
for i in crop_list["crops"]:
    crop_names.append(i)
print(crop_list)
print(crop_names)

# TODO: This probably needs to be put into classes or functions
crop = StringVar()
crop_entry = ttk.Combobox(main_window, width=10, textvariable=crop, state='readonly', values=crop_names)
crop_entry.grid(column=2, row=1, sticky=(W, E))
crop_entry.current(0)
ttk.Label(main_window, text="Crop").grid(column=1, row=1, sticky=W)

available_spaces = StringVar()
available_spaces_entry = ttk.Entry(main_window, width=7, textvariable=available_spaces)
available_spaces_entry.grid(column=2, row=2, sticky=(W, E))
ttk.Label(main_window, text="Available spaces").grid(column=1, row=2, sticky=W)

starting_seeds = StringVar()
starting_seeds_entry = ttk.Entry(main_window, width=7, textvariable=starting_seeds)
starting_seeds_entry.grid(column=2, row=3, sticky=(W, E))
ttk.Label(main_window, text="# of starting seeds").grid(column=1, row=3, sticky=W)

ttk.Button(main_window, text="Calculate", command=main).grid(column=3, row=5, sticky=W)

crop_entry.focus()
root.bind("<Return>", main)

days_until_full = StringVar()
ttk.Label(main_window, text="Greenhouse is filled in approximately").grid(column=1, row=7, sticky=W)
ttk.Label(main_window, textvariable=days_until_full).grid(column=2, row=7, sticky=(W, E))
ttk.Label(main_window, text="days").grid(column=3, row=7, sticky=W)

days_until_mature = StringVar()
ttk.Label(main_window, text="All plants mature in approximately").grid(column=1, row=8, sticky=W)
ttk.Label(main_window, textvariable=days_until_mature).grid(column=2, row=8, sticky=(W, E))
ttk.Label(main_window, text="days").grid(column=3, row=8, sticky=W)


root.mainloop()