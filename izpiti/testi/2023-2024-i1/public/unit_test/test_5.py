'''slovar_zanrov'''
import unittest

import naloge
from .TEST_DATA import *

test_case = unittest.TestCase()

actual = naloge.slovar_zanrov([])
expected = {}

test_case.assertEqual(actual, expected)

#test_case.assertEqual(len(actual), len(expected), "Slovar ima napacno stevilo elementov.")
#for (exp_key, exp_val), (act_key, act_val) in zip(expected.items(), actual.items()):
#    test_case.assertEqual(act_key, exp_key, "Napacen kljuc.")
#    test_case.assertEqual(act_val, exp_val, "Napacna vrednost.")
   
