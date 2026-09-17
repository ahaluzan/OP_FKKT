import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

actual = izpit.preberi_podatke(DATA_FILES[0])
expected = READS[0]

for act, exp in zip(actual, expected):
    test_case.assertEqual(len(act[0]), len(exp[0]), "Datum nima dveh komponent")

