import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

actual = izpit.visanje_po_letih(TEST_DICT3, 'Italy', 2000, 2020)
expected = TEST_INCR3

test_case.assertEqual(actual, expected)
