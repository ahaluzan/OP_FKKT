import unittest
import naloge

test_case = unittest.TestCase()

podatki = [(1902, 'Sammy Mellor', 'United States', 9792, 39.4),
 (1923, 'Clarence DeMar', 'United States', 8627, 42.2),
 (1926, 'Johnny Miles', 'Canada', 8740, 42.2),
 (1927, 'Clarence DeMar', 'United States', 7622, 42.2),
 (1970, 'Sara Mae Berman', 'United States', 11107, 42.2),
 (1929, 'Johnny Miles', 'Canada', 8640, 42.2),
 (1971, 'Sara Mae Berman', 'United States', 11100, 42.2)]

kilometri = 42.2

expected = {'Clarence DeMar', 'Sara Mae Berman', 'Johnny Miles'}

actual = naloge.boljse(podatki,kilometri)

test_case.assertEqual(expected, actual, "Napacno delovanje funkcije.")