#!/usr/bin/python3
"""unittest for max_integer()"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class Test_Max_Integers(unittest.TestCase):

    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_in_middle(self):
        self.assertEqual(max_integer([1, 4, 2]), 4)

    def test_one_negative(self):
        self.assertEqual(max_integer([-1, 1, 2]), 2)

    def test_all_negative(self):
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_one_element(self):
        self.assertEqual(max_integer([2]), 2)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

if __name__ == "__main__":
    unittest.main()