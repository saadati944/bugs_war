
class Point:
    def __init__(self, x: int, y: int, chr: str = ''):
        self.x = x
        self.y = y
        self.chr = chr

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Map:
    def __init__(self):
        self.points = []

    def add_point(self, point: Point):
        self.points.append(point)

    def reset(self):
        self.points = []

    def get_map(self, width: int, height: int) -> str:
        m = ''
        for i in range(width):
            for j in range(height):
                ind = self.indexof(Point(i, j))
                if ind >= 0:
                    m += self.points[ind].chr
                else:
                    m += ' '
            m += '\n'
        return m

    def indexof(self, point:Point):
        for i in range(len(self.points)):
            if self.points[i] == point:
                return i
        return -1