import pygame
from pygame.locals import *
from util.colors import *

class Button:
    # variables 
    text_color = BLACK
    # width = 100
    # height = 50

    def __init__(self, x, y, width, height, text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = Rect(self.x, self.y, self.width, self.height)
        self.text = text
        self.clicked = False
    
    def draw(self, surface):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                self.clicked = True
                pygame.draw.rect(surface, CLICKED_COLOR, self.rect)
        
            elif pygame.mouse.get_pressed()[0] == 0 and self.clicked == True:
                self.clicked = False
                action = True
            else:
                pygame.draw.rect(surface, HOVER_COLOR, self.rect)
        else:
            pygame.draw.rect(surface, BUTTON_COLOR, self.rect)

        font = pygame.font.SysFont("Arial", 30, bold=False, italic=False)
        text_img = font.render(self.text, True, self.text_color)
        text_x = (self.width - text_img.get_width()) // 2
        text_y = (self.height - text_img.get_height()) // 2
        surface.blit(text_img, (self.x + text_x, self.y + text_y))

        return action
    
