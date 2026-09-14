import unittest
import naloge

test_case = unittest.TestCase()

podatki = {5: [(43, 'Indonesia', 'Intermediate', 15, 8.2, 62, 30),
  (52, 'UK', 'Beginner', 2, 4.4, 62, 36),
  (16, 'UK', 'Beginner', 7, 10.1, 54, 40),
  (21, 'Indonesia', 'Beginner', 15, 11.2, 53, 29)],
 6: [(40, 'India', 'Advanced', 7, 6.9, 59, 38),
  (36, 'Pakistan', 'Advanced', 12, 3.6, 57, 48)],
 7: [(30, 'Germany', 'Intermediate', 3, 10.4, 48, 36)],
 8: [(44, 'India', 'Beginner', 10, 8.5, 69, 38)],
 9: [(39, 'India', 'Beginner', 1, 4.9, 72, 47)]}

expected = {5: 8.47, 6: 5.25, 7: 10.4, 8: 8.5, 9: 4.9}.values()

actual = naloge.statistika(podatki).values()

test_case.assertCountEqual(expected, actual, "Napačne vrednosti.")