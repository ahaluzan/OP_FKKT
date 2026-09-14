import unittest
import naloge

test_case = unittest.TestCase()

podatki = [(52, 'UK', 'Beginner', 2, 4.4, 62, 36, 5),
 (16, 'UK', 'Beginner', 7, 10.1, 54, 40, 5),
 (21, 'Indonesia', 'Beginner', 15, 11.2, 53, 29, 5),
 (36, 'Pakistan', 'Advanced', 12, 3.6, 57, 48, 6)]

expected = {5: [(52, 'UK', 'Beginner', 2, 4.4, 62, 36),
  (16, 'UK', 'Beginner', 7, 10.1, 54, 40),
  (21, 'Indonesia', 'Beginner', 15, 11.2, 53, 29)],
 6: [(36, 'Pakistan', 'Advanced', 12, 3.6, 57, 48)]}.values()

actual = naloge.v_slovar(podatki).values()

test_case.assertCountEqual(expected, actual, "Napačne vrednosti.")