import unittest
import naloge
import variables

test_case = unittest.TestCase()

datoteka = "data/kava5.csv"

actual = naloge.preberi_podatke(datoteka)

test_case.assertTrue(all(isinstance(terka, tuple) for terka in actual), "Elementi seznama niso terke.")
