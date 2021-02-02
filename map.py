import settings, time


class Char:
    def __init__(self, ch):
        self.char = ch


class Map:
    def __init__(self):
        self.reset()

    def add_point(self, x:int, y:int, char:str):
        self.blocks[y][x] = Char(char)

    def reset(self):
        self.blocks = []
        for i in range(settings.world_height):
            self.blocks.append([])
        for i in range(settings.world_height):
            for j in range(settings.world_width):
                self.blocks[i].append(Char(' '))

    def get_map(self) -> str:
        m = ''
        for i in range(settings.world_height):
            for j in range(settings.world_width):
                m += self.blocks[i][j].char
            m += '\n'
        return m