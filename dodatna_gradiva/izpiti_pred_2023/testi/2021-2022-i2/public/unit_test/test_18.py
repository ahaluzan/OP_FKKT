import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

expected = 9
actual = izpit.najvec_soncnih(DATA3)

test_case.assertEqual(actual, expected)

