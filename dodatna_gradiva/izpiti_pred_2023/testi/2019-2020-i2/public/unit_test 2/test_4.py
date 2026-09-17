import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

actual = izpit.preberi_podatke(DATOTEKA_TEST_1)
expected = PODATKI_TEST_1

for act, exp in zip(actual, expected):
    for act_col, exp_col in zip(act, exp):
        test_case.assertIsInstance(act_col, type(exp_col), "Napacen tip podatka")
