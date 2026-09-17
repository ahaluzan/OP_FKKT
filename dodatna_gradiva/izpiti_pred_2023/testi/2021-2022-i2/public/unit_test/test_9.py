import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

expected = 23.03
actual = izpit.povprecje_po_dnevih(DATA3, 7)

test_case.assertEqual(actual, expected)

