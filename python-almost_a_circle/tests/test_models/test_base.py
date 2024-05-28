#!/usr/bin/python3
"""unittest for Base()"""


import unittest
from models.base import Base

class Test_Base(unittest.TestCase):

    def test_BaseID(self):
        obj = Base()
        self.assertIsNotNone(obj.id)

if __name__ == "__main__":
    unittest.main()