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
        self.state = 'start'

############################################################################

    def run(self):
        while self.running:
            if self.state == 'intro':
                self.start_events()
                self.start_update()
                self.start_draw()
            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()

##################### HELP FUNCTIONS ###########################
#helps draw the text and allows us to make it what we want
    def draw_text(self, words, screen, pos, size, color, font_name):
        font = pygame.font.SysFont(font_name, size)
        text = font.render(words, False, color)
        text_size = text.get_size()
        screen.blit(text, pos)


#############################################################################

    def intro_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.state = 'playing'
    
#############################################################################

    def start_update(self):
        pass
    
############################################################################   

    def start_draw(self): 
        #this makes the background collor black
        self.screen.fill(BLACK)
        self.draw_text('CLICK SPACE BAR', self.screen, (210, HEIGHT//2), START_TEXT_SIZE, (168, 130, 60), START_FONT)
        pygame.display.update()




