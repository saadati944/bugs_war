
class Prop:
    def __init__(self, name, char, x, y):
        self.name = name
        self.char = char
        self.x = x
        self.y = y

class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y