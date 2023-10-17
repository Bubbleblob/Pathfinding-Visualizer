import pygame
from util.node import *
from util.colors import *

def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, gap, rows)
            grid[i].append(node)
    return grid

def draw_grid(window, rows, width):
    gap = width // rows
    for i in range(rows + 1):
        pygame.draw.line(window, GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(window, GREY, (j * gap, 0), (j * gap, width))

def resetGrid(grid):
    for row in grid:
        for node in row:
            node.reset()

def draw(window, grid, rows, width, update_rect):
    window.fill(WHITE)

    for row in grid:
        for node in row:
            node.draw(window)   
    draw_grid(window, rows, width)
    pygame.display.update(update_rect)

def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos

    row = y // gap
    col = x // gap

    return row, col

def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()
