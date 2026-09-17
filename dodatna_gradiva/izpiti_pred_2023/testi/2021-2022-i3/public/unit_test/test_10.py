import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

expected = PO_LETIH[1][1]
actual = izpit.po_letih(*PO_LETIH[1][0])

test_case.assertEqual(actual, expected)
