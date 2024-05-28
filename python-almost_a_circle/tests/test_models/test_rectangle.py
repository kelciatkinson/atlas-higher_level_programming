#!/usr/bin/python3
"""unittest for Base()"""


import unittest
from models.rectangle import Rectangle

class Test_Rectangle(unittest.TestCase):

    def test_rect(self):
        self.assertIsNotNone(Rectangle(1, 2))

if __name__ == "__main__":
    unittest.main()
