import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

expected = NAJVEC[3][1]
actual = izpit.najvec(*NAJVEC[3][0])

test_case.assertEqual(actual, expected)
