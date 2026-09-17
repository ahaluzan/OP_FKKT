'''po_letih'''

import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

expected = PO_LETIH[0][1]
actual = izpit.po_letih(*PO_LETIH[0][0])

test_case.assertIsInstance(actual, type(expected), "Funkcija vraca napacen tip")

for (act_k, act_v), (exp_k, exp_v) in zip(expected.items(), actual.items()):
    test_case.assertIsInstance(exp_k, type(act_k), "Kljuci v slovarju so napacnega tipa")
    test_case.assertIsInstance(exp_v, type(act_v), "Vrednosti v slovarju so napacnega tipa")
