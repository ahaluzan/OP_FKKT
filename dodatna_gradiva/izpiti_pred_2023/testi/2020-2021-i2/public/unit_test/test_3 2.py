import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

case = TEST_DATA2

actual = izpit.preberi_temperaturo("temp_2010.csv")
expected = case

test_case.assertEqual(actual, expected)
