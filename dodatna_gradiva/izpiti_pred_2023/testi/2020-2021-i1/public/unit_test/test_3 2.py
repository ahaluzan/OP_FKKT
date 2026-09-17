import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

case = TEST_DATA

actual = izpit.preberi_populacijo("population1.csv")
#expected = case

for k, v in actual.items():
    test_case.assertIsInstance(k, str, "Napacen tip kljuca")
    test_case.assertIsInstance(v, int, "Napacen tip vrednosti")
