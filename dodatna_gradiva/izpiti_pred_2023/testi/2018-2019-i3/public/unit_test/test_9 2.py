import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

actual = izpit.stopnje_obdavcitev(READS[1])
expected = STOPNJE_OBDAVCITEV[1]

for act, exp in zip(actual, expected):
    test_case.assertIsInstance(act[1], float, "Stopnja obdavcitve mora biti decimalno stevilo")
    test_case.assertEqual(act[1], exp[1], "Stopnja obdavcitve ni prava")

