import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

actual = izpit.povprecne_mesecne_place(READS[1])
expected = MESECNA_POVPRECJA[1]

test_case.assertEqual(len(actual), len(expected), "Rezultat ne vsebuje vseh podatkov")
