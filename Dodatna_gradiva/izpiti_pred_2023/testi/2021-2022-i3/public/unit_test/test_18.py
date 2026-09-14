import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

expected = NAJVEC[2][1]
actual = izpit.najvec(*NAJVEC[2][0])

test_case.assertEqual(actual, expected)
