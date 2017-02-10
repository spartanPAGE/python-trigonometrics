from app.basics.entity import Entity

class Primitive(Entity):
    def __init__(self, pos, color, thickness):
        super().__init__(pos)
        self.color = color
        self.thickness = thickness
