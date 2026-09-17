'''ocene_po_filmih'''
import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

actual = len(izpit.ocene_po_filmih(RATINGS, READ))
expected = len(VOTES)

test_case.assertEqual(actual, expected,
                      "Dolžina slovarja ocen mora biti %d" % expected)
