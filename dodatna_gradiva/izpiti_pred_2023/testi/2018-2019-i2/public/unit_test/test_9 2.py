import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

actual = izpit.kolicina_padavin(READS[0])
expected = PADAVINE_PRAVI

test_case.assertEqual(actual.keys(), expected.keys(), "Rezultat ne vsebuje podatkov za vse mesece")

