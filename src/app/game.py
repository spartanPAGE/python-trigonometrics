import pygame
import game_skeleton.pygame as pygame_skeleton

PyGameSkeleton = pygame_skeleton.PyGameSkeleton
Guard = pygame_skeleton.SystemGuard


from app.point import Point
from app.basics.primitives import CrossedCircle, Line
from app.basics.entity import Entity
from app.entities.fixedlengthline import FixedLengthLine
from app.gui import DisplayClearer, Label
import math

def rads_to_angle(rads):
    return math.degrees(rads)

def fix_angle_to_360(angle, point):
    angle = abs(angle)
    if point.y < 0:
        return 360-angle
    return angle

def angle_text(rads, delta_pos):
    angle = rads_to_angle(rads)
    return 'angle ~~ ' + str(round(fix_angle_to_360(angle, delta_pos), 4))

class Game(pygame_skeleton.PyGameSkeleton):
    TITLE = 'trigonometrics'
    ICONTITLE = ''

    def __init__(self):
        circle = CrossedCircle(Point(150, 150), 150, (255,)*3, (0,)*3, 3)
        super().__init__(circle.diameter, circle.diameter+100)
        pygame.display.set_caption(self.TITLE, self.ICONTITLE)

        mouse_args = ((255, 0, 255), 3, circle.radius,
            lambda: circle.pos,
            lambda: Point(*pygame.mouse.get_pos()),
        )

        self.mouse_pointing_line = FixedLengthLine(*mouse_args)

        self.crossed_circle = circle
        self.font = pygame.font.SysFont("monospace", 15)

        text_supplier = lambda: angle_text(self.mouse_pointing_line.angle_in_rads, self.delta_pos_for_label())
        self.angle_label = Label(Point(30, 30+circle.diameter), self.font, (50, 255, 100), text_supplier)

        self.updatables = [
            self.mouse_pointing_line,
            self.angle_label
        ]

        self.drawables = [
            DisplayClearer((0,)*3),
            self.crossed_circle,
            self.mouse_pointing_line,
            self.angle_label
        ]

    def delta_pos_for_label(self):
        return self.mouse_pointing_line.starting_position - self.mouse_pointing_line.ending_position

    def update(self, dt):
        [updatable.update(dt) for updatable in self.updatables]

    def draw(self, dt):
        [drawable.draw(dt, self.display) for drawable in self.drawables]
