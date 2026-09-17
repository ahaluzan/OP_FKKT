import unittest

import naloga

test_case = unittest.TestCase()

GRADED = {
    'a': 10,
    'b': 5,
    'c': 10,
    'd': 5,
    'e': 10
}

DISTRIBUTED = {
    5: 2,
    6: 0,
    7: 0,
    8: 0,
    9: 0,
    10: 3
}

distributed = naloga.porazdelitev_ocen(GRADED)

test_case.assertEqual(distributed, DISTRIBUTED, "Izračunana porazdelitev ocen ni pravilna")
