'''obdelaj_datume'''

import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

expected = OBDELAJ_DATUME[0][1]
actual = izpit.obdelaj_datume(*OBDELAJ_DATUME[0][0])

test_case.assertIsInstance(actual, type(expected), "Funkcija vraca napacen tip")

for act, exp in zip(expected, actual):
    test_case.assertIsInstance(act, type(exp), "Funkcija vraca napacen tip")

    for a, e in zip(act, exp):
        test_case.assertIsInstance(a, type(e), "Funkcija vraca napacen tip")
