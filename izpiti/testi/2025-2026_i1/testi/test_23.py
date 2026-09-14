import unittest
import naloge

test_case = unittest.TestCase()

podatki = {5: [(52, 'UK', 'Beginner', 2, 4.4, 62, 36),
  (16, 'UK', 'Beginner', 7, 10.1, 54, 40),
  (21, 'Indonesia', 'Beginner', 15, 11.2, 53, 29)],
 6: [(36, 'Pakistan', 'Advanced', 12, 3.6, 57, 48)]}

expected = True

data = naloge.statistika(podatki).values()
actual = all(isinstance(k,float) for k in data)

test_case.assertEqual(expected, actual, "Napačen podatkovni tip vrednosti.")