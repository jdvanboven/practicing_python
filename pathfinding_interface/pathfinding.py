import pygame

pygame.init()
grid_surface = pygame.display.set_mode(size=(500,500), flags=pygame.RESIZABLE)
clock = pygame.time.Clock()
running = True
base_color = (200, 0, 0)
grid_size = (11, 9)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x ,y = (event.pos[0], event.pos[1])
            print(x, y)

    grid_surface.fill("black")

    pygame.draw.rect(grid_surface, base_color, (100, 100, 50, 50))
    
    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()


