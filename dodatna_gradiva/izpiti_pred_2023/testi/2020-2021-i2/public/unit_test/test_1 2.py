"""preberi_temperaturo"""
import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

case = TEST_DATA3

actual = izpit.preberi_temperaturo("temp_2005.csv")
expected = case

# check length of solution list
test_case.assertEqual(len(actual), len(expected), "Napacno stevilo prebranih zapisov.")

# check length of one solution tuple (one entry)
test_case.assertEqual(len(actual[0]), len(expected[0]), "Napacno stevilo elementov v vrnjeni terki.")

# check variable types of solution
test_case.assertEqual(type(actual[0][0]), type(25), "Vrednost v terki je napacnega tipa.")
test_case.assertEqual(type(actual[0][1]), type("sasa"), "Vrednost v terki je napacnega tipa.")
test_case.assertEqual(type(actual[0][2]), type(3.14), "Vrednost v terki je napacnega tipa.")
test_case.assertEqual(type(actual[0][3]), type(3.14), "Vrednost v terki je napacnega tipa.")

# check rounding of variables
test_case.assertEqual(len(str(actual[0][2]).split(".")[-1]), 2, "Verjetno napacno zaokrozevanje.")
test_case.assertEqual(len(str(actual[0][3]).split(".")[-1]), 2, "Verjetno napacno zaokrozevanje.")
