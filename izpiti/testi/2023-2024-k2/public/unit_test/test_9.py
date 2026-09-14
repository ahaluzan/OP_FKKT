import unittest

import naloge
from .TEST_DATA import *

test_case = unittest.TestCase()

actual = naloge.slovar_starosti([(1992, 'Walcott', 'literature', 'm', '1930-23-01', 'LC'),
 (1967, 'Wald', 'medicine', 'm', '1906-18-11', 'US'), 
 (2020, 'Milgrom', 'economics', 'm', '1948-20-04', 'US')])
expected = {(1992, 'Walcott'): 62, (1967, 'Wald'): 61, (2020, 'Milgrom'): 72}

test_case.assertEqual(len(actual), len(expected), "Slovar ima napacno stevilo elementov.")
for (exp_key, exp_val), (act_key, act_val) in zip(expected.items(), actual.items()):
    test_case.assertEqual(act_key, exp_key, "Napacen kljuc.")
    test_case.assertEqual(act_val, exp_val, "Napacna vrednost.")
