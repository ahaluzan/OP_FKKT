import unittest

import naloge
from .TEST_DATA import *

test_case = unittest.TestCase()

data_in = [('Frances Hodgson Burnett', 'The Secret Garden', 'standalone', 4.13, 331, ['Classics', 'Fiction', 'Childrens'])]
data_out = {'Classics': [('Frances Hodgson Burnett', 'The Secret Garden')],
 'Fiction': [('Frances Hodgson Burnett', 'The Secret Garden')],
 'Childrens': [('Frances Hodgson Burnett', 'The Secret Garden')]}

actual = naloge.slovar_zanrov(data_in)
expected = data_out

test_case.assertEqual(len(actual), len(expected), "Slovar ima napacno stevilo elementov.")
for (exp_key, exp_val), (act_key, act_val) in zip(expected.items(), actual.items()):
    test_case.assertEqual(act_key, exp_key, "Napacen kljuc.")
    test_case.assertEqual(act_val, exp_val, "Napacna vrednost.")
   
