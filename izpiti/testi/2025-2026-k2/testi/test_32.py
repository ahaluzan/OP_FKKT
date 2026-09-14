import unittest
import naloge

test_case = unittest.TestCase()

podatki = [(1927, 'Clarence DeMar', 'United States', 9622, 42.2),
 (1928, 'Clarence DeMar', 'United States', 9427, 42.2),
 (1930, 'Clarence DeMar', 'United States', 9288, 42.2)]

kilometri = 42.2

expected = {'Clarence DeMar'}

actual = naloge.boljse(podatki,kilometri)

test_case.assertEqual(expected, actual, "Napacno delovanje funkcije. Preverite, ali pravilno preverjate izboljsanje casa.")