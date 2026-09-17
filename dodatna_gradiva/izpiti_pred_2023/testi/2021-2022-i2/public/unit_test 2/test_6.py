'''povprecje_po_dnevih'''

import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

expected = 8.61
actual = izpit.povprecje_po_dnevih(DATA1)

test_case.assertIsInstance(actual, type(expected), "Funkcija vraca napacen tip")
