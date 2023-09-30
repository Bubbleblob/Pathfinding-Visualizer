import pygame
from colors import *

class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    def get_position(self):
        return self.row, self.col
    
    def is_closed(self):
        return self.color == YELLOW
    
    def is_open(self):
        return self.color == PEACH
    
    def is_barrier(self):
        return self.color == BLACK
    
    def is_start(self):
        return self.color == GREEN
    
    def is_end(self):
        return self.color == RED
    
    def reset(self):
        self.color = WHITE
    
    def make_start(self):
        self.color = GREEN

    def make_closed(self):
        self.color = YELLOW

    def make_open(self):
        self.color = PEACH

    def make_barrier(self):
        self.color = BLACK

    def make_end(self):
        self.color = RED

    def make_path(self):
        self.color = TURQUOISE

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        self.neighbors = []

        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier(): # down nei
            self.neighbors.append(grid[self.row + 1][self.col])
        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier(): # up nei
            self.neighbors.append(grid[self.row - 1][self.col])
        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier(): # right nei
            self.neighbors.append(grid[self.row][self.col + 1])
        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier(): # left nei
            self.neighbors.append(grid[self.row][self.col - 1])

    def __lt__(self, other):
        return False