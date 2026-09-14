import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

actual = izpit.stopnje_obdavcitev(READS[1])
expected = STOPNJE_OBDAVCITEV[1]

for act, exp in zip(actual, expected):
    test_case.assertEqual(len(act), len(exp), "Posamezen zapis ima napačno število komponent")
