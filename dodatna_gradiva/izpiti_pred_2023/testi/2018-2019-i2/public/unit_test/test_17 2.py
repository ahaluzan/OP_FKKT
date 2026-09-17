import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

actual = izpit.najvec_padavin(TESTNI_PODATKI_2)
expected = NAJVEC_PADAVIN_TESTNI_2

test_case.assertEqual(actual, expected)
