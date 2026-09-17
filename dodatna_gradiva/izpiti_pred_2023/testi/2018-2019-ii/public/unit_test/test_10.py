import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()
actual = izpit.statistika_vplacil(READS[2])
expected = STATS[2]

test_case.assertEqual(len(actual), len(expected))

for player, count in expected.items():
    test_case.assertIn(player, actual)
    test_case.assertEqual(count, actual[player])
