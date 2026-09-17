'''vozil_na_dan'''

import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

expected = VOZIL_NA_DAN[0][1]
actual = izpit.vozil_na_dan(*VOZIL_NA_DAN[0][0])

test_case.assertIsInstance(actual, type(expected), "Funkcija vraca napacen tip")

for (act_k, act_v), (exp_k, exp_v) in zip(expected.items(), actual.items()):
    test_case.assertIsInstance(act_k, type(exp_k), "Kljuci v slovarju so napacnega tipa")
    test_case.assertIsInstance(act_v, type(exp_v), "Vrednosti v slovarju so napacnega tipa")
