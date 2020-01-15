#these are the screen setings
#makes the margins for the test on the maze
from pygame.math import Vector2 as vec 

WIDTH, HEIGHT = 610, 670
FPS = 60
TOP_BOTTOM_MARGIN = 50
MAZE_WIDTH, MAZE_HEIGHT = WIDTH-TOP_BOTTOM_MARGIN, HEIGHT-TOP_BOTTOM_MARGIN

#color settings
BLACK = (0,0,0)
RED = (208,22,22)
GREY = (107, 107, 107)
WHITE = (255, 255, 255)
PLAYER_COLOR = (190, 194, 15) 
# font settings
START_TEXT_SIZE = 14
START_FONT = 'arial black'


#player settings
PLAYER_START_POS = vec(13, 17)

#enemy settings
