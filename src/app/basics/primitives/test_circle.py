import unittest
import app.basics.primitives.circle as subject

class CircleCreationCase(unittest.TestCase):
    def test_creation(self):
        c = subject.Circle(1, 10, 'white', 'thick')
        self.assertEqual(c.position, 1)
        self.assertEqual(c.radius, 10)
        self.assertEqual(c.color, 'white')
        self.assertEqual(c.thickness, 'thick')
