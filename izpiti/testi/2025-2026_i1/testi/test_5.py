import unittest
import naloge

test_case = unittest.TestCase()

expected = [5, 5, 5, 6]

datoteka = "data/python5.csv"

actual = [t[-1] for t in naloge.preberi_podatke(datoteka)]

test_case.assertEqual(expected, actual, "Napačna pretvorba točk v ocene. Preverite meje.")