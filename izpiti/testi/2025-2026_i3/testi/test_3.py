import unittest
import naloge
import variables

test_case = unittest.TestCase()

expected = [25, 34, 19, 45]

datoteka = "data/kava5.csv"

actual = [terka[0] for terka in naloge.preberi_podatke(datoteka)]

test_case.assertEqual(expected, actual, "Napacna pretvorba starosti v celo stevilo ali napacna pozicija v terki.")
