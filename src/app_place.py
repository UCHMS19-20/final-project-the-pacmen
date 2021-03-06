import pygame
import sys
import copy
#we are going to have settings for the game
#so we need to make a place for the settings
from settings import *
from player_place import *
from enemy_place import *

pygame.init()
#this could be used for velocity, acceleration, position, etc.
vec = pygame.math.Vector2 


#contains all of the stuff necessary for the game to run
class App:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        #use a clock to control fps
        self.clock = pygame.time.Clock()
        self.running = True 
        self.state = 'start'
        self.cell_width = MAZE_WIDTH//COLS
        self.cell_height = MAZE_HEIGHT//ROWS
        self.walls = []
        self.coins = []
        self.fruit = []
        self.enemies = []
        self.e_pos = []
        self.p_pos = None
        self.load()
        self.player = Player(self, vec(self.p_pos))
        self.make_enemies()

       

      
############################################################################
    #this block of code is checking everything so everything RUNS on the screen properly 
    def run(self):
        while self.running:
            #this starts the whole game up
            if self.state == 'start':
                self.start_events()
                self.start_update()
                self.start_draw()
            #this displays everything on the screen necessary while the game is actually happening
            elif self.state == 'playing':
                self.playing_events()
                self.playing_update()
                self.playing_draw()
            #this displays everything on the screen necessary for when the game is over
            elif self.state == 'game over':
                self.game_over_events()
                self.game_over_update()
                self.game_over_draw()
            #this displays everythig on the screen for when the user WINS the game
            elif self.state == 'win':
                self.game_win_events()
                self.game_win_update()
                self.game_win_draw()
            else:
                self.running = False
            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()

