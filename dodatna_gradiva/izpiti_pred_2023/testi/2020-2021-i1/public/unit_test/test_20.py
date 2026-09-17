import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

case = TEST_WORST2

regije = {'Americas': 0, 'Europe': 0}
actual = izpit.najslabsa_regija(regije)
expected = case

test_case.assertEquals(actual, None)
