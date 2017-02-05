import unittest

import game_skeleton.scaffolding as test_subject

class GameMock(test_subject.GameSkeleton):
    def __init__(self):
        super().__init__()


class TestGameSkeleton(unittest.TestCase):

    def test_is_running_right_after_creation(self):
        self.assertTrue(GameMock().is_running)
