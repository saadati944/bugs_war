import time
import settings
import bugswar

class Bug:
    '''
    this is a Bug !!!
    but not a simple one
    this is an smart one :o
    '''
    def __init__(self, name, x, y):
        
        #position of the bug
        self.X = x
        self.Y = y

        #size of the world
        self.width  = settings.world_width
        self.height = settings.world_height

        #and its name
        self.name = name


    #move character
    def move_left(self):
        if self.X<settings.world_width-1:
            self.X+=1
        time.sleep(settings.wait_after_move)

    def move_right(self):
        if self.X > 0:
            self.X-=1
        time.sleep(settings.wait_after_move)
    
    def move_down(self):
        if self.Y<settings.world_height-1:
            self.Y+=1
        time.sleep(settings.wait_after_move)

    def move_up(self):
        if self.Y > 0:
            self.Y-=1
        time.sleep(settings.wait_after_move)
    
    #scanning a degree
    def scan(self, deg):
        #todo:complete this part
        time.sleep(settings.wait_after_shoot)
    
    def shoot(self, deg):
        #todo:complete this part
        time.sleep(settings.wait_after_shoot)

