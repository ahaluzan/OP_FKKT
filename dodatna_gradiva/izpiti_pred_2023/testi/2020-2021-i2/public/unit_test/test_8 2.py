import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

case = TEST_OVER1

actual = izpit.presezek(TEST_DATA1, 11.5, 2013)
expected = case

test_case.assertEqual(actual, expected)

