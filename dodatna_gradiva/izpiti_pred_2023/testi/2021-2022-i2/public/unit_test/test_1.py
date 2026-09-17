'''preberi_vreme'''
import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

expected = DATA1
actual = izpit.preberi_vreme('weather_KP_small.csv')

test_case.assertIsInstance(actual, type(expected), "Funkcija vraca napacen tip")

"""
for act, exp in zip(expected, actual):
    test_case.assertIsInstance(act, type(exp), "Funkcija vraca napacen tip")

    for a, e in zip(act, exp):
        test_case.assertIsInstance(a, type(e), "Funkcija vraca napacen tip")
"""