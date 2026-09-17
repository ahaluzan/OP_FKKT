import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

actual = izpit.visanje_po_letih(TEST_DICT4, 'Slovenia', 1991, 2021)
expected = TEST_INCR4

test_case.assertEqual(actual, expected)
