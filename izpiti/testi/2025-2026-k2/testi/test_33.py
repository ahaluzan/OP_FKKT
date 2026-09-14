import unittest
import naloge

test_case = unittest.TestCase()

podatki = [(1927, 'Clarence DeMar', 'United States', 9622, 42.2),
 (1928, 'Clarence DeMar', 'United States', 9827, 42.2),
 (1930, 'Clarence DeMar', 'United States', 9888, 42.2)]

kilometri = 42.2

expected = set()

actual = naloge.boljse(podatki,kilometri)

test_case.assertEqual(expected, actual, "Napacno delovanje funkcije. Preverite, ali pravilno preverjate izboljsanje casa.")