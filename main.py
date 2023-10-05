import pygame
from util.button import *
from util.colors import *
from algorithms.aStar import *
from algorithms.runAlgorithm import *

def main():
    pygame.init()

    # create menu screen 
    WIDTH = 800
    HEIGHT = 1000
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Path Finding Algorithms")

    TITLE = "Path Finding Algorithms"
    font = pygame.font.SysFont("Arial", 40)
    title_surface = font.render(TITLE, True, BLACK)

    # create button instances
    start_x = WIDTH // 4
    exit_x = WIDTH // 4 * 2
    start_y = HEIGHT // 3
    exit_y = HEIGHT // 3
    start_button = Button(start_x, start_y, 100, 50, "start")
    exit_button = Button(exit_x, exit_y, 100, 50, "exit")

    # used for determining which algorithm to run (0-aStar, 1-dijsktra, 2-bfs)
    algorithm_flag = [0]

    run = True
    
    while run:
        screen.fill(LIGHT_GREY)
        screen.blit(title_surface, (200, 200))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if start_button.draw(screen):
            runAlgorithm(screen, WIDTH, algorithm_flag)
        if exit_button.draw(screen):
            run = False

        pygame.display.update()
    
    pygame.quit()


if __name__ == '__main__':
    main()