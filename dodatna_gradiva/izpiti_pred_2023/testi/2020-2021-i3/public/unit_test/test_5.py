import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

case = TEST_DATA

actual = izpit.preberi_v_slovar("promet_2019_small.csv")
expected = case

for (expk, expv) in expected.items():
    test_case.assertIn(expk, actual, "Neujemanje pri kljucu")
    test_case.assertEqual(actual[expk], expv, "Neujemanje pri vrednosti")
