import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

u1, u2 = 'Enej', 'Greg'
actual = izpit.presek(RATINGS, u1, u2)
expected = [0, 4, 15, 17]

test_case.assertEqual(actual, expected, "Neustrezen presek za uporabnika '{}' in '{}'.".format(
    u1, u2))
