'''razbij_datum'''

import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

expected = RAZBIJ_DATUM[0][1]
actual = izpit.razbij_datum(*RAZBIJ_DATUM[0][0])

test_case.assertIsInstance(actual, type(expected), "Funkcija vraca napacen tip")
test_case.assertEqual(len(actual), len(expected), "Funkcija vraca napacen podatek")
test_case.assertIsInstance(actual[0], type(expected[0]), "Funkcija vraca napacen tip")
test_case.assertIsInstance(actual[1], type(expected[1]), "Funkcija vraca napacen tip")
