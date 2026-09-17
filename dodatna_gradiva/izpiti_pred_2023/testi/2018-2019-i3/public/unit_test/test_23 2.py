import unittest

from .TEST_DATA import *
import izpit

test_case = unittest.TestCase()

actual = izpit.najboljse_polletje(READS[1])
expected = NAJBOLJSA_POLLETJA[1]

test_case.assertIsInstance(actual[0], tuple, "Zacetni datum mora biti terka dolzine 2.")
test_case.assertEqual(len(actual[0]), len(expected[0]), "Zacetni datum mora biti terka dolzine 2.")
test_case.assertIsInstance(actual[1], tuple, "Koncni datum mora biti terka dolzine 2.")
test_case.assertEqual(len(actual[1]), len(expected[1]), "Koncni datum mora biti terka dolzine 2.")
test_case.assertIsInstance(actual[2], float, "Povprecje mora biti decimalno stevilo")
