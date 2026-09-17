'''izracunaj_ocene'''
import unittest

import naloga

test_case = unittest.TestCase()

CORRECTED = {
    "a": [-1],
    "b": [0],
    "c": [4.99]
}
GRADED = {
    "a": 5,
    "b": 5,
    "c": 5
}

graded = naloga.izracunaj_ocene(CORRECTED)

test_case.assertEqual(graded, GRADED, "Izračunane ocene niso prave")
