import pygame
from util.graph_util import *
from util.node import *

def bfs(draw, start, end):
    came_from = {}
    visited = set()
    queue = []

    visited.add(start)
    queue.append(start)

    while queue:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # exit game
                pygame.quit()
        current = queue.pop(0)

        if current == end: # reconstruct path
            end.make_end()
            reconstruct_path(came_from, end, draw)
            start.make_start()
            return True

        for neighbor in current.neighbors:
            if neighbor not in visited:
                came_from[neighbor] = current
                queue.append(neighbor)
                visited.add(neighbor)
                neighbor.make_open()

        draw()

        if current != start:
            current.make_closed()

    return False
