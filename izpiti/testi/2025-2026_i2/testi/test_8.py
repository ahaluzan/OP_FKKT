import unittest
import naloge
import variables

test_case = unittest.TestCase()

expected = variables.shop10

datoteka = "data/shop10.csv"

actual = naloge.preberi_podatke(datoteka)

test_case.assertEqual(expected, actual, "Napacno vracanje funkcije.")