import pygame
import random
from itertools import permutations
import numpy as np
import math
from statistics import mode

pygame.init()
grid_surface = pygame.display.set_mode(size=(750,450), flags=pygame.RESIZABLE)
clock = pygame.time.Clock()
running = True
base_color = (200, 0, 0)
grid_size = (11, 9)
grid_width = 11
grid_height = 9
cell_width = 50
cell_height = 50

population_size = 200
number_of_generations = 200
crossover_rate = 0.7
mutation_rate = 0.7

class Grid_cell:
    def __init__(self, x, y, w, h):
        self.planted = False
        self.passable = True
        self.fill_color = "gray"
        self.border_color = "red"
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.x_coord = self.x // (cell_width + 1)
        self.y_coord = self.y // (cell_height + 1)

    def __str__(self):
        return "planted: {}, passable: {}, color: {}".format(self.planted, self.passable, self.fill_color)

    def change_planted_state(self):
        if self.planted == False:
            self.planted = True
            self.fill_color = "green"

        elif self.planted == True:
            self.planted = False
            self.fill_color = "gray"
    
    def change_passable_state(self):
        if self.passable == True:
            self.passable = False

        elif self.passable == False:
            self.passable = True       


def generate_initial_population_old(locations_list, population_size):
    population_permutations = []
    possible_permutations = list(permutations(locations_list))
    random_ids = random.sample(range(0, len(possible_permutations)), min(population_size, math.factorial(len(locations_list))))
    for i in random_ids:
        population_permutations.append(list(possible_permutations[i]))

    return population_permutations

def generate_initial_population(locations_list, population_size):
    population_permutations = []
    for i in range(0, population_size):
        population_permutations.append(random.sample(locations_list, len(locations_list)))

    return population_permutations

def calculate_distance_between_cells(cell_1, cell_2):
    a = cell_1.x_coord - cell_2.x_coord
    b = cell_1.y_coord - cell_2.y_coord
    distance = np.sqrt(a**2 + b**2)
    return distance

def calculate_individual_distance(individual):
    individual_distance = 0
    for i in range(0, len(individual)):
        if i == (len(individual) - 1):
            individual_distance += calculate_distance_between_cells(individual[i], individual[0])
        else:
            individual_distance += calculate_distance_between_cells(individual[i], individual[i+1])
    return individual_distance

def calculate_fitness_probabilities(population):
    total_distance_all_individuals = []
    for i in range(0, len(population)):
        total_distance_all_individuals.append(calculate_individual_distance(population[i]))
    max_population_distance = max(total_distance_all_individuals)
    population_fitness = max_population_distance - total_distance_all_individuals
    population_fitness_sum = sum(population_fitness)
    population_fitness_probabilities = population_fitness / population_fitness_sum
    return population_fitness_probabilities

def perform_random_selection(population, population_fitness_probabilities):
    population_fitness_probabilities_cumsum = population_fitness_probabilities.cumsum()
    randomly_selected_number = np.random.uniform(0,1,1)
    bool_probabilities_array = population_fitness_probabilities_cumsum < randomly_selected_number
    # The line below has a '- 1' at the end in the instructions. This seemed to select the wrong individual, so I removed it. Noting it here so I don't forget.
    selected_individual_index = len(bool_probabilities_array[bool_probabilities_array == True])
    return population[selected_individual_index]

def crossover_parents(parent_1, parent_2):
    n_cities_cut = len(parent_1) - 1
    cut = round(random.uniform(1, n_cities_cut))
    offspring_1 = []
    offspring_2 = []

    offspring_1 = parent_1[0:cut]
    offspring_1 += [city for city in parent_2 if city not in offspring_1]

    offspring_2 = parent_2[0:cut]
    offspring_2 += [city for city in parent_1 if city not in offspring_2]

    return offspring_1, offspring_2

def generate_mutations(offspring):
    n_cities_cut = len(offspring) - 1
    index_1 = round(random.uniform(1, n_cities_cut))
    index_2 = round(random.uniform(1, n_cities_cut))

    temp = offspring[index_1]
    offspring[index_1] = offspring[index_2]
    offspring[index_2] = temp

    return offspring

