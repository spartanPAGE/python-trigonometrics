import unittest
import app.point as subject

class PointCreationCase(unittest.TestCase):
    def test_creation(self):
        p = subject.Point(5, 6)
        self.assertEqual(p.seq, [5, 6])
        self.assertEqual(p.x, 5)
        self.assertEqual(p.y, 6)

class PointArithmeticsCase(unittest.TestCase):
    def test_addition(self):
        p = subject.Point(5, 6) + subject.Point(-3, 4)
        self.assertEqual(p.seq, [2, 10])

    def test_substraction(self):
        p = subject.Point(5, 6) - subject.Point(-3, 4)
        self.assertEqual(p.seq, [8, 2])

    def test_multiplication(self):
        p = subject.Point(5, 6) * subject.Point(-3, 4)
        self.assertEqual(p.seq, [-3*5, 6*4])

    def test_realdivision(self):
        p = subject.Point(5, 6) / subject.Point(-3, 4)
        self.assertEqual(p.seq, [5/(-3), 6/4])

    def test_floordivision(self):
        p = subject.Point(5, 6) // subject.Point(-3, 4)
        self.assertEqual(p.seq, [5//(-3), 6//4])
