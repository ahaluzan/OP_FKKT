import unittest
import naloge
import variables

test_case = unittest.TestCase()

expected = variables.kava20

datoteka = "data/kava20.csv"

actual = naloge.preberi_podatke(datoteka)

test_case.assertEqual(expected, actual, "Napacno vracanje funkcije.")
