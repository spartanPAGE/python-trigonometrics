import unittest
import app.basics.entity as subject

class EntityCreationCase(unittest.TestCase):
    def test_creation(self):
        e = subject.Entity(5)
        self.assertEqual(e.pos, e.position)
        self.assertEqual(e.pos, 5)
        e.pos = 10
        self.assertEqual(e.pos, 10)
