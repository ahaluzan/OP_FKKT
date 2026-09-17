import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

expected = 12.64
actual = izpit.povprecje_po_dnevih(DATA3)

test_case.assertEqual(actual, expected)

