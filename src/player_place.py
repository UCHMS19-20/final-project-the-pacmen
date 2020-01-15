import pygame
from settings import* 
vec = pygame.math.Vector2
######this is where and the how player in the game could be implented#####################
class Player:
    def __init__(self, app, pos):
        self.app = app 
        self.grid_pos = pos 
        self.pix_pos = self.get_pix_pos()
        self.direction = vec(1,0)

    def update(self):
        self.pix_pos += self.direction
        self.grid_pos = (self.pix_pos[0]+TOP_BOTTOM_MARGIN)//self.app.cell_width+1

    def draw(self):
        pygame.draw.circle(self.app.screen, PLAYER_COLOR, (int(self.pix_pos.x), int(self.pix_pos.y)), self.app.cell_width//2-2)
        pygame.draw.rect(self.app.screen, RED, (self.grid_pos[0]*self.app.cell_width+TOP_BOTTOM_MARGIN//2, self.grid_pos[1]*self.app.cell_height+TOP_BOTTOM_MARGIN//2, self.app.cell_width, self.app.cell_height))


    def move(self, direction):
        self.direction = direction
    
    def get_pix_pos(self):
        return vec((self.grid_pos.x*self.app.cell_width)+TOP_BOTTOM_MARGIN//2+
        self.app.cell_width//2, (self.grid_pos.y*self.app.cell_height)+
        TOP_BOTTOM_MARGIN//2+self.app.cell_height//2)
        print(self.grid_pos, self.pix_pos)