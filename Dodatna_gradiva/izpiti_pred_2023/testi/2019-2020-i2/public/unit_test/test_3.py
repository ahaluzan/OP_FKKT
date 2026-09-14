'''preberi_podatke'''
import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

actual = izpit.preberi_podatke(DATOTEKA_TEST_1)
expected = PODATKI_TEST_1

test_case.assertEqual(len(actual), len(expected), "Napacno stevilo prebranih zapisov")
