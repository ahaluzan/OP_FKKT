import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

file_ = DATA_FILES[2]
jackpot = JACKPOTS[2]
read = READS[2]
expected = MATCHES[2]

for player, bets in read.items():
    actual = izpit.prestej_ujemanja(bets, jackpot)
    test_case.assertEqual(actual, expected[player])
