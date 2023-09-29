import pygame
import utilities

from aStar import *

def main():
    #runAStar(algorithm_screen, WIDTH)

    BLACK = (0, 0, 0) 
    # create menu screen 
    WIDTH = 800
    screen = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption("A* Path Finding Algorithm")

    # create algorithm run screen
    #algorithm_screen = pygame.display.set_mode((WIDTH, WIDTH))

    # load button images
    start_img = pygame.image.load('start_btn.png').convert_alpha()
    exit_img = pygame.image.load('exit_btn.png').convert_alpha()

    # create button instances
    start_button = utilities.Button(100, 200, start_img, 1)
    exit_button = utilities.Button(450, 200, exit_img, 1)

    run = True
    
    while run:
        screen.fill(BLACK)

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