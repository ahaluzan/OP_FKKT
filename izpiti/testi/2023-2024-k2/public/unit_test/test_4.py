'''slovar_drzav'''
import unittest

import naloge
from .TEST_DATA import *

test_case = unittest.TestCase()

actual = naloge.slovar_drzav(N21_in)
expected = N21_out

test_case.assertEqual(type(actual), type(expected), "Funkcija vraca napacen tip rezultata.")
