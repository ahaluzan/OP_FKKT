import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

arg, expected = TEST_V_SLOVAR[1]
actual = izpit.v_slovar(arg)

test_case.assertEquals(actual, expected)
