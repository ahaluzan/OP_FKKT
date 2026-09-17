"""v_datum"""
import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

arg, expected = TEST_DATES[0]
expected = type(expected)
actual = type(izpit.v_datum(arg))
test_case.assertEquals(
    actual,
    expected,
    "Rezultat klica funkcije 'v_datum' mora biti tipa %s in ne %s" % (expected, actual),
)
