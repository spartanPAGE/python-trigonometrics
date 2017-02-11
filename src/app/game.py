import pygame
import game_skeleton.pygame as pygame_skeleton
PyGameSkeleton = pygame_skeleton.PyGameSkeleton
Guard = pygame_skeleton.SystemGuard
import math

from app.point import Point
from app.basics.primitives import CrossedCircle, Line
from app.entity import Entity

class FixedLengthMousePoitingLine(Line):
    def __init__(self, pos, color, thickness, length):
        super().__init__(pos, pos, color, thickness)
        self.length = length

    def update(self, *_):
        self.ending_position = Point(*pygame.mouse.get_pos())
        self.fix_length()

    def fix_length(self):
        delta_pos = self.ending_position - self.starting_position
        alpha = self.angle_in_rads
        x = delta_pos.x + self.length * math.cos(alpha)
        y = delta_pos.y + self.length * math.sin(alpha)
        self.ending_position = Point(x, y)+self.starting_position

    @property
    def angle_in_rads(self):
        delta_pos = self.ending_position - self.starting_position
        return math.atan2(delta_pos.y, delta_pos.x)

class Label(Entity):
    pass

class DisplayClearer:
    def __init__(self, color):
        self.color = color

    def draw(self, dt, display):
        display.fill(self.color)


class Game(pygame_skeleton.PyGameSkeleton):
    TITLE = 'trigonometrics'
    ICONTITLE = ''

    def __init__(self):
        self.crossed_circle = CrossedCircle(Point(150, 150), 150, (255,)*3, (0,)*3, 3)
        self.mouse_pointing_line = FixedLengthMousePoitingLine(Point(150, 150), (255, 0, 255), 3, self.crossed_circle.radius)
        super().__init__(*((self.crossed_circle.radius*2,)*2))
        pygame.display.set_caption(self.TITLE, self.ICONTITLE)

        self.updatables = [
            self.mouse_pointing_line
        ]

        self.drawables = [
            DisplayClearer((0,)*3),
            self.crossed_circle,
            self.mouse_pointing_line
        ]


    def update(self, dt):
        [updatable.update(dt) for updatable in self.updatables]

    def draw(self, dt):
        [drawable.draw(dt, self.display) for drawable in self.drawables]
