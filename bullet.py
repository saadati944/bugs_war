import math
import settings


class Bullet:
    def __init__(self, x, y, deg, starttime):
        self.X = x
        self.Y = y

        #convert degree to radians
        self.deg = -(deg * math.pi / 180)

        self.starttime = starttime
    
    def calculatePos(self, time):
        return int(self.X + (time - self.starttime) * math.cos(self.deg)), int(self.Y + (time - self.starttime) * math.sin(self.deg))
    