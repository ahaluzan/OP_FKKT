import unittest
import naloge

test_case = unittest.TestCase()

podatki = [(1924, 'Clarence DeMar', 'United States', 8980, 42.0),
 (1922, 'Clarence DeMar', 'United States', 8290, 39.4),
 (1923, 'Clarence DeMar', 'United States', 8627, 39.4),
 (1927, 'Clarence DeMar', 'United States', 9622, 42.2),
 (1928, 'Clarence DeMar', 'United States', 9427, 42.2),
 (1930, 'Clarence DeMar', 'United States', 9288, 42.2),
 (1924, 'Clarence DeMar', 'United States', 8980, 42.0),
 (1922, 'Clarence DeMar', 'United States', 8290, 39.4),
 (1923, 'Clarence DeMar', 'United States', 8627, 39.4),
 (1927, 'Clarence DeMar', 'United States', 9622, 42.2),
 (1928, 'Clarence DeMar', 'United States', 9427, 42.2),
 (1930, 'Clarence DeMar', 'United States', 9288, 42.2)]

expected = {'Clarence DeMar'}

actual = naloge.veckrat(podatki)

test_case.assertEqual(expected, actual, "Napacno vracanje funkcije.")