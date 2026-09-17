import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

arg, expected = DRUGA[0]
actual = izpit.skupaj_vozil(arg)

test_case.assertEquals(actual, expected)
