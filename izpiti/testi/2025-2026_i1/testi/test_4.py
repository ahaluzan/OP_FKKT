import unittest
import naloge

test_case = unittest.TestCase()

expected = True

datoteka = "data/python5.csv"

actual = all(isinstance(terka[4], float) for terka in naloge.preberi_podatke(datoteka))

test_case.assertEqual(expected, actual, "Napačna pretvorba elementov terke v decimalno število ali pretvorba napačnega elementa.")