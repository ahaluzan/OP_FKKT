import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

expected = 0.9
actual = izpit.povprecje_po_dnevih(DATA3, 1)

test_case.assertEqual(actual, expected)

