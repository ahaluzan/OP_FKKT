"statistika"
import unittest
import naloge

test_case = unittest.TestCase()

podatki = {5: [(52, 'UK', 'Beginner', 2, 4.4, 62, 36),
  (16, 'UK', 'Beginner', 7, 10.1, 54, 40),
  (21, 'Indonesia', 'Beginner', 15, 11.2, 53, 29)],
 6: [(36, 'Pakistan', 'Advanced', 12, 3.6, 57, 48)]}

expected = {5: 8.57, 6: 3.6}

actual = naloge.statistika(podatki)

test_case.assertEqual(type(expected), type(actual), "Funkcija vrača napačen podatkovni tip.")