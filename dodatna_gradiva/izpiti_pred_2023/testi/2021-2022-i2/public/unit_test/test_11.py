'''lepi_dnevi'''

import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

expected = RES1
actual = izpit.lepi_dnevi(DATA1)

test_case.assertIsInstance(actual, type(expected), "Funkcija vraca napacen tip")
