"""skupaj_vozil"""
import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

arg, expected = DRUGA[0]
actual = izpit.skupaj_vozil(arg)
test_case.assertEquals(
    type(actual),
    type(expected),
    "Rezultat klica funkcije 'skupaj_vozil' mora biti tipa %s in ne %s" % (type(expected), type(actual)),
)
