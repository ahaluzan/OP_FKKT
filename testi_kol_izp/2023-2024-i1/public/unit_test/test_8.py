import unittest

import naloge
from .TEST_DATA import *

test_case = unittest.TestCase()

data_in = [('Frances Hodgson Burnett', 'The Secret Garden', 'standalone', 4.13, 331, ['Classics', 'Fiction', 'Childrens']),
  ('John Green', 'Looking for Alaska', 'standalone', 4.02, 221, ['Young Adult', 'Fiction', 'Contemporary']),
  ('Stephenie Meyer', 'Twilight', 'The Twilight Saga', 3.6, 501, ['Young Adult', 'Fantasy', 'Romance'])]

data_out = {'Classics': [('Frances Hodgson Burnett', 'The Secret Garden')],
 'Fiction': [('Frances Hodgson Burnett', 'The Secret Garden'),
  ('John Green', 'Looking for Alaska')],
 'Childrens': [('Frances Hodgson Burnett', 'The Secret Garden')],
 'Young Adult': [('John Green', 'Looking for Alaska'),
  ('Stephenie Meyer', 'Twilight')],
 'Contemporary': [('John Green', 'Looking for Alaska')],
 'Fantasy': [('Stephenie Meyer', 'Twilight')],
 'Romance': [('Stephenie Meyer', 'Twilight')]}

actual = naloge.slovar_zanrov(data_in)
expected = data_out

test_case.assertEqual(len(actual), len(expected), "Slovar ima napacno stevilo elementov.")
for (exp_key, exp_val), (act_key, act_val) in zip(expected.items(), actual.items()):
    test_case.assertEqual(act_key, exp_key, "Napacen kljuc.")
    test_case.assertEqual(act_val, exp_val, "Napacna vrednost.")
