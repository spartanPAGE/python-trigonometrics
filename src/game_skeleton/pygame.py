from game_skeleton.scaffolding import GameSkeleton
import pygame

def initialize():
    pygame.init()

def finalize():
    pygame.quit()

class SystemGuard:
    def __enter__(self):
        initialize()

    def __exit__(self, type, value, traceback):
        finalize()

class PyGameSkeleton(GameSkeleton):
    DEFAULT_MAX_FPS = 120

    def __init__(self, window_width, window_height):
        super().__init__()
        window_size = (window_width, window_height)
        self.display_surface = pygame.display.set_mode(window_size)
        self.max_fps = self.DEFAULT_MAX_FPS
        self.close_on_quit_event = True
        self.clock =  pygame.time.Clock()

    def fetch_events(self):
        return pygame.event.get()

    def consume_events(self, events):
        is_quit_in_events = any(e for e in events if e.type == pygame.QUIT)
        if(self.close_on_quit_event and is_quit_in_events):
            self.stop()

    @property
    def display(self):
        return self.display_surface

    def fetch_delta_time(self):
        return self.clock.tick(self.max_fps)

    def after_draw(self):
        pygame.display.flip()
