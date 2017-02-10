from app.basics.primitive import Primitive
import pygame

class Line(Primitive):
    def __init__(self, start_pos, end_pos, color, thickness):
        super().__init__(start_pos, color, thickness)
        self.end_pos = end_pos

    @property
    def starting_position(self):
        return self.pos

    @property
    def ending_position(self):
        return self.end_pos

    def draw(self, dt, display):
        drawing_data = (self.color, self.starting_position.seq, self.ending_position.seq, self.thickness)
        pygame.draw.line(display, *drawing_data)
