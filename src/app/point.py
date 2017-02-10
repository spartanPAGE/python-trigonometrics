class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def seq(self):
        return [self.x, self.y]


    @staticmethod
    def apply_mk_new(self, other, unit_func):
        return Point(unit_func(self.x, other.x), unit_func(self.y, other.y))

    def __add__(self, other):
        return Point.apply_mk_new(self, other, lambda x, y: x+y)

    def __sub__(self, other):
        return Point.apply_mk_new(self, other, lambda x, y: x-y)

    def __mul__(self, other):
        return Point.apply_mk_new(self, other, lambda x, y: x*y)

    def __truediv__(self, other):
        return Point.apply_mk_new(self, other, lambda x, y: x/y)

    def __floordiv__(self, other):
        return Point.apply_mk_new(self, other, lambda x, y: x//y)