import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

case = TEST_DICT3

actual = izpit.slovarji(TEST_DATA3)
expected = case

test_case.assertEqual(actual, expected)
