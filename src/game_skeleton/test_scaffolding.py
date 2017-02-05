import unittest

import game_skeleton.scaffolding as test_subject

class TestGameSkeleton(unittest.TestCase):
    def test_is_running_right_after_creation(self):
        self.assertTrue(test_subject.GameSkeleton().is_running)

    def test_is_not_running_right_after_stop(self):
        game = test_subject.GameSkeleton()
        game.stop()
        self.assertFalse(game.is_running)


class GameMockWithEvents(test_subject.GameSkeleton):
    def fetch_events(self):
        return ["example event", "foo", "bar"]

    def consume_events(self, events):
        self.is_example_event_in_events = "example event" in events

class TestGameSkeletonEventsStreaming(unittest.TestCase):
    def test_events_are_streamed_properly(self):
        game = GameMockWithEvents()
        game.stream_events()
        self.assertTrue(game.is_example_event_in_events)


class TimeAwareGameMock(test_subject.GameSkeleton):
    def __init__(self):
        super().__init__()
        self.dt = 0

    def fetch_delta_time(self):
        self.dt += 1
        return self.dt

    def update(self, dt):
        self.dt_of_last_update = dt

    def draw(self, dt):
        self.dt_of_last_draw = dt

class TestGameSkeletonTimeStreaming(unittest.TestCase):
    def test_time_is_streamed_properly(self):
        game = TimeAwareGameMock()
        self.assertEqual(game.dt, 0)

        for i in range(1, 5):
            game.stream_time()
            self.assertEqual(i, game.dt_of_last_update)
            self.assertEqual(i, game.dt_of_last_draw)
