import pygame
import random

pygame.init()
grid_surface = pygame.display.set_mode(size=(550,450), flags=pygame.RESIZABLE)
clock = pygame.time.Clock()
running = True
base_color = (200, 0, 0)
grid_size = (11, 9)
grid_width = 11
grid_height = 9
cell_width = 50
cell_height = 50

grid_surface.fill("black")

class Grid_cell:
    def __init__(self, x, y, w, h):
        self.state = "empty"
        self.color = "gray"
        self.x = x
        self.y = y
        self.w = w
        self.h = h

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

board = []
for y in range(grid_height):
    board.append([])
    for x in range(grid_width):
        board[y].append(Grid_cell(x*(cell_width + 1), y*(cell_height + 1), cell_width, cell_height))


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            col = event.pos[0] // (cell_width + 1)
            row = event.pos[1] // (cell_height + 1)

            if col <= (grid_width - 1) and row <= (grid_height -1):
                current_cell = board[row][col]
                current_cell.change_cell_state()

                for row in board:
                    for cell in row:
                        pygame.draw.rect(grid_surface, cell.color, (cell.x, cell.y, cell.w, cell.h))
        


            
    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()