##################### HELP FUNCTIONS ###########################
#helps draw the text and allows us to make it what we want (colors, location, font, etc)
    def draw_text(self, words, screen, pos, size, color, font_name, centered=False):
        font = pygame.font.SysFont(font_name, size)
        text = font.render(words, False, color)
        text_size = text.get_size()
        if centered:
            pos[0] = pos[0]-text_size[0]//2
            pos[1] = pos[1]-text_size[1]//2
        screen.blit(text, pos)
    #loads the pacman maze image and makes the screen fit
    def load(self):
        self.background = pygame.image.load('src/background.png')
        self.background = pygame.transform.scale(self.background, (MAZE_WIDTH, MAZE_HEIGHT))
        
        #opening the walls file and creating walls list with coordinates of walls
        with open("walls.txt", 'r') as file:
            for yidx, line in enumerate(file):
                for xidx, char in enumerate(line):
                    # 1's are equivalent to where walls are located
                    if char == "1":
                        self.walls.append(vec(xidx, yidx))
                    # C's are equivalent to where coins are located
                    elif char == "C":
                        self.coins.append(vec(xidx, yidx))
                    # P is equivalent to where pacman is located
                    elif char == "P":
                        self.p_pos = [xidx, yidx]
                    #these numbers are equivalent to the ghosts positions on the boardgame
                    elif char in ["2", "3", "4", "5"]:
                        self.e_pos.append([xidx, yidx])
                    # H is equivalent to the holes in the wall where the enemies start
                    elif char == "H":
                        pygame.draw.rect(self.background, BLACK, (xidx*self.cell_width, yidx*self.cell_height, self.cell_width, self.cell_height))
                    # F is equivalent to where the fruit is located
                    elif char == "F":
                        self.fruit.append(vec(xidx, yidx))

    #makes the enemies in location
    def make_enemies(self):
        for idx, pos in enumerate(self.e_pos):
            self.enemies.append(Enemy(self, vec(pos), idx))
    
    #this code draws the grid of the game and makes the paths, but the grid is not shown
    def draw_grid(self):
        for x in range(WIDTH//self.cell_width):
            pygame.draw.line(self.background, GREY, (x*self.cell_width, 0), (x*self.cell_width, HEIGHT))
        for x in range(HEIGHT//self.cell_height):
            pygame.draw.line(self.background, GREY, (0, x*self.cell_height), (WIDTH, x*self.cell_height))




##########################START FUNCTIONS###################################################
    
    #this is what starts the game when the player wants to reset it, all of the starting positions of enemies, coins, pacman, etc.
    
    def reset(self):
        self.player.lives = 2
        self.player.current_score = 0
        self.player.grid_pos = vec(self.player.starting_pos)
        self.player.pix_pos = self.player.get_pix_pos()
        self.player.direction *= 0 
        for enemy in self.enemies:
            enemy.grid_pos = vec(enemy.starting_pos)
            enemy.pix_pos = enemy.get_pix_pos()
            enemy.direction *= 0
        
        
        #this bit of code is checking where the coin is on the walls.txt grid
        self.coins = []
        self.fruit = []

        with open("walls.txt", 'r') as file:
            for yidx, line in enumerate(file):
                for xidx, char in enumerate(line):
                    if char == 'C':
                        self.coins.append(vec(xidx, yidx))
        self.state = "playing"

        #this code is checking where the fruit is on the walls.txt grid
        with open("walls.txt", 'r') as file:
            for yidx, line in enumerate(file):
                for xidx, char in enumerate(line):
                    if char == 'F':
                        self.fruit.append(vec(xidx, yidx))
        self.state = "playing"


    #this determines if the user has started the game or not
    def start_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            #if spacebar is pushed down, game starts
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.state = 'playing'
    
#############################################################################

    def start_update(self):
        pass
    
###################START SCREEN########################



#this code draws the text and defines the color, height, font, etc. ALL OF THE GRAPHICS stuff
    def start_draw(self): 
        #makes the background screen black
        self.screen.fill(BLACK)
        #intro screen stuff
        self.draw_text('PUSH THE SPACE BAR BABY', self.screen, [WIDTH//2, HEIGHT//2-50], START_TEXT_SIZE, (168, 130, 60), START_FONT, centered=True)
        self.draw_text('1 PLAYER ONLY', self.screen, [WIDTH//2, HEIGHT//2+50], START_TEXT_SIZE, (31, 100, 136), START_FONT, centered=True)
        self.draw_text('Ms. Gerstein A 3/4', self.screen, [WIDTH//2, HEIGHT//2+100], START_TEXT_SIZE, (168, 130, 60), START_FONT, centered=True)

        pygame.display.update() 

#############END OF START SCREEN###################




##############################playing fuctions(while the game is going on)#################

#all of this code gives the user the ability to control pacman during the game. ALL OF THIS IS WHILE THE GAME IS GOING ON
    def playing_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                #allows the user to use arrow keys to move pacman around using the arrow keys
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.move(vec(-1, 0))
                if event.key == pygame.K_RIGHT:
                     self.player.move(vec(1, 0))
                if event.key == pygame.K_UP:
                     self.player.move(vec(0, -1))
                if event.key == pygame.K_DOWN:
                     self.player.move(vec(0, 1))
    

    #updates enemies
    def playing_update(self):
        self.player.update()
        for enemy in self.enemies:
            enemy.update()
        #if the ghost touches pacman, remove a life
        for enemy in self.enemies:
            if enemy.grid_pos == self.player.grid_pos:
                self.remove_life()
         
        #if the user eats all the coins and fruit, the score will be 1083, ending the game and making the win screen
        if self.player.current_score == 1083:
            self.state = "win"

    #########END OF PLAYING FUNCTIONS#############


    
############################################################################   
#this code draws the text and defines the color, height, font, etc. ALL OF THE GRAPHICS stuff
    def playing_draw(self):
        self.screen.fill(BLACK) 
        #this makes the background collor black
        self.screen.blit(self.background, (TOP_BOTTOM_MARGIN//2, TOP_BOTTOM_MARGIN//2))
        #draws coins
        self.draw_coins()
        #draws fruit
        self.draw_fruit()
        

        #draws text once in the actual game
        self.draw_text('CURRENT SCORE: {}'.format(self.player.current_score), self.screen, [200,0], 18, WHITE, START_FONT)
        
        #draws stuff shown
        self.player.draw()
        for enemy in self.enemies:
            enemy.draw()
        pygame.display.update() 

    #game checks if the number of lives is 0, if num of lives is 0, game over
    def remove_life(self):
        self.player.lives -= 1
        if self.player.lives == 0:
            self.state = "game over"
        #if lives dont equal 0, the game restarts with the amount of lives lost subtracted from 3
        else:
            self.player.grid_pos = vec(self.player.starting_pos)
            self.player.pix_pos = self.player.get_pix_pos()
            self.player.direction *= 0
            for enemy in self.enemies:
                enemy.grid_pos = vec(enemy.starting_pos)
                enemy.pix_pos = enemy.get_pix_pos()
                enemy.direction *= 0
    


    #this here allows the game to draw the coins in which the player could collect 
    def draw_coins(self):
        for coin in self.coins:
            pygame.draw.circle(self.screen, (252, 2, 0), (int(coin.x*self.cell_width)+self.cell_width//2+TOP_BOTTOM_MARGIN//2, int(coin.y*self.cell_height)+self.cell_height//2+TOP_BOTTOM_MARGIN//2), 5)
    
    #this here allows the game to draw the fruit in which the player could collect for 200 points
    def draw_fruit(self):
        for fruit in self.fruit:
            pygame.draw.circle(self.screen, (255, 255, 255), (int(fruit.x*self.cell_width)+self.cell_width//2+TOP_BOTTOM_MARGIN//2, int(fruit.y*self.cell_height)+self.cell_height//2+TOP_BOTTOM_MARGIN//2), 5)

#################################WINNING THE GAME STUFF######################################################


    #this code gives the user options to choose what they want to do if they win the game. play again? quit?
    def game_win_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.reset()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False
    

    #did player win?
    def game_win_update(self):
        pass

    #all of this code draws the winner screen once the game of pacman is won, all the coins eaten
    def game_win_draw(self):
        self.screen.fill(BLACK)
        quit_text = "Press ESC to QUIT"
        again_text = "Press SPACE to PLAY AGAIN"
        self.draw_text("YOU WIN!!!", self.screen, [WIDTH//2, 100], 52, GREEN, "arial", centered=True)
        self.draw_text(again_text, self.screen, [WIDTH//2, HEIGHT//2], 36, (190, 190, 190), "arial", centered=True)   
        self.draw_text(quit_text, self.screen, [WIDTH//2, HEIGHT//1.5], 36, (190, 190, 190), "arial", centered=True)
        pygame.display.update()  
    
    #################################END OF THE WINNING GAME STUFF##############################################

    #################################GAME OVER STUFF########################################################
    # this describes how the player can replay or exit the game
    def game_over_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.reset()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False


    #did player lose?
    def game_over_update(self):
        pass

    # this is for when the player loses all of their lives. This code just displays text on the screen asking the player what the would like to do after they lose the game (ending screen)
    def game_over_draw(self):
        self.screen.fill(BLACK)
        quit_text = "Press ESC to QUIT"
        again_text = "Press SPACE to PLAY AGAIN"
        self.draw_text("GAME OVER  ¯\_(:/)_/¯", self.screen, [WIDTH//2, 100], 52, RED, "arial", centered=True)
        self.draw_text(again_text, self.screen, [WIDTH//2, HEIGHT//2], 36, (190, 190, 190), "arial", centered=True)   
        self.draw_text(quit_text, self.screen, [WIDTH//2, HEIGHT//1.5], 36, (190, 190, 190), "arial", centered=True)
        pygame.display.update()   


    ##############################END OF GAME OVER STUFF##############################################################3

    