#!/usr/bin/python3
"""fffffffffffffffffffffff"""


import unittest
from models import base
Base = base.Base

class  TestBase(unittest.TestCase):
    """ddddddddddddddddddddd"""
    def test_base(self):
        """fffffffffffffffff"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(29)
        b5 = Base(-7)
        b6 = Base(2.7)
        b7 = Base()
        b8 = Base(None)

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 29)
        self.assertEqual(b5.id, -7)
        self.assertEqual(b6.id, 2.7)
        self.assertEqual(b7.id, 4)
        self.assertEqual(b8.id, 5)

    def test_to_json_string(self):
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, '[]')

    def test_from_json_string(self):
        json_string = Base.from_json_string(None)
        self.assertEqual(json_string, [])

if __name__ == '__main__':
    unittest.main()
