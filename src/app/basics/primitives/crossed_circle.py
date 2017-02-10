from app.basics.primitives.bordered_circle import BorderedCircle
from app.point import Point
class CrossedCircle(BorderedCircle):
    def draw(self, dt, display):
        super().draw(dt, display)

        for i in range(1, 3):
            Line(self.position-Point((i-1)*self.radius, abs(i-2)*self.radius),
                 self.position+Point((i-1)*self.radius, abs(i-2)*self.radius),
                 self.color, self.stored_thickness).draw(dt, display)
