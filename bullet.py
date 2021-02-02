import math
import settings


class Bullet:
    def __init__(self, x, y, deg, starttime, shooter):
        self.X = x
        self.Y = y

        #convert degree to radians
        self.deg = -(deg * math.pi / 180)

        self.starttime = starttime
    
        self.shooter = shooter

    def calculatePos(self, time):
        return int(self.X + (time - self.starttime) * settings.related_bullet_speed * math.cos(self.deg)), int(self.Y + (time - self.starttime) * settings.related_bullet_speed * math.sin(self.deg)), self.shooter
    