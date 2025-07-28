import pygame
class Canvas: 
    def __init__(self):
        pygame.init()
        self.screen_width = 650 
        self.screen_height = 650 

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Hilbert curve")
        