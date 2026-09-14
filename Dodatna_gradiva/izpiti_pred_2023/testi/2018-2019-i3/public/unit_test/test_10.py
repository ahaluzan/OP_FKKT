import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

actual = izpit.stopnje_obdavcitev(READS[0])
expected = STOPNJE_OBDAVCITEV[0]

for act, exp in zip(actual, expected):
    test_case.assertEqual(act, exp)

