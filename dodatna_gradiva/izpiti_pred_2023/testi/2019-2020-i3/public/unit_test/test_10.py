import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

arg, expected = TEST_INFECTION_COUNT[1]
actual = izpit.okuzb_med_dnevi(*arg)

test_case.assertEquals(actual, expected)
