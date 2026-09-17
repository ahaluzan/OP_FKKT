import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

actual = izpit.povprecne_mesecne_place(READS[1])
expected = MESECNA_POVPRECJA[1]

for mesec, povprecje in actual.items():
    test_case.assertEqual(povprecje, expected[mesec], "Povprecje za mesec %d je napačno." % mesec)

for mesec, povprecje in expected.items():
    test_case.assertEqual(povprecje, actual[mesec], "Povprecje za mesec %d je napačno." % mesec)
