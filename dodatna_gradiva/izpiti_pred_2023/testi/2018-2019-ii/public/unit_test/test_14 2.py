import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

file_ = DATA_FILES[1]
jackpot = JACKPOTS[1]
read = READS[1]
expected = MATCHES[1]

for player, bets in read.items():
    actual = izpit.prestej_ujemanja(bets, jackpot)
    test_case.assertEqual(actual, expected[player])
