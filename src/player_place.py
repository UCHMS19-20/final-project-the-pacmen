import pygame
from settings import * 
vec = pygame.math.Vector2
######this is where and the how player (PACMAN HIMSELF) in the game could be implented into the actual game#####################
class Player:
    def __init__(self, app, pos):
        self.app = app 
        self.starting_pos = [pos.x, pos.y]
        self.grid_pos = pos 
        self.pix_pos = self.get_pix_pos()
        self.direction = vec(1, 0)
        self.stored_direction = None
        self.able_to_move = True
        self.current_score = 0
        self.speed = 2
        self.lives = 2

#this is check the position of the pacman himself. ALL OF THIS LOCKS PACMAN INTO PLACES IN THE X,Y grid.
    def update(self):
        if self.able_to_move:
             self.pix_pos += self.direction*self.speed
        if self.time_to_move():
            if self.stored_direction != None:
                self.direction = self.stored_direction
            self.able_to_move = self.can_move()
         
       

        #setting grid position in reference to pixel position.  as the player moves, there is something tracking it
        self.grid_pos[0] = (self.pix_pos[0]-TOP_BOTTOM_MARGIN+self.app.cell_width//2)//self.app.cell_width+1
        self.grid_pos[1] = (self.pix_pos[1]-TOP_BOTTOM_MARGIN+self.app.cell_height//2)//self.app.cell_height+1
        
        #this makes pacman eat the coin if he is on the coin using the on_coin and eat_coin functions
        if self.on_coin():
            self.eat_coin()
        #this makes pacman eat the fruit if he is on the fruit using the on_fruit and eat_fruit functions
        if self.on_fruit():
            self.eat_fruit()
    
    
    #draws pacmans shape
    def draw(self):
        pygame.draw.circle(self.app.screen, PLAYER_COLOR, (int(self.pix_pos.x), int(self.pix_pos.y)), self.app.cell_width//2-2)

        for x in range(self.lives):
            pygame.draw.circle(self.app.screen, PLAYER_COLOR, (30 + 20*x, HEIGHT - 15), 7)

    ##################################COIN STUFF########################################################33

    #this function determines if pacman is on a coin or not. This checks to see if the entirety of pacmans body is on the full coin.
    def on_coin(self):
        if self.grid_pos in self.app.coins:
            #pacman has to be on the entirety of the coin in the x direction, grid square doesnt really matter
            if int(self.pix_pos.x+TOP_BOTTOM_MARGIN//2) % self.app.cell_width == 0:
                if self.direction == vec(1,0) or self.direction == vec(-1, 0):
                    return True
            #same in y direction as in x direction
            if int(self.pix_pos.y+TOP_BOTTOM_MARGIN//2) % self.app.cell_height == 0:
                if self.direction == vec(0, 1) or self.direction == vec(0, -1):
                    return True    
        return False
    #this code adds a score of 1 to the current score when pacman eats a coin, and it removes the coin eaten from the maze
    def eat_coin(self):
        self.app.coins.remove(self.grid_pos)
        self.current_score += 1

    ########################################END OF COIN STUFF#####################################


    
   
    #################################FRUIT STUFF###################################################
   
   
    #this code determines if pacman is actually on the fruit or not. If he is not on the fruit he will not eat the fruit
    def on_fruit(self):
        if self.grid_pos in self.app.fruit:
            if int(self.pix_pos.x+TOP_BOTTOM_MARGIN//2) % self.app.cell_width == 0:
                if self.direction == vec(1,0) or self.direction == vec(-1, 0):
                    return True
            
            if int(self.pix_pos.y+TOP_BOTTOM_MARGIN//2) % self.app.cell_height == 0:
                if self.direction == vec(0, 1) or self.direction == vec(0, -1):
                    return True    
        return False
    
    
    #this code adds a score of 200 points to the current score when the pacman eats a fruit, also removes the fruit from the maze
    def eat_fruit(self):
        self.app.fruit.remove(self.grid_pos)
        self.current_score += 200

    ##########################################END OF FRUIT STUFF#####################################33
            


    #determines if the ghost should move
    def move(self, direction):
        self.stored_direction = direction
    
    #determines the pixel position of pacman (actual position on the grid)
    def get_pix_pos(self):
        return vec((self.grid_pos[0]*self.app.cell_width)+TOP_BOTTOM_MARGIN//2+
        self.app.cell_width//2, (self.grid_pos[1]*self.app.cell_height) +
        TOP_BOTTOM_MARGIN//2+self.app.cell_height//2)
        


    #this part makes it pacman cannot move in the x or y direction until he is in a full grid square, he is essentially locked until he is in a full grid square
    def time_to_move(self):
        if int(self.pix_pos.x+TOP_BOTTOM_MARGIN//2) % self.app.cell_width == 0:
            if self.direction == vec(1, 0) or self.direction == vec(-1, 0) or self.direction == vec(0, 0):
                return True
        if int(self.pix_pos.y+TOP_BOTTOM_MARGIN//2) % self.app.cell_height == 0:
            if self.direction == vec(0, 1) or self.direction == vec(0, -1) or self.direction == vec(0, 0):
                return True
    
    
    #this function determines if pacman can move in a certain direction. Is there a wall?
    def can_move(self):
        for wall in self.app.walls:
            if vec(self.grid_pos+self.direction) == wall:
                return False
        return True
