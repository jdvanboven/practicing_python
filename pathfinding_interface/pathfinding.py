import pygame
import random

pygame.init()
grid_surface = pygame.display.set_mode(size=(500,500), flags=pygame.RESIZABLE)
clock = pygame.time.Clock()
running = True
base_color = (200, 0, 0)
grid_size = (11, 9)
cell_width = 50
cell_height = 50

class Grid_cell:
    def __init__(self):
        self.state = "empty"
        self.color = "gray"
        self.x = 0
        self.y = 0
        self.w = cell_width
        self.h = cell_height

    def __str__(self):
        return "state: {}, color:{}".format(self.state, self.color)

    def change_cell_state(self):
        if self.state == "empty":
            self.state = "filled"
            self.color = "green"
        
        elif self.state == "filled":
            self.state = "impassable"
            self.color = "blue"

        elif self.state == "impassable":
            self.state = "empty"
            self.color = "gray"

first_cell = Grid_cell()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x = event.pos[0]
            y = event.pos[1]
            print(x, y)
            first_cell.change_cell_state
            if x <= 50 and y <= 50:
                first_cell.change_cell_state()
                print(first_cell)

    grid_surface.fill("black")

    pygame.draw.rect(grid_surface, first_cell.color, (first_cell.x, first_cell.y, first_cell.w, first_cell.h))
    
    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()


