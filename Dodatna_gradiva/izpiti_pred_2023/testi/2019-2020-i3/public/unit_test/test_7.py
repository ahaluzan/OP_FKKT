import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

arg, expected = TEST_DATES[0]
actual = izpit.v_datum(arg)
test_case.assertEquals(
    actual,
    expected,
    "Vrednost %s se pretvori mora pretvoriti v %s in ne %s" % (arg, expected, actual),
)
