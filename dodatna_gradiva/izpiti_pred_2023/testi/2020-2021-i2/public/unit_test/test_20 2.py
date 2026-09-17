import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

actual = izpit.visanje_po_letih(TEST_DICT4, 'Slovenia', 1892, 1990)
expected = TEST_INCR5

test_case.assertEqual(actual, expected)
