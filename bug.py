import time
import prop
import math
import bugswar
import settings


class Bug:
    '''
    this is a Bug !!!
    but not a simple one
    this is an smart one :o
    '''

    def __init__(self, name, char, x, y, create_bullet, bugs_list):

        # position of the bug
        self.X = x
        self.Y = y

        # size of the world
        self.width = settings.world_width
        self.height = settings.world_height

        # bugs name and character
        self.name = name
        self.char = char

        # the health level of the bug
        self.health = settings.bug_max_health

        # a function to generate bullets
        self.create_bullet = create_bullet

        # list of all bugs in the world
        self.bugs_list = bugs_list

    # move character

    def move_right(self):
        t = time.time()
        if self.X < settings.world_width-1:
            self.X += 1
            for b in bugswar.bugs_list:
                if b == False or b == self:
                    continue
                if b.X == self.X and b.Y == self.Y:
                    self.X -= 1
                    b.health -= 5
                    self.health -= 5
                    break
        time.sleep(abs(settings.wait_after_move - (time.time() - t)))

    def move_left(self):
        t = time.time()
        if self.X > 0:
            self.X -= 1
            for b in bugswar.bugs_list:
                if b == False or b == self:
                    continue
                if b.X == self.X and b.Y == self.Y:
                    self.X += 1
                    b.health -= 5
                    self.health -= 5
                    break
        time.sleep(abs(settings.wait_after_move - (time.time() - t)))

    def move_down(self):
        t = time.time()
        if self.Y < settings.world_height-1:
            self.Y += 1
            for b in bugswar.bugs_list:
                if b == False or b == self:
                    continue
                if b.X == self.X and b.Y == self.Y:
                    self.Y -= 1
                    b.health -= 5
                    self.health -= 5
                    break
        time.sleep(abs(settings.wait_after_move - (time.time() - t)))

    def move_up(self):
        t = time.time()
        if self.Y > 0:
            self.Y -= 1
            for b in bugswar.bugs_list:
                if b == False or b == self:
                    continue
                if b.X == self.X and b.Y == self.Y:
                    self.Y += 1
                    b.health -= 5
                    self.health -= 5
                    break
        time.sleep(abs(settings.wait_after_move - (time.time() - t)))

    # scanning a degree
    def scan(self, deg):
        t = time.time()
        deg = -(deg * math.pi / 180)
        points = [prop.point(self.X, self.Y)]
        i = 1
        while points[len(points)-1].x < settings.world_width and points[len(points)-1].y < settings.world_height and points[len(points)-1].x >= 0 and points[len(points)-1].y >= 0:
            points.append(prop.point(
                int(self.X + (i) * math.cos(deg)), int(self.Y + (i) * math.sin(deg))))
            i += 1

        for b in self.bugs_list:
            if b == False or b==self:
                continue
            if prop.point(b.X, b.Y) in points:
                return True

        time.sleep(abs(settings.wait_after_move - (time.time() - t)))

    def shoot(self, deg):
        t = time.time()
        self.create_bullet(self.X, self.Y, deg)
        time.sleep(abs(settings.wait_after_move - (time.time() - t)))
