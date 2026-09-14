import unittest
import naloge

test_case = unittest.TestCase()

podatki = [(1902, 'Sammy Mellor', 'United States', 9792, 39.4),
 (1923, 'Clarence DeMar', 'United States', 8627, 39.4),
 (1926, 'Johnny Miles', 'Canada', 8740, 42.0),
 (1927, 'Clarence DeMar', 'United States', 9622, 42.2),
 (1970, 'Sara Mae Berman', 'United States', 11107, 42.2),
 (1929, 'Johnny Miles', 'Canada', 9188, 42.2),
 (1971, 'Sara Mae Berman', 'United States', 11100, 42.2)]

kilometri = 42.2

expected = {'Sara Mae Berman'}

actual = naloge.boljse(podatki,kilometri)

test_case.assertEqual(expected, actual, "Napacno delovanje funkcije.")