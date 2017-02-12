class DisplayClearer:
    def __init__(self, color):
        self.color = color

    def draw(self, dt, display):
        display.fill(self.color)
