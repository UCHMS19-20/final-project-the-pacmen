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
            if self.state == 'start':
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
        pos[0] = pos[0]-text_size[0]//2
        pos[1] = pos[1]-text_size[1]//2
        screen.blit(text, pos)


#############################################################################

    def start_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.state = 'playing'
    
#############################################################################

    def start_update(self):
        pass
    
############################################################################   
#this code draws the text and defines the color, height, font, etc. ALL OF THE GRAPHICS stuff
    def start_draw(self): 
        #this makes the background collor black
        self.screen.fill(BLACK)
        self.draw_text('PUSH THE SPACE BAR BABY', self.screen, [WIDTH//2, HEIGHT//2], START_TEXT_SIZE, (168, 130, 60), START_FONT)
        pygame.display.update()



