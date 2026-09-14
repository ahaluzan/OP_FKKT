'''med_leti'''

import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

expected = MED_LETI[0][1]
actual = izpit.med_leti(*MED_LETI[0][0])

test_case.assertIsInstance(actual, type(expected), "Funkcija vraca napacen tip")
test_case.assertEqual(actual, expected)
