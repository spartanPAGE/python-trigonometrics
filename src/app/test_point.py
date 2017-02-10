import unittest
import app.point as test_subject

class PointTestCase(unittest.TestCase):
    subject = test_subject

class PointCreationCase(PointTestCase):
    def test_creation(self):
        p = self.subject.Point(5, 6)
        self.assertEqual(p.seq, [5, 6])
        self.assertEqual(p.x, 5)
        self.assertEqual(p.y, 6)

class PointArithmeticsCase(PointTestCase):
    def test_addition(self):
        p = self.subject.Point(5, 6) + self.subject.Point(-3, 4)
        self.assertEqual(p.seq, [2, 10])

    def test_substraction(self):
        p = self.subject.Point(5, 6) - self.subject.Point(-3, 4)
        self.assertEqual(p.seq, [8, 2])

    def test_multiplication(self):
        p = self.subject.Point(5, 6) * self.subject.Point(-3, 4)
        self.assertEqual(p.seq, [-3*5, 6*4])

    def test_realdivision(self):
        p = self.subject.Point(5, 6) / self.subject.Point(-3, 4)
        self.assertEqual(p.seq, [5/(-3), 6/4])

    def test_floordivision(self):
        p = self.subject.Point(5, 6) // self.subject.Point(-3, 4)
        self.assertEqual(p.seq, [5//(-3), 6//4])
