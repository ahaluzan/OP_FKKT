import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

arg, expected = TEST_SPOL[2]
actual = izpit.moski_zenske(arg)

test_case.assertAlmostEqual(actual, expected, places=5)
