#!/usr/bin/python3
"""unittest for max_integer()"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class Test_Max_Integers(unittest.TestCase):

    def test_(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)


if __name__ == "__main__":
    unittest.main()