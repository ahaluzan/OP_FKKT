import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

actual = izpit.ocene_po_filmih(RATINGS, READ)
expected = VOTES

test_case.assertIsInstance(actual.__class__, dict.__class__, "Funkcija mora vrniti slovar")
test_case.assertEqual(actual.keys(), expected.keys(), "Vrnjen slovar ne vsebuje ustreznih filmov")
