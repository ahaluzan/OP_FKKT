import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

expected = NAJVEC[1][1]
actual = izpit.najvec(*NAJVEC[1][0])

test_case.assertEqual(actual, expected)
