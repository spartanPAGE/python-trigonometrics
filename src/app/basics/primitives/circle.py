from app.basics.primitive import Primitive
import pygame

class Circle(Primitive):
    def __init__(self, pos, radius, color, thickness):
        super().__init__(pos, color, thickness)
        self.radius = radius

    def draw(self, dt, display):
        drawing_data = (self.color, self.pos.seq, self.radius, self.thickness)
        pygame.draw.circle(display, *drawing_data)
