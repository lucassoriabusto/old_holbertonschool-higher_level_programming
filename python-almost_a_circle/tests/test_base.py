#!/usr/bin/python3

import unittest
from models import Base

class  TestBase(unittest.TestCase):

    def test_base(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)

if __name__ == '__main__':
    unittest.main()
