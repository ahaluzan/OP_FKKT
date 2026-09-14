import unittest
import naloge
import variables

test_case = unittest.TestCase()

expected = [20, 41, 85, 71, 31, 81, 38, 26]

datoteka = "data/shop10.csv"

actual = [terka[-2] for terka in naloge.preberi_podatke(datoteka)]

test_case.assertEqual(expected, actual, "Napacna pretvorba v celo stevilo ali napacna pozicija celega stevila v terki.")