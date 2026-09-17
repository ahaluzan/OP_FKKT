'''najvec'''

import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

expected = NAJVEC[0][1]
actual = izpit.najvec(*NAJVEC[0][0])

test_case.assertIsInstance(actual, type(expected), "Funkcija vraca napacen tip podatka")
test_case.assertEqual(actual, expected)
