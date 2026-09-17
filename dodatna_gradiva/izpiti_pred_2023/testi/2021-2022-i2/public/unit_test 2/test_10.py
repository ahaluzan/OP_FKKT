import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

expected = False
actual = izpit.povprecje_po_dnevih(DATA1, 12)

test_case.assertEqual(actual, expected)

