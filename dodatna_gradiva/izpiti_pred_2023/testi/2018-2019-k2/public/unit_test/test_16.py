'''porazdelitev_ocen'''
import unittest

import naloga

test_case = unittest.TestCase()

GRADED = {
    'a': 5,
    'b': 5,
    'c': 5,
    'd': 5,
    'e': 5
}

DISTRIBUTED = {
    5: 5,
    6: 0,
    7: 0,
    8: 0,
    9: 0,
    10: 0
}

distributed = naloga.porazdelitev_ocen(GRADED)

test_case.assertEqual(distributed, DISTRIBUTED, "Izračunana porazdelitev ocen ni pravilna")
