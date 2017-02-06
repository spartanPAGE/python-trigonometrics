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


class LoopAwareGameMock(test_subject.GameSkeleton):
    def __init__(self, loops):
        super().__init__()
        self.dt = 0
        self.update_counter = 0
        self.draw_counter = 0
        self.DT_STOP_VAL = loops-1

    def fetch_events(self):
        return {'dt': self.dt}

    def fetch_delta_time(self):
        self.dt += 1
        return self.dt

    def consume_events(self, events):
        if events['dt'] == self.DT_STOP_VAL:
            self.stop()

    def update(self, dt):
        self.update_counter += 1

    def draw(self, dt):
        self.draw_counter += 1

class TestGameSkeletonRunningAbility(unittest.TestCase):
    def test_run_is_well_running_properly(self):
        loops = 3
        game = LoopAwareGameMock(loops)
        game.run()
        self.assertTrue(game.draw_counter == game.update_counter == loops)
