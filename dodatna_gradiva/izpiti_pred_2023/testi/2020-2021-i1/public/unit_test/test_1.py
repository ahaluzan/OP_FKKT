"""preberi_populacijo"""
import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

case = TEST_DATA

actual = izpit.preberi_populacijo("population1.csv")
expected = case

test_case.assertEqual(len(actual), len(expected), "Napacno stevilo prebranih zapisov")
