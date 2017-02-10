import unittest
import app.basics.primitives.line as subject

class LineCreationCase(unittest.TestCase):
    def test_creation(self):
        l = subject.Line(1, 10, 'white', 'thick')
        self.assertEqual(l.starting_position, 1)
        self.assertEqual(l.ending_position, 10)
        self.assertEqual(l.color, 'white')
        self.assertEqual(l.thickness, 'thick')
