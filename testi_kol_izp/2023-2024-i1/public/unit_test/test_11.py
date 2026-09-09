import unittest

import naloge
from .TEST_DATA import *

test_case = unittest.TestCase()

sez = [('Frances Hodgson Burnett', 'The Secret Garden', 'standalone', 4.13, 331, []),
       ('John Green', 'Looking for Alaska', 'standalone', 4.02, 221, []),
       ('Louis Sachar', 'Holes', 'Holes', 3.97, 233, []),
       ('Arthur Golden', 'Memoirs of a Geisha', 'standalone', 4.12, 503, []),
       ('Stephenie Meyer', 'Twilight', 'The Twilight Saga', 3.6, 501, [])]

actual = naloge.statistika_strani(sez)
expected = {'min': 221, 'max': 503, 'avg': 357.8}

test_case.assertEqual(len(actual), len(expected), "Slovar ima napacno stevilo elementov.")
for (exp_key, exp_val), (act_key, act_val) in zip(expected.items(), actual.items()):
    test_case.assertEqual(act_key, exp_key, "Napacen kljuc.")
    test_case.assertEqual(act_val, exp_val, "Napacna vrednost.")
