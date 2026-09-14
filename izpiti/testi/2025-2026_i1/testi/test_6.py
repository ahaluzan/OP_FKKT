import unittest
import naloge

test_case = unittest.TestCase()

expected = [5, 6, 5, 7, 5, 8, 5, 9, 6]

datoteka = "data/python10.csv"

actual = [t[-1] for t in naloge.preberi_podatke(datoteka)]

test_case.assertEqual(expected, actual, "Napačna pretvorba točk v ocene. Preverite meje - od vključno.")