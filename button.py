import pygame
from pygame.locals import *
from colors import *

class Button:
    # variables 
    text_color = BLACK
    width = 180
    height = 70

    def __init__(self, x, y, text):
        self.x = x
        self.y = y
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
        text_len = text_img.get_width()
        surface.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 25))

        return action
    
