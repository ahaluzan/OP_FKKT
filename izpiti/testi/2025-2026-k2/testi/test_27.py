import unittest
import naloge

test_case = unittest.TestCase()

podatki = [(1902, 'Sammy Mellor', 'United States', 9792, 39.4),
 (1917, 'Bill Kennedy', 'United States', 8917, 39.4),
 (1919, 'Carl Linder', 'United States', 8953, 39.4),
 (1923, 'Clarence DeMar', 'United States', 8627, 39.4),
 (1926, 'Johnny Miles', 'Canada', 8740, 42.0),
 (1927, 'Clarence DeMar', 'United States', 9622, 42.2),
 (1970, 'Sara Mae Berman', 'United States', 11107, 42.2),
 (1993, 'Olga Markova', 'Russia', 8727, 42.2),
 (1994, 'Uta Pippig', 'Germany', 8505, 42.2), 
 (1971, 'Sara Mae Berman', 'United States', 11310, 42.2)]

expected = {'Clarence DeMar', 'Sara Mae Berman'}

actual = naloge.veckrat(podatki)

test_case.assertEqual(expected, actual, "Napacno vracanje funkcije.")