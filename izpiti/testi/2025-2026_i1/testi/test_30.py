import unittest
import naloge

test_case = unittest.TestCase()

podatki = {5: [(28, 'UK', 'Beginner', 9, 4.5, 52, 49),
  (43, 'Indonesia', 'Intermediate', 15, 8.2, 62, 30),
  (52, 'UK', 'Beginner', 2, 4.4, 62, 36),
  (18, 'Pakistan', 'Beginner', 5, 10.6, 46, 34),
  (16, 'UK', 'Beginner', 7, 10.1, 54, 40),
  (21, 'Indonesia', 'Beginner', 15, 11.2, 53, 29),
  (39, 'India', 'Beginner', 1, 4.9, 72, 47),
  (33, 'Pakistan', 'Beginner', 12, 7.4, 60, 34)],
 7: [(29, 'USA', 'Beginner', 6, 7.8, 54, 31),
  (30, 'Germany', 'Intermediate', 3, 10.4, 48, 36)],
 6: [(40, 'India', 'Advanced', 7, 6.9, 59, 38),
  (36, 'Pakistan', 'Advanced', 12, 3.6, 57, 48)],
 8: [(44, 'India', 'Beginner', 10, 8.5, 69, 38),
  (28, 'Germany', 'Intermediate', 3, 5.3, 68, 32)]}

expected = {5: 7.66, 7: 9.1, 6: 5.25, 8: 6.9}

actual = naloge.statistika(podatki)

test_case.assertEqual(expected, actual, "Napačno vračanje funkcije.")