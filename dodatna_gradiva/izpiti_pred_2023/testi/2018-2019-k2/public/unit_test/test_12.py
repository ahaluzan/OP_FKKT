import unittest

import naloga

test_case = unittest.TestCase()

CORRECTED = {
    "a": [5],
    "b": [5.25],
    "c": [5.99]
}
GRADED = {
    "a": 6,
    "b": 6,
    "c": 6
}

graded = naloga.izracunaj_ocene(CORRECTED)

test_case.assertEqual(graded, GRADED, "Izračunane ocene niso prave")
