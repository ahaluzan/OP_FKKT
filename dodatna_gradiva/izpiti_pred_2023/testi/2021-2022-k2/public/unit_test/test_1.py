'''v_seznam'''
import unittest

import naloge
from .TEST_DATA import *

test_case = unittest.TestCase()

actual = naloge.v_seznam("izpiti_3.csv")
expected = N1_DATA

test_case.assertEqual(type(actual), type(expected), "Funkcija vraca napacen tip rezultata.")
