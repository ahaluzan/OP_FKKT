import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

case = TEST_DATA3

actual = izpit.preberi_temperaturo("temp_2005.csv")
expected = case

test_case.assertEqual(actual, expected)
