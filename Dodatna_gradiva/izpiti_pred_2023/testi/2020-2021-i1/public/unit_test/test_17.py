import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

case = TEST_WORST1

regije = {'Americas': 0.0683, 'Europe': 0.0678}
actual = izpit.najslabsa_regija(regije)
expected = case

test_case.assertEquals(actual, expected)
