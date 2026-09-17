'''v_slovarja'''
import unittest

import naloge
from .TEST_DATA import *

test_case = unittest.TestCase()

actual = naloge.v_slovarja(N1_DATA)
expected = N2_DATA

test_case.assertEqual(type(actual), type(expected), "Funkcija vraca napacen tip rezultata.")
