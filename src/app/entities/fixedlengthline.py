from app.basics.primitives import Line
import math

class FixedLengthLine(Line):
    def __init__(self, color, thickness, length, spos_supplier, epos_supplier):
        super().__init__(None, None, color, thickness)
        self.length = length
        self.spos_supplier = spos_supplier
        self.epos_supplier = epos_supplier

    def update(self, *_):
        self.starting_position = self.spos_supplier()
        self.ending_position = self.epos_supplier()
        self.fix_length()

    def fix_length(self):
        delta_pos = self.ending_position - self.starting_position
        alpha = self.angle_in_rads
        x = self.length * math.cos(alpha)
        y = self.length * math.sin(alpha)
        self.ending_position = Point(x, y)+self.starting_position

    @property
    def angle_in_rads(self):
        delta_pos = self.ending_position - self.starting_position
        return math.atan2(delta_pos.y, delta_pos.x)
