import unittest
import naloge

test_case = unittest.TestCase()

expected = [(1903, 'John Lordan', 'United States', 9689, 39.4),
 (1917, 'Bill Kennedy', 'United States', 8917, 39.4),
 (1970, 'Sara Mae Berman', 'United States', 11107, 42.2),
 (1922, 'Clarence DeMar', 'United States', 8290, 39.4),
 (1923, 'Clarence DeMar', 'United States', 8627, 39.4),
 (1925, 'Charles Mellor', 'United States', 9180, 42.0),
 (1926, 'Johnny Miles', 'Canada', 8740, 42.0),
 (1927, 'Clarence DeMar', 'United States', 9622, 42.2),
 (1928, 'Clarence DeMar', 'United States', 9427, 42.2),
 (1929, 'Johnny Miles', 'Canada', 9188, 42.2),
 (2000, 'Catherine Ndereba', 'Kenya', 8771, 42.2),
 (1931, 'James Henigan', 'United States', 10005, 42.2),
 (1969, 'Sara Mae Berman', 'United States', 12166, 42.2),
 (1993, 'Olga Markova', 'Russia', 8727, 42.2),
 (1994, 'Uta Pippig', 'Germany', 8505, 42.2)]

datoteka = "data/boston_mmiss.csv"

actual = naloge.preberi_podatke(datoteka)

test_case.assertEqual(expected, actual, "Napacno vracanje funkcije v primeru manjkajocih podatkov.")