import unittest
import naloge
import variables

test_case = unittest.TestCase()

expected = variables.shop20

datoteka = "data/shop20.csv"

actual = naloge.preberi_podatke(datoteka)

test_case.assertEqual(expected, actual, "Napacno vracanje funkcije.")