def generate_offspring(population, population_fitness_probabilities, population_size, crossover_rate, mutation_rate):
    parents_list = []
    for i in range(0, int(crossover_rate * population_size)):
        parents_list.append(perform_random_selection(population, population_fitness_probabilities))

    offspring_list = []
    for i in range(0, len(parents_list), 2):
        offspring_1, offspring_2 = crossover_parents(parents_list[i], parents_list[i+1])

        mutate_threshold = random.random()
        if mutate_threshold > (1 - mutation_rate):
            offspring_1 = generate_mutations(offspring_1)

        mutate_threshold = random.random()
        if mutate_threshold > (1 - mutation_rate):
            offspring_2 = generate_mutations(offspring_2)

        offspring_list.append(offspring_1)
        offspring_list.append(offspring_2)

    mixed_offspring = parents_list + offspring_list

    return mixed_offspring    

def perform_replacement(mixed_offspring, crossover_rate, population_size, population):
    fitness_probabilities = calculate_fitness_probabilities(mixed_offspring)
    sorted_fitness_indices = np.argsort(fitness_probabilities)[::-1]
    best_fitness_indices = sorted_fitness_indices[0:int(crossover_rate * population_size)]

    best_mixed_offspring = []
    for i in best_fitness_indices:
        best_mixed_offspring.append(mixed_offspring[i])

    old_population_indices = []
    for i in range(int((1 - crossover_rate) * population_size)):
        old_population_indices.append(random.randint(0, (len(population) - 1)))

    for i in old_population_indices:
        best_mixed_offspring.append(population[i])

    random.shuffle(best_mixed_offspring)
    return best_mixed_offspring

def run_genetic_algorithm(locations_list, population_size):
    # population = generate_initial_population(locations_list, population_size)
    population = generate_initial_population(locations_list, population_size)
    
    for generation in range(1, number_of_generations + 1):
        if generation % 20 == 0:
            print(f'generation = {generation}')
            total_dist_all_individuals = []
            for i in range(0, len(population)):
                total_dist_all_individuals.append(calculate_individual_distance(population[i]))
            minimum_distance = min(total_dist_all_individuals)
            print(minimum_distance)

        population_fitness_probabilities = calculate_fitness_probabilities(population)
        mixed_offspring = generate_offspring(population, population_fitness_probabilities, population_size, crossover_rate, mutation_rate)
        population = perform_replacement(mixed_offspring, crossover_rate, population_size, population)

    total_dist_all_individuals = []
    for i in range(0, len(population)):
        total_dist_all_individuals.append(calculate_individual_distance(population[i]))
    index_minimum = np.argmin(total_dist_all_individuals)
    minimum_distance = min(total_dist_all_individuals)
    print(minimum_distance)
    shortest_path = population[index_minimum]
    return shortest_path
        
board = []
for y in range(grid_height):
    for x in range(grid_width):
        board.append(Grid_cell(x*(cell_width + 1), y*(cell_height + 1), cell_width, cell_height))

calc_button = Grid_cell(601, 101, 100, 50)
print(calc_button.x_coord, calc_button.y_coord)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            col = event.pos[0] // (cell_width + 1)
            row = event.pos[1] // (cell_height + 1)
            print(col, row)
            
            if col <= (grid_width - 1) and row <= (grid_height - 1):
                for cell in board:
                    if cell.x_coord == col and cell.y_coord == row:
                        current_cell = cell
                        break

                if event.button == 1:
                    current_cell.change_planted_state()

                elif event.button == 3:
                    current_cell.change_passable_state()

            if (col == calc_button.x_coord + 1 or col == calc_button.x_coord + 2) and row == (calc_button.y_coord + 1):
                selected_cells_list = []
                for cell in board:
                    if cell.planted == True:
                        selected_cells_list.append(cell)
                shortest_path = run_genetic_algorithm(selected_cells_list, population_size)

    # if 'shortest_path' in locals():
    #     print(shortest_path)

    for cell in board:
        pygame.draw.rect(grid_surface, cell.fill_color, (cell.x, cell.y, cell.w, cell.h))
        if cell.passable == False:
            pygame.draw.rect(grid_surface, cell.border_color, (cell.x, cell.y, cell.w, cell.h), width = 3)

    pygame.draw.rect(grid_surface, "white", (calc_button.x, calc_button.y, calc_button.w, calc_button.h))
    # for cell in shortest_path:
    #     pygame.draw.line(grid_surface, "red", ((cell.x + cell.w /2), cell.y + cell.h / 2), (20, 20) , 3)
            
    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()


