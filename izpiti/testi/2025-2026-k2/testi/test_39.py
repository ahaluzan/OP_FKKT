import unittest
import naloge

test_case = unittest.TestCase()

podatki = [(1974, 'Miki Gorman', 'United States', 10031, 42.2),
 (1977, 'Miki Gorman', 'United States', 10113, 42.2),
 (1986, 'Ingrid Kristiansen', 'Norway', 8695, 42.2),
 (1989, 'Ingrid Kristiansen', 'Norway', 8673, 42.2),
 (2006, 'Rita Jeptoo', 'Kenya', 8618, 42.2),
 (2013, 'Rita Jeptoo', 'Kenya', 8785, 42.2)]

kilometri = 42.2

expected = {'Ingrid Kristiansen'}

actual = naloge.boljse(podatki,kilometri)

test_case.assertEqual(expected, actual, "Napacno delovanje funkcije.")