import unittest
import naloge
import variables

test_case = unittest.TestCase()

expected = variables.shop10

datoteka = "data/shop10.csv"

actual = naloge.preberi_podatke(datoteka)

test_case.assertEqual(type(expected[0]), type(actual[0]), "Funkcija vraca napacen podatkovni tip znotraj seznama.")