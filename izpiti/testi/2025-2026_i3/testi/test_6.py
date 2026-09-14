import unittest
import naloge
import variables

test_case = unittest.TestCase()

expected = ['F', 'M', 'F', 'F', 'M', 'F', 'F', 'M']

datoteka = "data/kava10.csv"

actual = [terka[1] for terka in naloge.preberi_podatke(datoteka)]

test_case.assertEqual(expected, actual, "Napacna pretvorba spola ali napacno izpuscanje vrstic z vrednostjo 'Unknown'.")
