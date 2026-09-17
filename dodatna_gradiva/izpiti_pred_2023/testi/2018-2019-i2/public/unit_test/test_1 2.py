'''preberi_podatke'''
import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

actual = izpit.preberi_podatke(DATA_FILES[0])
expected = READS[0]

test_case.assertEqual(len(actual), len(expected), "Stevilo vrstic ni pravo")
