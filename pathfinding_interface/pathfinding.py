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

# grid_surface.fill("black")

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
                
                if event.button == 1:
                    current_cell.change_planted_state()

                elif event.button == 3:
                    current_cell.change_passable_state()

                for row in board:
                    for cell in row:
                        pygame.draw.rect(grid_surface, cell.fill_color, (cell.x, cell.y, cell.w, cell.h))
                        if cell.passable == False:
                            pygame.draw.rect(grid_surface, cell.border_color, (cell.x, cell.y, cell.w, cell.h), width = 3)


            
    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()


