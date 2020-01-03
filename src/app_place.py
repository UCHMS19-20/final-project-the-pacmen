import pygame
import sys
#we are going to have settings for the game
#so we need to make a place for the settings
from settings import *

pygame.init()
#this could be used for velocity, acceleration, position, etc.
vec = pygame.math.Vector2 


#going to have a screen
class App:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        #use a clock to control fps
        self.clock = pygame.time.Clock()
        self.running = True 
        self.state = 'intro'

############################################################################

    def run(self):
        while self.running:
            if self.state == 'intro':
                self.intro_events()
                self.intro_update()
                self.intro_draw()
            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()

#############################################################################

    def intro_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    
#############################################################################

    def intro_update(self):
        pass
    
############################################################################   

    def intro_draw(self):
        pygame.display.update()




