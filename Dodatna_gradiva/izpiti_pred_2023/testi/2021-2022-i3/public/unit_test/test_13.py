import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

expected = MED_LETI[2][1]
actual = izpit.med_leti(*MED_LETI[2][0])

test_case.assertEqual(actual, expected)
