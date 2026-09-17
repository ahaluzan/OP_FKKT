import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

actual = izpit.preberi_podatke(DATA_FILES[0])
expected = READS[0]

# Stevilo stavnih listov
for player, bets in expected.items():
    test_case.assertIn(player, actual)
    test_case.assertEqual(len(bets), len(actual[player]))

