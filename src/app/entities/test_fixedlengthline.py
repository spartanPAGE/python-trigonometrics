import unittest
import app.entities.fixedlengthline as subject
from app.point import Point

class FixedLengthLineCase(unittest.TestCase):
    def test_creation(self):
        color = None
        thickness = None
        length = 5
        spos_supp = lambda: Point(0, 0)
        epos_supp = lambda: Point(5, 0)
        line = subject.FixedLengthLine(color, thickness, spos_supp, epos_supp)

        line.update()
        self.assertEqual(line.length, 5)
        self.assertEqual(line.starting_position, Point(0, 0))
        self.assertEqual(line.ending_position, Point(5, 0))

        line.epos_supp = lambda: Point(3, 0)
        line.update()
        self.assertEqual(line.length, 5)
        self.assertEqual(line.starting_position, Point(0, 0))
        self.assertNotEqual(line.ending_position, Point(0, 0))
