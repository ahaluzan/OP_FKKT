import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

file_ = DATA_FILES[0]
jackpot = JACKPOTS[0]
read = READS[0]
expected = MATCHES[0]

for player, bets in read.items():
    actual = izpit.prestej_ujemanja(bets, jackpot)
    test_case.assertEqual(actual, expected[player])
