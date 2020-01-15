######this is where and the how player in the game could be implented#####################
class Player:
    def __init__(self, app, pos):
        self.app = app 
        self.grid_pos = pos 
    self.pix_pos = vec((self.gid_pos.x*self.app.cell_width)+TOP_BOTTOM_MARGIN,
     (self.grid_pos.y*self.app.cell_height)+TOP_BOTTOM_MARGIN)
    print(self.grid_pos, self.pix_pos)

