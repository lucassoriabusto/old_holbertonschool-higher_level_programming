#!/usr/bin/python3


import unittest
from models.base import Base


class testbase(unittest.TestCase):
    """Class test base"""

    def test_id(self):
        data = Base()
        self.assertEqual(data.id, 1)

    def test_id_prev(self):
        data = Base()
        self.assertEqual(data.id, 2)

    def test_id_pass(self):
        data = Base(89)
        self.assertEqual(data.id, 89)

if __name__ == '__main__':
    unittest.main()
