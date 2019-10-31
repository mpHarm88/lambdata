"""
This is our testing file for square root functions
"""

import unittest
from sqrt import lazy_sqrt, builtin_sqrt, newton_sqrt

#Our class for square root functions
class SqrtTests(unittest.TestCase):
    """These are our tests for square root functions  """
    def test_sqrt9(self):
        self.assertEqual(lazy_sqrt(9), 3)


    def test_sqrt2(self):
        self.assertAlmostEqual(builtin_sqrt(2), 1.414)


class Othertests(unittest.TestCase):
    def test_thing(self):
        pass

if __name__ == '__main__':
    unittest.main()
