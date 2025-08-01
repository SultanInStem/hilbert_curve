import pygame
import sys 
class Canvas: 
    def __init__(self):
        pygame.init()
        self.screen_width = 650 
        self.screen_height = 650 
        self.running = True
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Hilbert curve")
        self.fps = 30 
        self.clock = pygame.time.Clock()

    def update(self): 
        pass 
    def handle_events(self): 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                self.running = False 
    def display(self): 
        self.screen.fill((0,0,0))

        pygame.display.flip()
        self.clock.tick(self.fps)
    def run(self):
        while(self.running):
            self.update()
            self.handle_events()
            self.display() 
        pygame.quit()
        sys.exit()

