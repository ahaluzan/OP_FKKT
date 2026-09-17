import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

arg, expected = PETA_A[1]
actual = izpit.preveri_pokritost(arg)

test_case.assertEqual(len(actual), len(expected))

for (expk, expv) in expected.items():
    test_case.assertIn(expk, actual, "Neujemanje pri kljucu")
    test_case.assertEqual(actual[expk], expv, "Neujemanje pri vrednosti")
