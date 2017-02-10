from app.basics.primitives.circle import Circle

class BorderedCircle(Circle):
    def __init__(self, pos, radius, color, inner_color, thickness):
        super().__init__(pos, radius, color, 0)
        self.inner_circle = Circle(pos, radius-thickness, inner_color, 0)
        self.stored_thickness = thickness

    def draw(self, dt, display):
        for circle in [super(), self.inner_circle]:
            circle.draw(dt, display)
