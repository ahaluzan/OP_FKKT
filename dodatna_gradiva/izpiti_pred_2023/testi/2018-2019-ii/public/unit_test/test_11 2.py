'''prestej_ujemanja'''
import unittest

import izpit

test_case = unittest.TestCase()

combos = [
    [1, 2, 5, 7, 10, 15, 39],
    [3, 5, 10, 11, 21, 22, 30],
    [4, 5, 10, 11, 21, 22, 30]
]
jackpot = [1, 2, 5, 7, 10, 15, 39]

actual = izpit.prestej_ujemanja(combos, jackpot)
expected = [7, 2, 2]

test_case.assertEqual(len(actual), len(expected))
