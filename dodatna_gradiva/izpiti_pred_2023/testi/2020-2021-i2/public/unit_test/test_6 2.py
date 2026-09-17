"""presezek"""
import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

case = TEST_OVER1

actual = izpit.presezek(TEST_DATA3, 11.5, 2013)
expected = case

# check type of solution
test_case.assertEqual(type(actual), type(expected), "Vrnjeni rezultat ni mnozica.")

# check length of solution
test_case.assertEqual(len(actual), len(expected), "Napacno stevilo presezkov.")
