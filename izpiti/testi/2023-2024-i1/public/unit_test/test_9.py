'''statistika_strani'''
import unittest

import naloge
from .TEST_DATA import *

test_case = unittest.TestCase()

sez = [('Frances Hodgson Burnett', 'The Secret Garden', 'standalone', 4.13, 331, [])]

actual = naloge.statistika_strani(sez)
expected = {'min': 331, 'max': 331, 'avg': 331.0}

test_case.assertEqual(len(actual), len(expected), "Slovar ima napacno stevilo elementov.")
for (exp_key, exp_val), (act_key, act_val) in zip(expected.items(), actual.items()):
    test_case.assertEqual(act_key, exp_key, "Napacen kljuc.")
    test_case.assertEqual(act_val, exp_val, "Napacna vrednost.")
