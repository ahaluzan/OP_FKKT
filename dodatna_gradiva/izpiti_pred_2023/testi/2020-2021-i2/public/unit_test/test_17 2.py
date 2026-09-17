import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

actual = izpit.visanje_po_letih(TEST_DICT2, 'Russia', 2010, 2013)
expected = TEST_INCR2

test_case.assertEqual(actual, expected)
