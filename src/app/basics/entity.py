class Entity:
    def __init__(self, pos):
        self.pos = pos

    @property
    def position(self):
        return self.pos
