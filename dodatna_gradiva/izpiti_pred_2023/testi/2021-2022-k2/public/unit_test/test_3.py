import unittest

import naloge
from .TEST_DATA import *

test_case = unittest.TestCase()

actual = naloge.v_seznam("izpiti_3.csv")
expected = N1_DATA

test_case.assertEqual(len(actual), len(expected), "Stevilo prebranih podatkov je napacno")

for prebran, dejanski in zip(actual, expected):
    test_case.assertEqual(prebran, dejanski, "Prebrani podatki so napacni")