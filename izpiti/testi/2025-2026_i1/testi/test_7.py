import unittest
import naloge

test_case = unittest.TestCase()

expected = True

datoteka = "data/python20.csv"

data = naloge.preberi_podatke(datoteka)
actual = all(t[1] != "Other" for t in data)

test_case.assertEqual(expected, actual, "Napačno vračanje funkcije, če je v spremenljivki 'drzava' vrednost 'Other'.")