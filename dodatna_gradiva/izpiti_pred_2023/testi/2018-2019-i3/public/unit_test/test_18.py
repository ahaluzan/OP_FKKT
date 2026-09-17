import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

actual = izpit.povprecne_mesecne_place(READS[1])
expected = MESECNA_POVPRECJA[1]

test_case.assertEqual(actual.keys(), expected.keys(), "Rezultat ne vsebuje vseh podatkov")
