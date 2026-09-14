"""visanje_po_letih"""
import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

actual = izpit.visanje_po_letih(TEST_DICT1, 'Russia', 2012, 2013)
expected = TEST_INCR1

test_case.assertEqual(actual, expected)
