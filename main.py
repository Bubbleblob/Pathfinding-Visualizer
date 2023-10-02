import pygame
from util.button import *
from util.colors import *
from algorithms.aStar import *
from algorithms.runAlgorithm import *

def main():
    pygame.init()

    # create menu screen 
    WIDTH = 800
    screen = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption("A* Path Finding Algorithm")

    # create button instances
    start_button = Button(100, 200, "start")
    exit_button = Button(450, 200, "exit")

    run = True
    
    while run:
        screen.fill(LIGHT_GREY)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if start_button.draw(screen):
            runAlgorithm(screen, WIDTH)
        if exit_button.draw(screen):
            run = False

        pygame.display.update()
    
    pygame.QUIT()


if __name__ == '__main__':
    main()