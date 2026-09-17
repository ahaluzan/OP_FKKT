import unittest

import naloge
from .TEST_DATA import *

test_case = unittest.TestCase()

actual = naloge.v_seznam("izpiti_3.csv")
expected = N1_DATA

for act, exp in zip(actual, expected):
    test_case.assertIsInstance(act, type(exp), "Vrstica je napacnega tipa")
    for i in range(len(exp)):
        test_case.assertIsInstance(act[i], type(exp[i]), "Podatek z indeksom %d je napacnega tipa" % i)
