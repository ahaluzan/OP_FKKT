import unittest
import naloge
import variables

test_case = unittest.TestCase()

expected = variables.kava5

datoteka = "data/kava5.csv"

actual = naloge.preberi_podatke(datoteka)

test_case.assertEqual(expected, actual, "Napacno vracanje funkcije.")
