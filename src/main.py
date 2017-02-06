import pygame
import game_skeleton.pygame as game

class App(game.PyGameSkeleton):
    WINDOW_SIZE = (640,)*2

    def __init__(self):
        super().__init__(*self.WINDOW_SIZE)

    def draw(self, dt):
        self.display.fill((0, 200, 255))
        self.display.fill((255, 0, 0), (300, 200, 150, 90))


def main():
    with game.SystemGuard():
        App().run()

if __name__ == "__main__":
    main()
