import unittest
import naloge
import variables

test_case = unittest.TestCase()

expected = variables.shop10[1][0]

datoteka = "data/shop10.csv"

actual = naloge.preberi_podatke(datoteka)[1][0]

test_case.assertEqual(expected, actual, "Napacna pretvorba oznake 'Female'.")