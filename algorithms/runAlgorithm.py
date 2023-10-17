import pygame
from util.graph_util import *
from algorithms.aStar import *
from algorithms.bfs import *
from algorithms.dijkstra import *
from util.button import *

def runAlgorithm(window, width, algorithm_flag):
    ROWS = 50
    run = True
    started = False
    start = None
    end = None
    grid = make_grid(ROWS, width)
    update_grid = pygame.Rect(0, 0, width, width) # used to only update the grid
    update_control_panel = pygame.Rect(0, 800, 800, 200) # used to only update the control panel

    # buttons
    main_menu_button = Button(100, 850, 130, 50, "main menu")
    reset_button = Button(250, 850, 100, 50, "reset")
    run_algorithm_button = Button(400, 850, 100, 50, "run")
    choose_algorithm_button = Button(550, 850, 110, 50, "algorithm")

    a_star_button = Button(100, 850, 100, 50, "A*")
    dijkstra_button = Button(250, 850, 100, 50, "Dijkstra")
    bfs_button = Button(400, 850, 100, 50, "BFS")

    main_panel_flag = True  # used to display and run functionality of main panel buttons
    algorithm_panel_flag = False  # used to display and run functionality of choosing algorithm buttons

    # display text based on which algorithm is currently picked
    # if algorithm_flag[0] == 0:
    #     current_algorithm_text = "A*"
    # elif algorithm_flag[0] == 1:
    #     current_algorithm_text = "Dijsktra"
    # else:
    #     current_algorithm_text = "Breadth First Search"

    font = pygame.font.SysFont("Arial", 40)

    while run:
        draw(window, grid, ROWS, width, update_grid)
        pygame.draw.rect(window, LIGHT_GREY, update_control_panel)
        pygame.draw.line(window, GREY, (0, width), (width, width))

        if algorithm_flag[0] == 0:
            current_algorithm_text = "A*"
        elif algorithm_flag[0] == 1:
            current_algorithm_text = "Dijsktra"
        else:
            current_algorithm_text = "Breadth First Search"
        title_surface = font.render(current_algorithm_text, True, BLACK)
        window.blit(title_surface, (0, 800))

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

        # buttons for main panel
        if main_panel_flag:
            if main_menu_button.draw(window):
                run = False

            if reset_button.draw(window):
                resetGrid(grid)
                start = None
                end = None

            if run_algorithm_button.draw(window):
                if start and end:
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid) # update neighbors based on change in barriers

                    if algorithm_flag[0] == 0:
                        aStar(lambda: draw(window, grid, ROWS, width, update_grid), grid, start, end)
                    elif algorithm_flag[0] == 1:
                        dijkstra(lambda: draw(window, grid, ROWS, width, update_grid), grid, start, end)
                    else:
                        bfs(lambda: draw(window, grid, ROWS, width, update_grid), start, end)

            if choose_algorithm_button.draw(window):
                main_panel_flag = False
                algorithm_panel_flag = True

        # buttons for choosing algorithm panel
        if algorithm_panel_flag: 
            if a_star_button.draw(window):
                algorithm_flag[0] = 0
                main_panel_flag = True
                algorithm_panel_flag = False

            if dijkstra_button.draw(window):
                algorithm_flag[0] = 1
                main_panel_flag = True
                algorithm_panel_flag = False

            if bfs_button.draw(window):
                algorithm_flag[0] = 2
                main_panel_flag = True
                algorithm_panel_flag = False

        pygame.display.update(update_control_panel)

    return
