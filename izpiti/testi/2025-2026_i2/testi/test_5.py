import unittest
import naloge
import variables

test_case = unittest.TestCase()

expected = len(variables.shop10)

datoteka = "data/shop10.csv"

actual = len(naloge.preberi_podatke(datoteka))

test_case.assertEqual(expected, actual, "Preverite obravnavanje vrstic, ki se zacnejo z '#'.")