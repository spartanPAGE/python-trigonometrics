import unittest
import app.basics.primitives.bordered_circle as subject

class CircleCreationCase(unittest.TestCase):
    def test_creation(self):
        c = subject.BorderedCircle(1, 10, 'white', 'black', 3)
        self.assertEqual(c.position, 1)
        self.assertEqual(c.radius, 10)
        self.assertEqual(c.color, 'white')
        self.assertEqual(c.thickness, 0)
        self.assertEqual(c.stored_thickness, 3)

        self.assertEqual(c.inner_circle.pos, 1)
        self.assertEqual(c.inner_circle.radius, 10-3)
        self.assertEqual(c.inner_circle.color, 'black')
        self.assertEqual(c.inner_circle.thickness, 0)
