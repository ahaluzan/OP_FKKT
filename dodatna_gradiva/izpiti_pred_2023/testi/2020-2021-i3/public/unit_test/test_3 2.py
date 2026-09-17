import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

case = TEST_DATA

actual = izpit.preberi_v_slovar("promet_2019_small.csv")
expected = case

for act, exp in zip(list(actual.values())[0], list(expected.values())[0]):
    test_case.assertEqual(type(act), type(exp), "Napacen tip znotraj vrednosti v slovarju")
