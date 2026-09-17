"""povprecje_podniz"""

import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

arg, expected = CETRTA[0]
actual = izpit.povprecje_podniz(*arg)

test_case.assertIsInstance(actual, type(expected), "Funkcija vraca napacen tip")
