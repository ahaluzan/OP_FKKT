import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

arg, expected = PETA_B[2]
actual = izpit.slabo_pokrite(*arg)

test_case.assertEqual(actual, expected)
