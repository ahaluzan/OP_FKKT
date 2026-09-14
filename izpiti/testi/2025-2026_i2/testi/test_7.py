import unittest
import naloge
import variables

test_case = unittest.TestCase()

expected = [2.9, 4.3, 3.7, 3.2, 4.8, 3.3, 3.5, 4.8]

datoteka = "data/shop10.csv"

actual = [terka[-1] for terka in naloge.preberi_podatke(datoteka)]

test_case.assertEqual(expected, actual, "Napacna pretvorba v decimalno stevilo ali napacna pozicija decimalnega stevila v terki.")