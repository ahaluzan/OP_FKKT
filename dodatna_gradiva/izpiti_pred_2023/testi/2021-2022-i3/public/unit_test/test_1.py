'''preberi_podatke'''
import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

expected = PREBERI_PODATKE[0][1]
actual = izpit.preberi_podatke(*PREBERI_PODATKE[0][0])

test_case.assertIsInstance(actual, type(expected), "Funkcija vraca napacen tip")

for act, exp in zip(expected, actual):
    test_case.assertIsInstance(act, type(exp), "Funkcija vraca napacen tip")
