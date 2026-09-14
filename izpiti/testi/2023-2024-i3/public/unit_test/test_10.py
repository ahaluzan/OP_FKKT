import unittest

import naloge
from .TEST_DATA import *

test_case = unittest.TestCase()

sez = {'starosti': [28, 27, 33, 26, 26, 29, 26, 29, 23, 24, 26],
 'goli': [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
 'rumeni_kartoni': [0, 0, 0, 0, 0, 0, 1, 2, 1, 2, 0],
 'rdeci_kartoni': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}

actual = naloge.drzavno_povprecje(sez)
expected = {'povprecna_starost': 27.0, 'najvec_golov': 1, 'kazni': (6, 0)}

for (exp_key, exp_val), (act_key, act_val) in zip(expected.items(), actual.items()):
    test_case.assertEqual(act_key, exp_key, "Napacen kljuc.")
    test_case.assertEqual(act_val, exp_val, "Napacna vrednost.")
