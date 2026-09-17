import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

arg, expected = CETRTA[2]
actual = izpit.povprecje_podniz(*arg)

test_case.assertAlmostEqual(actual, expected, 2)
