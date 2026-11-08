import unittest
from inventory.store import Store


class T(unittest.TestCase):
    def test_add(self):
        s = Store()
        s.add("apple", 2)
        s.add("apple", 3)
        self.assertEqual(s.count("apple"), 5)
