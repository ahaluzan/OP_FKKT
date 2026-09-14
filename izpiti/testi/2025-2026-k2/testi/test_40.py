import unittest
import naloge

test_case = unittest.TestCase()

podatki = [(1900, 'Jack Caffery', 'Canada', 9584, 39.4),
 (1901, 'Jack Caffery', 'Canada', 8963, 39.4),
 (1911, 'Clarence DeMar', 'United States', 8499, 39.4),
 (1922, 'Clarence DeMar', 'United States', 8290, 42.0),
 (1923, 'Clarence DeMar', 'United States', 8627, 39.4)]

kilometri = 39.4

expected = {'Jack Caffery'}

actual = naloge.boljse(podatki,kilometri)

test_case.assertEqual(expected, actual, "Napacno delovanje funkcije.")
