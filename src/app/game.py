import pygame
import game_skeleton.pygame as game

Guard = game.SystemGuard

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def seq(self):
        return [self.x, self.y]

class Entity:
    def __init__(self, pos):
        self.pos = pos

    @property
    def position(self):
        return this.pos

class Primitive(Entity):
    def __init__(self, pos, color):
        super().__init__(pos)
        self.color = color

class Circle(Primitive):
    def __init__(self, pos, radius, color, thickness):
        super().__init__(pos, color)
        self.radius = radius
        self.thickness = thickness

    def draw(self, dt, display):
        drawing_data = (self.color, self.pos.seq, self.radius, self.thickness)
        pygame.draw.circle(display, *drawing_data)

class BorderedCircle(Circle):
    def __init__(self, pos, radius, color, inner_color, thickness):
        super().__init__(pos, radius, color, 0)
        self.inner_circle = Circle(pos, radius-thickness, inner_color, 0)

    def draw(self, dt, display):
        for circle in [super(), self.inner_circle]:
            circle.draw(dt, display)


class Game(game.PyGameSkeleton):
    WINDOW_SIZE = (640,)*2
    TITLE = 'trigonometrics'
    ICONTITLE = ''

    def __init__(self):
        super().__init__(*self.WINDOW_SIZE)
        pygame.display.set_caption(self.TITLE, self.ICONTITLE)

    def draw(self, dt):

        BorderedCircle(Point(150, 150), 150, (255,)*3, (0,)*3, 25).draw(dt, self.display)
