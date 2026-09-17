import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

actual = izpit.preberi_podatke(DATA_FILES[0])
expected = READS[0]

for act, exp in zip(actual, expected):
    test_case.assertEqual(act[1:-1], exp[1:-1], "Podatki niso pravega formata")

