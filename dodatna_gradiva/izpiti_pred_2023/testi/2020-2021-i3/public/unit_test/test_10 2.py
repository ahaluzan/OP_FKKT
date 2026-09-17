import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

arg, expected = DRUGA[1]
actual = izpit.skupaj_vozil(arg)

test_case.assertEquals(actual, expected)

