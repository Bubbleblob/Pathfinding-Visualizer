import heapq
import pygame
from util.graph_util import *
from util.node import *

def dijkstra(draw, grid, start, end):
    # initialize distances to infinity and set start to 0
    distances = {node: float("inf") for row in grid for node in row}
    distances[start] = 0
    came_from = {}

    min_heap = [(0, start)] # used to keep track of shortest distance
    heapq.heapify(min_heap)

    while min_heap:
        distance, current = heapq.heappop(min_heap)

        if current == end: # reconstruct path
            end.make_end()
            reconstruct_path(came_from, end, draw)
            start.make_start()
            return True
        if distance > distances[current]:
            continue

        for neighbor in current.neighbors:
            new_distance = distances[current] + 1

            if new_distance < distances[neighbor]:
                neighbor.make_open()
                came_from[neighbor] = current
                distances[neighbor] = new_distance
                heapq.heappush(min_heap, (new_distance, neighbor))
        draw()

        if current != start:
            current.make_closed()
            