import unittest
import naloge

test_case = unittest.TestCase()

expected = True

datoteka = "data/python5.csv"

actual = all(isinstance(terka[i], int) for terka in naloge.preberi_podatke(datoteka) for i in [0,3,5,6,7])

test_case.assertEqual(expected, actual, "Napačna pretvorba elementov terke v int ali pretvorba napačnih elementov.")