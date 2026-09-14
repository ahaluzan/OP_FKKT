import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

actual = izpit.stopnje_obdavcitev(READS[1])
expected = STOPNJE_OBDAVCITEV[1]

for act, exp in zip(actual, expected):
    test_case.assertIsInstance(act, tuple, "Posamezen zapis mora biti terka")
    test_case.assertIsInstance(act[0], tuple, "Datum mora biti terka")
    test_case.assertEqual(len(act[0]), len(exp[0]), "Datum mora biti terka 2 komponent")
    test_case.assertEqual(act[0], exp[0], "Datuma se ne ujemata")
