"1. naloga"
import unittest
import naloge
import variables

test_case = unittest.TestCase()

datoteka = "data/kava5.csv"

actual = naloge.preberi_podatke(datoteka)

test_case.assertIsInstance(actual, list, "Funkcija ne vraca seznama.")
