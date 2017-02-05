import unittest

import game_skeleton.scaffolding as test_subject

class GameMock(test_subject.GameSkeleton):
    def __init__(self):
        super().__init__()

    def fetch_events(self):
        return ["example event", "foo", "bar"]

    def consume_events(self, events):
        self.is_example_event_in_events = "example event" in events


class TestGameSkeleton(unittest.TestCase):
    def test_is_running_right_after_creation(self):
        self.assertTrue(GameMock().is_running)

    def test_is_not_running_right_after_stop(self):
        game = GameMock()
        game.stop()
        self.assertFalse(game.is_running)

    def test_events_are_streamed_properly(self):
        game = GameMock()
        game.stream_events()
        self.assertTrue(game.is_example_event_in_events)
