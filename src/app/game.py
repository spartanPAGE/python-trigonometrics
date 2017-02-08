import pygame
import game_skeleton.pygame as game

Guard = game.SystemGuard

class Game(game.PyGameSkeleton):
    WINDOW_SIZE = (640,)*2
    TITLE = 'trigonometrics'
    ICONTITLE = ''

    def __init__(self):
        super().__init__(*self.WINDOW_SIZE)
        pygame.display.set_caption(self.TITLE, self.ICONTITLE)

    def draw(self, dt):
        self.display.fill((0, 200, 255))
        pygame.draw.line(self.display, (255, 0, 255), (0, 0), (50, 50), 50)
        self.display.fill((255, 0, 0), (300, 200, 150, 90))
