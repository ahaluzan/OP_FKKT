'''preberi_stevec'''
import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

expected = PREBERI_STEVEC[0][1]
actual = izpit.preberi_stevec(*PREBERI_STEVEC[0][0])

test_case.assertIsInstance(actual, type(expected), "Funkcija vraca napacen tip")

for act, exp in zip(expected, actual):
    test_case.assertIsInstance(act, type(exp), "Funkcija vraca napacen tip")

    for a, e in zip(act, exp):
        test_case.assertIsInstance(a, type(e), "Funkcija vraca napacen tip")
