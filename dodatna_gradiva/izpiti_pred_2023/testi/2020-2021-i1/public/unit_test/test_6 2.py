"""preberi_covid"""
import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

case = TEST_COVID

pop = {'Slovenia': 2078989, 'Monaco': 39290, 'Gibraltar': 33689}
actual = izpit.preberi_covid("covid1.csv", pop)
expected = case

test_case.assertEqual(len(actual), len(expected), "Napacno stevilo prebranih zapisov")
