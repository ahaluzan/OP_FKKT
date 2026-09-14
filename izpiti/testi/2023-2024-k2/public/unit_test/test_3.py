import unittest

import naloge
from .TEST_DATA import *

test_case = unittest.TestCase()

actual = naloge.preberi_podatke("nobelove_S2.csv")
expected = N12

test_case.assertEqual(actual, expected, "Branje datoteke z imenom nobelove_S2.csv je napacno.")


