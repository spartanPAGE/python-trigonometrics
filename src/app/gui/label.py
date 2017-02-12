from app.basics.entity import Entity

class Label(Entity):
    def __init__(self, pos, font, color, text_supplier):
        super().__init__(pos)
        self.font = font
        self.color = color
        self.text_supplier = text_supplier
        self.text = ''
        self.text_surface = None

    def generate_text_surface(self, antialiasing_flag=1):
        render_data = (self.text, antialiasing_flag, self.color)
        self.text_surface = self.font.render(*render_data)

    def update(self, dt):
        text = self.text_supplier()
        if(text != self.text):
            self.text = text
            self.generate_text_surface()

    def draw(self, dt, display):
        display.blit(self.text_surface, tuple(self.pos.seq))
