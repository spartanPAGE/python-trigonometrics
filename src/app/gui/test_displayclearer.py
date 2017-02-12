import unittest
import app.gui.displayclearer as subject

class GoodAssertion(Exception):
    pass

class DisplayMock:
    def __init__(self, required_color_supplier):
        self.required_color_supplier = required_color_supplier

    def fill(self, color):
        if color == self.required_color_supplier():
            raise GoodAssertion()


class DisplayClearerTestCase(unittest.TestCase):
    def test_essential(self):
        display_clearer = subject.DisplayClearer((255, 0, 00))
        display_mock = DisplayMock(lambda: (255, 0, 00))
        with self.assertRaises(GoodAssertion):
            display_clearer.draw(None, display_mock)
