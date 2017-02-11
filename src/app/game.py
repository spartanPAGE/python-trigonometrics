import pygame
import game_skeleton.pygame as pygame_skeleton
PyGameSkeleton = pygame_skeleton.PyGameSkeleton
Guard = pygame_skeleton.SystemGuard
import math

from app.point import Point
from app.basics.primitives import CrossedCircle, Line
from app.basics.entity import Entity

class FixedLengthMousePointingLine(Line):
    def __init__(self, pos, color, thickness, length):
        super().__init__(pos, pos, color, thickness)
        self.length = length

    def update(self, *_):
        self.ending_position = Point(*pygame.mouse.get_pos())
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

class Label(Entity):
    def __init__(self, pos, font, color, text_supplier):
        super().__init__(pos)
        self.font = font
        self.color = color
        self.text_supplier = text_supplier
        self.text = ''
        self.text_surface = None

    def generate_text_surface(self, antialiasing_flag=1):
        self.text_surface = self.font.render(self.text, antialiasing_flag, color)

    def update(self, dt):
        text = self.text_supplier()
        if(text != self.text):
            self.text = text
            self.generate_text_surface()

    def draw(self, dt, display):
        display.blit(self.text_surface, self.pos)

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
        self.mouse_pointing_line = FixedLengthMousePointingLine(Point(150, 150), (255, 0, 255), 3, self.crossed_circle.radius)
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
