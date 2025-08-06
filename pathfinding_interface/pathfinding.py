import pygame
import random
from itertools import permutations
import numpy as np

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

# population_size should be smaller than the amount of permutations. Not too large, because that requires a lot of calculation.
population_size = 6

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

def calculate_distance_between_cells(cell_1, cell_2):
    a = cell_1.x_coord - cell_2.x_coord
    b = cell_1.y_coord - cell_2.y_coord
    distance = np.sqrt(a**2 + b**2)
    return distance

# test_list = []
# for x in range(0, 250, 50):
#     print(x)
#     test_list.append(Grid_cell(x, x, 10, 10))

def generate_distance_matrix(cells_list):
    distance_matrix = []
    for _ in range(len(cells_list)):
        distance_matrix.append([])
    
    for index_1 in range(len(cells_list)):
        for index_2 in range(index_1, len(cells_list)):
            distance = calculate_distance_between_cells(cells_list[index_1], cells_list[index_2])
            distance_matrix[index_1].append(distance)
            if index_1 is not index_2:
                distance_matrix[index_2].append(distance)
    return distance_matrix

def generate_initial_population(locations_list, population_size):
    population_permutations = []
    possible_permutations = list(permutations(locations_list))
    print(possible_permutations)
    print(len(possible_permutations))
    random_ids = random.sample(range(0, len(possible_permutations)), population_size)
    for i in random_ids:
        population_permutations.append(list(possible_permutations[i]))

    return population_permutations

def calculate_individual_distance():
    pass

def run_genetic_algorithm(locations_list, population_size):
    population_permutations = generate_initial_population(locations_list, population_size)
    print(population_permutations)

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
                run_genetic_algorithm(selected_cells_list, population_size)

    for cell in board:
        pygame.draw.rect(grid_surface, cell.fill_color, (cell.x, cell.y, cell.w, cell.h))
        if cell.passable == False:
            pygame.draw.rect(grid_surface, cell.border_color, (cell.x, cell.y, cell.w, cell.h), width = 3)

    pygame.draw.rect(grid_surface, "white", (calc_button.x, calc_button.y, calc_button.w, calc_button.h))
            
    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()


