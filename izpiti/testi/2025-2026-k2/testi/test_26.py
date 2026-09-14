import unittest
import naloge

test_case = unittest.TestCase()

podatki = [(1902, 'Sammy Mellor', 'United States', 9792, 39.4),
    (1922, 'Clarence DeMar', 'United States', 8290, 39.4),
 (1903, 'John Lordan', 'United States', 9689, 39.4),
 (1904, 'Michael Spring', 'United States', 9484, 39.4),
 (1917, 'Bill Kennedy', 'United States', 8917, 39.4),
 (1919, 'Carl Linder', 'United States', 8953, 39.4),
 (1923, 'Clarence DeMar', 'United States', 8627, 39.4)]

expected = {'Clarence DeMar'}

actual = naloge.veckrat(podatki)

test_case.assertEqual(expected, actual, "Napacno vracanje funkcije.")