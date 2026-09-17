import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

actual = izpit.kolicina_padavin(TESTNI_PODATKI_1)
expected = PADAVINE_TESTNI_1

test_case.assertEqual(actual.keys(), expected.keys(), "Rezultat ne vsebuje podatkov za vse mesece")

