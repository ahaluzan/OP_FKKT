import unittest
import naloge
import variables

test_case = unittest.TestCase()

expected = [3.57, 2.75, 3.9, 3.6, 3.1, 2.95, 3.75, 2.6]

datoteka = "data/kava10.csv"

actual = [terka[4] for terka in naloge.preberi_podatke(datoteka)]

test_case.assertEqual(expected, actual, "Napacna pretvorba cene v decimalno stevilo ali napacno zaokrozevanje na 2 decimalni mesti.")
