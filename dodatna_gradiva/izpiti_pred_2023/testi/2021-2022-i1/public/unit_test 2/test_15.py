import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

expected = VOZIL_NA_DAN[3][1]
actual = izpit.vozil_na_dan(*VOZIL_NA_DAN[3][0])

test_case.assertEqual(actual, expected)