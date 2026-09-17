import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

case = TEST_DICT2

actual = izpit.slovarji(TEST_DATA2)
expected = case

test_case.assertEqual(actual, expected)
