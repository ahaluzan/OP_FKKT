import unittest

import naloge
from .TEST_DATA import *

test_case = unittest.TestCase()

actual = naloge.preberi_podatke("nobelove_S.csv")
expected = N11

test_case.assertEqual(len(actual), len(expected), "Vrnjen seznam ni ustrezne velikosti.")
for act, exp in zip(actual, expected):
    test_case.assertIsInstance(act, type(exp), "Vrstica je napacnega tipa.")
    for i in range(len(exp)):
        test_case.assertIsInstance(act[i], type(exp[i]), "Podatek z indeksom %d je napacnega tipa." % i)
