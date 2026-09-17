import unittest

import naloga

test_case = unittest.TestCase()

CORRECTED = {
    "a": [7],
    "b": [7.99],
    "c": [8],
    "d": [8.5],
    "e": [9],
    "f": [9.5],
    "g": [10]
}
GRADED = {
    "a": 8,
    "b": 8,
    "c": 9,
    "d": 9,
    "e": 10,
    "f": 10,
    "g": 10
}

graded = naloga.izracunaj_ocene(CORRECTED)

test_case.assertEqual(graded, GRADED, "Izračunane ocene niso prave")
