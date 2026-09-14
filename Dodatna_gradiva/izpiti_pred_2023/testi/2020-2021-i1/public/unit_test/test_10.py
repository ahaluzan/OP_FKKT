import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

case = TEST_COVID2

pop = {'Slovenia': 2078989, 'USA': 331341050}
actual = izpit.preberi_covid("covid2.csv", pop)
expected = case

test_case.assertEquals(actual, expected)
