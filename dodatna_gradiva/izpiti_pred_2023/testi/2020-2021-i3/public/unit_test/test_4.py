import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

case = TEST_DATA

actual = izpit.preberi_v_slovar("promet_2019_small.csv")
expected = case

test_case.assertEqual(len(actual), len(expected), "Napacno stevilo prebranih podatkov")