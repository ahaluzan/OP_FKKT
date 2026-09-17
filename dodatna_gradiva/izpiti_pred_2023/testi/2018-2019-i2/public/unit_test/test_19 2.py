import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

actual = izpit.najvec_padavin(READS[0])
expected = NAJVEC_PADAVIN_TESTNI_ALL

test_case.assertEqual(actual, expected)
