import unittest

import naloga

test_case = unittest.TestCase()

CORRECTED = {
    "a": [6],
    "b": [6.25],
    "c": [6.99]
}
GRADED = {
    "a": 7,
    "b": 7,
    "c": 7
}

graded = naloga.izracunaj_ocene(CORRECTED)

test_case.assertEqual(graded, GRADED, "Izračunane ocene niso prave")
