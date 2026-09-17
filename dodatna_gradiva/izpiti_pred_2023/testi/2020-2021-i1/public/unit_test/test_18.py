import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

case = TEST_WORST2

regije = {'Oceania': 0.0, 'Europe': 0.0678, 'Asia': 0.0329}
actual = izpit.najslabsa_regija(regije)
expected = case

test_case.assertEquals(actual, expected)
