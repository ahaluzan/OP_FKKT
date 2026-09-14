"preberi_podatke"
import unittest
import naloge

test_case = unittest.TestCase()

expected = [(52, 'UK', 'Beginner', 2, 4.4, 62, 36, 5),
 (16, 'UK', 'Beginner', 7, 10.1, 54, 40, 5),
 (21, 'Indonesia', 'Beginner', 15, 11.2, 53, 29, 5),
 (36, 'Pakistan', 'Advanced', 12, 3.6, 57, 48, 6)]

datoteka = "data/python5.csv"

actual = naloge.preberi_podatke(datoteka)

test_case.assertEqual(type(expected), type(actual), "Funkcija vraca napacen podatkovni tip.")