"""slovarji"""
import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

case = TEST_DICT3

actual = izpit.slovarji(TEST_DATA3)
expected = case

# check length of solution list
test_case.assertEqual(len(actual), len(expected), "Napacno stevilo vrnjenih zapisov.")

# check variable types of solution
test_case.assertEqual(type(actual), type({}), "Rezultat ni slovar.")
test_case.assertEqual(type(actual[list(actual.keys())[0]]), type({}), "Gnezdena vrednost ni slovar.")

# check length of one solution tuple (one entry)
for k in actual.keys():
  test_case.assertEqual(len(actual[k]), len(expected[k]), "Napacno stevilo elementov v gnezdenem slovarju.")

# check rounding of variables
test_case.assertEqual(len(str(actual[list(actual.keys())[0]][2012]).split(".")[-1]), 2, "Verjetno napacno zaokrozevanje.")

