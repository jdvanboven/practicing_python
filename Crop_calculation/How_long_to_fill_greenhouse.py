'''
This script can be used to calculate how long it takes to fill the greenhouse with a certain crop.
It needs to know how long a crop takes to mature, how many products it produces and if it produces once or more times.
It assumes the products are put into a seed maker and that the seed maker produces X seeds on average.
'''

TOTAL_SPACES = 100

class Plant:
    def __init__(self)
        self.age = 0

    def increase_age(self)
        self.age += 7

def age_plants(plant_list):
    for plant in plant_list
        plant.increase_age()

def generate_new_plants():
    pass

def main()
    p1 = Plant()
    plant_list = []
    plant_list.append(p1)
    greenhouse_full = False
    while greenhouse_full == False:
        age_plants(plant_list)
        plant_new_seeds(plant_list)


if __name__ == "__main__":
    main()