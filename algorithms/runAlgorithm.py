import pygame
from util.graph_util import *
from algorithms.aStar import *
from algorithms.bfs import *
from algorithms.dijkstra import *
from util.button import *

def runAlgorithm(window, width):
    ROWS = 50
    run = True
    started = False
    start = None
    end = None
    grid = make_grid(ROWS, width)
    update_grid = pygame.Rect(0, 0, width, width) # used to only update the grid
    update_control_panel = pygame.Rect(0, 800, 800, 200) # used to only update the control panel

    main_menu_button = Button(100, 850, 130, 50, "main menu")
    reset_button = Button(250, 850, 100, 50, "reset")
    run_algorithm_button = Button(400, 850, 100, 50, "run")
    choose_algorithm_button = Button(550, 850, 110, 50, "algorithm")

    # a_star_button = Button(100, 850, 100, 50, "A*")
    # dijkstra_button = Button(100, 850, 100, 50, "Dijkstra")
    # bfs_button = Button(100, 850, 100, 50, "BFS")

    while run:
        draw(window, grid, ROWS, width, update_grid)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            
            if started: # prevent clicks while algorithm is running
                continue

            if pygame.mouse.get_pressed()[0]: # left mouse click
                position = pygame.mouse.get_pos()
                row, col = get_clicked_pos(position, ROWS, width)
                if row >= 0 and row < 50 and col >= 0 and col < 50: # stop program from closing when out of bounds
                    node = grid[row][col]
                else:
                    continue
                if not start and node != end: # setting start node
                    start = node
                    start.make_start()

                elif not end and node != start: # setting end node
                    end = node
                    end.make_end()

                elif node != end and node != start:# setting barriers
                    node.make_barrier()

            elif pygame.mouse.get_pressed()[2]: # right mouse click (clearing current node)
                position = pygame.mouse.get_pos()
                row, col = get_clicked_pos(position, ROWS, width)
                if row >= 0 and row < 50 and col >= 0 and col < 50: # stop program from closing when out of bounds
                    node = grid[row][col]
                else:
                    continue
                node.reset()

                if node == start:
                    start = None
                if node == end:
                    end = None

            if event.type == pygame.KEYDOWN: # start algorithm
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid) # update neighbors based on change in barriers
                    
                    aStar(lambda: draw(window, grid, ROWS, width, update_grid), grid, start, end)

                elif event.key == pygame.K_r: # reset board
                    resetGrid(grid)
                    start = None
                    end = None

        if main_menu_button.draw(window):
            run = False
        if reset_button.draw(window):
            resetGrid(grid)
            start = None
            end = None
        if run_algorithm_button.draw(window):
            for row in grid:
                for node in row:
                    node.update_neighbors(grid) # update neighbors based on change in barriers
            
            aStar(lambda: draw(window, grid, ROWS, width, update_grid), grid, start, end)
        if choose_algorithm_button.draw(window):
            print("4")                                                                                          # FINISH THIS PART
        
        pygame.display.update(update_control_panel)
    
    return