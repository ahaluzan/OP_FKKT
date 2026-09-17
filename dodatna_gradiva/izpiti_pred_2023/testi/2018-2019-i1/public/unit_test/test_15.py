import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

for (u1, u2), expected in INTERSECTIONS.items():
    actual = izpit.presek(RATINGS, u1, u2)
    test_case.assertEqual(actual, expected,
                          "Neustrezen presek med uporabnikoma '{}' in '{}'".format(
                              u1, u2))
