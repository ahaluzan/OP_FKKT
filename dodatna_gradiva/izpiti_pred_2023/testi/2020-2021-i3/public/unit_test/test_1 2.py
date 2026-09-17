"""preberi_v_slovar"""
import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

case = TEST_DATA

actual = izpit.preberi_v_slovar("promet_2019_small.csv")
expected = case

test_case.assertEqual(type(list(actual.keys())[0]), type(list(expected.keys())[0]), "Napacen tip kljuca v slovarju")
