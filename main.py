import pygame
import numpy as np
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Initialize Pygame
pygame.init()

# Screen size and grid dimensions
size = (800, 600)
cell_size = 10
cols = size[0] // cell_size
rows = size[1] // cell_size

# Create the display surface
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Conway's Game of Life")

# Initialize the grid
grid = np.zeros((cols, rows), dtype=int)

def initialize_grid():
    global grid
    # Randomly initialize the grid with some live cells
    for x in range(cols):
        for y in range(rows):
            grid[x, y] = random.choice([0, 1])  # 0 or 1 with equal probability

def draw_grid():
    for x in range(cols):
        for y in range(rows):
            color = GREEN if grid[x, y] else BLACK
            pygame.draw.rect(screen, color, pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size))

def update_grid():
    global grid
    new_grid = np.copy(grid)
    for x in range(cols):
        for y in range(rows):
            alive_neighbors = sum([
                grid[(x-1)%cols, (y-1)%rows],
                grid[(x-1)%cols, y],
                grid[(x-1)%cols, (y+1)%rows],
                grid[x, (y-1)%rows],
                grid[x, (y+1)%rows],
                grid[(x+1)%cols, (y-1)%rows],
                grid[(x+1)%cols, y],
                grid[(x+1)%cols, (y+1)%rows]
            ])
            if grid[x, y] == 1:
                if alive_neighbors < 2 or alive_neighbors > 3:
                    new_grid[x, y] = 0
            else:
                if alive_neighbors == 3:
                    new_grid[x, y] = 1
    grid = new_grid

# Initialize the grid with random values
initialize_grid()

# Main loop
running = True
clock = pygame.time.Clock()
simulation_running = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                simulation_running = not simulation_running
            elif event.key == pygame.K_c:
                initialize_grid()  # Reinitialize the grid with random values

    if simulation_running:
        update_grid()

    screen.fill(BLACK)  # Clear the screen
    draw_grid()
    pygame.display.flip()
    clock.tick(10)

pygame.quit()
