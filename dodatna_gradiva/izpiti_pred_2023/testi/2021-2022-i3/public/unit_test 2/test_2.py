import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

expected = PREBERI_PODATKE[0][1]
actual = izpit.preberi_podatke(*PREBERI_PODATKE[0][0])

for act, exp in zip(expected, actual):
    for a, e in zip(act, exp):
        test_case.assertIsInstance(a, type(e), "Funkcija vraca napacen tip")
