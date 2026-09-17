import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

case = PO_DRZAVAH[0]
actual = izpit.po_drzavah(*case[0])
expected = case[1]

test_case.assertEquals(actual, expected)
