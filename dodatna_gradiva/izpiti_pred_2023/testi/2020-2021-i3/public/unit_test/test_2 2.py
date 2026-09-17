import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

case = TEST_DATA

actual = izpit.preberi_v_slovar("promet_2019_small.csv")
expected = case

test_case.assertEqual(type(list(actual.values())[0]), type(list(expected.values())[0]),
                      "Napacen tip vrednosti v slovarju")
