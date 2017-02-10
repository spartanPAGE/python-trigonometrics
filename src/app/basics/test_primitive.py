import unittest
import app.basics.primitive as subject

class PrimitiveCreationCase(unittest.TestCase):
    def test_creation(self):
        p = subject.Primitive(5, 'green', 'thick')
        self.assertEqual(p.pos, p.position)
        self.assertEqual(p.pos, 5)
        self.assertEqual(p.color, 'green')
        self.assertEqual(p.thickness, 'thick')
