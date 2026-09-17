'''po_drzavah'''
import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

case = PO_DRZAVAH[0]
actual = izpit.po_drzavah(*case[0])
expected = case[1]

test_case.assertIsInstance(actual, type(expected))

for k, v in actual.items():
    test_case.assertIsInstance(k, str, "Napacen tip kljuca")
    test_case.assertIsInstance(v, int, "Napacen tip vrednosti")
