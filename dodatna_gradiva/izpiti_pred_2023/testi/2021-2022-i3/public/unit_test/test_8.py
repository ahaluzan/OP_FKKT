import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

expected = PO_LETIH[0][1]
actual = izpit.po_letih(*PO_LETIH[0][0])

test_case.assertEqual(len(actual), len(expected), "Vrnjen slovar ima napacno stevilo elementov.")