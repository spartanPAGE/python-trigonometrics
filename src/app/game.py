import pygame

import game_skeleton.pygame as pygame_skeleton
PyGameSkeleton = pygame_skeleton.PyGameSkeleton
Guard = pygame_skeleton.SystemGuard

from app.point import Point



class Entity:
    def __init__(self, pos):
        self.pos = pos

    @property
    def position(self):
        return self.pos

class Primitive(Entity):
    def __init__(self, pos, color, thickness):
        super().__init__(pos)
        self.color = color
        self.thickness = thickness

class Line(Primitive):
    def __init__(self, start_pos, end_pos, color, thickness):
        super().__init__(start_pos, color, thickness)
        self.end_pos = end_pos

    @property
    def start_position(self):
        return self.pos

    @property
    def end_position(self):
        return self.end_pos

    def draw(self, dt, display):
        drawing_data = (self.color, self.start_position.seq, self.end_position.seq, self.thickness)
        pygame.draw.line(display, *drawing_data)


class Circle(Primitive):
    def __init__(self, pos, radius, color, thickness):
        super().__init__(pos, color, thickness)
        self.radius = radius

    def draw(self, dt, display):
        drawing_data = (self.color, self.pos.seq, self.radius, self.thickness)
        pygame.draw.circle(display, *drawing_data)

class BorderedCircle(Circle):
    def __init__(self, pos, radius, color, inner_color, thickness):
        super().__init__(pos, radius, color, 0)
        self.inner_circle = Circle(pos, radius-thickness, inner_color, 0)
        self.stored_thickness = thickness

    def draw(self, dt, display):
        for circle in [super(), self.inner_circle]:
            circle.draw(dt, display)


class UnitCircle(BorderedCircle):
    def draw(self, dt, display):
        super().draw(dt, display)

        for i in range(1, 3):
            Line(self.position-Point((i-1)*self.radius, abs(i-2)*self.radius),
                 self.position+Point((i-1)*self.radius, abs(i-2)*self.radius),
                 self.color, self.stored_thickness).draw(dt, display)


class Game(pygame_skeleton.PyGameSkeleton):
    WINDOW_SIZE = (640,)*2
    TITLE = 'trigonometrics'
    ICONTITLE = ''

    def __init__(self):
        super().__init__(*self.WINDOW_SIZE)
        pygame.display.set_caption(self.TITLE, self.ICONTITLE)

    def draw(self, dt):

        UnitCircle(Point(150, 150), 150, (255,)*3, (0,)*3, 5).draw(dt, self.display)
