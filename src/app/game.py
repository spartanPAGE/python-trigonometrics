import pygame
import game_skeleton.pygame as pygame_skeleton
PyGameSkeleton = pygame_skeleton.PyGameSkeleton
Guard = pygame_skeleton.SystemGuard

from app.point import Point
from app.basics.primitives import CrossedCircle, Line

class MousePoitingLine(Line):
    def __init__(self, pos, color, thickness):
        super().__init__(pos, pos, color, thickness)

    def update(self, dt):
        p = pygame.mouse.get_pos()
        self.ending_position = Point(*tuple(p))

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
        self.mouse_pointing_line = MousePoitingLine(Point(150, 150), (255, 0, 255), 3)
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
