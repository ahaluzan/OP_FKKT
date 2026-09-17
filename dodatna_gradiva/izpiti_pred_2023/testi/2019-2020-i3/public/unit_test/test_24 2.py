import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

arg, expected = TEST_POVPRECNA_STAROST[2]
actual = izpit.povprecna_starost(arg)

test_case.assertAlmostEqual(actual, expected, places=5)
