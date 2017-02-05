from toolz.functoolz import pipe

class GameSkeleton:

    def __init__(self):
        self.is_running = True

    def stop():
        self.is_running = False

    def fetch_events():
        return []

    def consume_events(e):
        pass

    def fetch_delta_time():
        return 0

    def update(dt):
        pass

    def run():
        while self.is_running:
            pipe(self.fetch_events(), self.consume_events)
            pipe(self.fetch_delta_time(), self.update)
