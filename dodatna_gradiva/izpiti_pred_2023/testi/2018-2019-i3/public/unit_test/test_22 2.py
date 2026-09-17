import unittest

from .TEST_DATA import *
import izpit

test_case = unittest.TestCase()

actual = izpit.najboljse_polletje(READS[1])
expected = NAJBOLJSA_POLLETJA[1]

test_case.assertEqual(len(actual), len(expected), "Rezultat mora imeti tri komponente")
