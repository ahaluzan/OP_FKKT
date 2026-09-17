import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

expected = 2
actual = izpit.najvec_soncnih(DATA1)

test_case.assertEqual(actual, expected)

