'''preberi_podatke'''
import unittest

import naloge
from .TEST_DATA import *

test_case = unittest.TestCase()

actual = naloge.preberi_podatke("nobelove_S.csv")
expected = N11

test_case.assertEqual(type(actual[0]), type(expected[0]), "Funkcija vraca napacen tip rezultata.")
