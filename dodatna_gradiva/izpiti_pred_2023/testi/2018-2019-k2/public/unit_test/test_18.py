import unittest

import naloga

test_case = unittest.TestCase()

GRADED = {
    'a': 5,
    'b': 6,
    'c': 7,
    'd': 8,
    'e': 9,
    'f': 10
}

DISTRIBUTED = {
    5: 1,
    6: 1,
    7: 1,
    8: 1,
    9: 1,
    10: 1
}

distributed = naloga.porazdelitev_ocen(GRADED)

test_case.assertEqual(distributed, DISTRIBUTED, "Izračunana porazdelitev ocen ni pravilna")
