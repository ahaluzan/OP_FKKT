'''med_leti-dodatek'''
import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

expected = MED_LETI_2[0][1]
actual = izpit.med_leti(*MED_LETI_2[0][0])

test_case.assertEqual(actual, expected)
