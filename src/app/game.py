import pygame

import game_skeleton.pygame as pygame_skeleton
PyGameSkeleton = pygame_skeleton.PyGameSkeleton
Guard = pygame_skeleton.SystemGuard

from app.point import Point
from app.basics.primitives import CrossedCircle

class Game(pygame_skeleton.PyGameSkeleton):
    WINDOW_SIZE = (640,)*2
    TITLE = 'trigonometrics'
    ICONTITLE = ''

    def __init__(self):
        super().__init__(*self.WINDOW_SIZE)
        pygame.display.set_caption(self.TITLE, self.ICONTITLE)

    def draw(self, dt):

        CrossedCircle(Point(150, 150), 150, (255,)*3, (0,)*3, 5).draw(dt, self.display)
