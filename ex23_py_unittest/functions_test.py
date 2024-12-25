#!/usr/bin/env python3

import functions
import unittest

class TestFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(functions.add(5, 3), 8)

    def test_subtract(self):
        self.assertEqual(functions.subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(functions.multiply(5, 3), 15)

    def test_divide(self):
        self.assertEqual(functions.divide(12, 3), 4)

if __name__ == "__main__":
    unittest.main()