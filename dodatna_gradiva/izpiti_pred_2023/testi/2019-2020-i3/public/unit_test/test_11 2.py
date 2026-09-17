"""v_slovar"""
import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

arg, expected = TEST_V_SLOVAR[0]
actual = izpit.v_slovar(arg)

test_case.assertIsInstance(actual, type(expected))

for k, v in actual.items():
    test_case.assertIsInstance(k, str, "Napacen tip kljuca")
    test_case.assertIsInstance(v, int, "Napacen tip vrednosti")
