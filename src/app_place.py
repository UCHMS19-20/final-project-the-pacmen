import pygame
import sys
#we are going to have settings for the game
#so we need to make a place for the settings
from settings import *
from player_place import*

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
        self.cell_width = MAZE_WIDTH//28
        self.cell_height = MAZE_HEIGHT//30
        self.player = Player(self, PLAYER_START_POS)

        self.load()
############################################################################

    def run(self):
        while self.running:
            if self.state == 'start':
                self.start_events()
                self.start_update()
                self.start_draw()
            elif self.state == 'playing':
                self.playing_events()
                self.playing_update()
                self.playing_draw()
            else:
                self.running = False
            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()

##################### HELP FUNCTIONS ###########################
#helps draw the text and allows us to make it what we want
    def draw_text(self, words, screen, pos, size, color, font_name, centered=False):
        font = pygame.font.SysFont(font_name, size)
        text = font.render(words, False, color)
        text_size = text.get_size()
        if centered:
            pos[0] = pos[0]-text_size[0]//2
            pos[1] = pos[1]-text_size[1]//2
        screen.blit(text, pos)

    def load(self):
        self.background = pygame.image.load('src/background.png')
        self.background = pygame.transform.scale(self.background, (MAZE_WIDTH, MAZE_HEIGHT))

    def draw_grid(self):
        for x in range(WIDTH//self.cell_width):
            pygame.draw.line(self.background, GREY, (x*self.cell_width, 0), (x*self.cell_width, HEIGHT))
        for x in range(HEIGHT//self.cell_height):
            pygame.draw.line(self.background, GREY, (0, x*self.cell_height), (WIDTH, x*self.cell_height))

##########################START FUNCTIONS###################################################

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
        self.draw_text('PUSH THE SPACE BAR BABY', self.screen, [WIDTH//2, HEIGHT//2-50], START_TEXT_SIZE, (168, 130, 60), START_FONT, centered=True)
        self.draw_text('1 PLAYER ONLY', self.screen, [WIDTH//2, HEIGHT//2+50], START_TEXT_SIZE, (31, 100, 136), START_FONT, centered=True)
        self.draw_text('Ms. Gerstein A 3/4', self.screen, [WIDTH//2, HEIGHT//2+100], START_TEXT_SIZE, (168, 130, 60), START_FONT, centered=True)
        self.draw_text('High Score', self.screen, [4,0], START_TEXT_SIZE, (255, 255, 255), START_FONT)
        pygame.display.update() 


##############################playing fuctions#################
    def playing_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                #used to control the player to move around
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.move(vec(-1,0))
                if event.key == pygame.K_RIGHT:
                     self.player.move(vec(1,0))
                if event.key == pygame.K_UP:
                     self.player.move(vec(0,-1))
                if event.key == pygame.K_DOWN:
                     self.player.move(vec(0,1))
    
#############################################################################

    def playing_update(self):
        self.player.update()
    
############################################################################   
#this code draws the text and defines the color, height, font, etc. ALL OF THE GRAPHICS stuff
    def playing_draw(self):
        self.screen.fill(BLACK) 
        #this makes the background collor black
        self.screen.blit(self.background, (TOP_BOTTOM_MARGIN//2, TOP_BOTTOM_MARGIN//2))
        self.draw_grid()
        #draws text once in the actual game
        self.draw_text('CURRENT SCORE: 0', self.screen, [60,0], 18, WHITE, START_FONT)
        self.draw_text('HIGH SCORE: 0', self.screen, [WIDTH//2+60,0], 18, WHITE, START_FONT)
        self.player.draw()
        pygame.display.update() 



