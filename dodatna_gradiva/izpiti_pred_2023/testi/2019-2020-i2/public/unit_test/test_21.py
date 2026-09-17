'''skupni'''
import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

case = SKUPNI[0]
actual = izpit.skupni(*case[0])
expected = case[1]

test_case.assertIsInstance(actual, type(expected))

for k, v in actual.items():
    test_case.assertIsInstance(k, tuple, "Napacen tip kljuca")
    test_case.assertIsInstance(v, set, "Napacen tip vrednosti")
