#!/usr/bin/python3
"""unittest for Base()"""


import unittest
from models.square import Square

class Test_Square(unittest.TestCase):

    def test_square(self):
        self.assertIsNotNone(Square(1))

if __name__ == "__main__":
    unittest.main()
