import pygame
import utilities
from colors import *
from aStar import *

def main():
    pygame.init()

    # create menu screen 
    WIDTH = 800
    screen = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption("A* Path Finding Algorithm")

    # create button instances
    start_button = utilities.Button(100, 200, "start")
    exit_button = utilities.Button(450, 200, "exit")

    run = True
    
    while run:
        screen.fill(LIGHT_GREY)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if start_button.draw(screen):
            runAStar(screen, WIDTH)
        if exit_button.draw(screen):
            run = False

        pygame.display.update()
    
    pygame.QUIT()


if __name__ == '__main__':
    main()