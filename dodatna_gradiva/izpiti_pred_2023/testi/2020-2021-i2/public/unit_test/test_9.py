import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

case = TEST_OVER3

actual = izpit.presezek(TEST_DATA2, -3.4, 2011)
expected = case

test_case.assertEqual(actual, expected)

