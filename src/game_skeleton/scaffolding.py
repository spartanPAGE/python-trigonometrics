from toolz.functoolz import pipe

class GameSkeleton:

    def __init__(self):
        self.is_running = True

    def stop(self):
        self.is_running = False

    def fetch_events(self):
        return []

    def consume_events(self, e):
        pass

    def fetch_delta_time(self):
        return 0

    def update(self, dt):
        pass

    def draw(self, dt):
        pass

    def stream_events(self):
        pipe(self.fetch_events(), self.consume_events)

    def stream_time(self):
        pipe(self.fetch_delta_time(), self.update)
        pipe(self.fetch_delta_time(), self.draw)

    def run(self):
        while self.is_running:
            self.stream_events()
            self.stream_time()
