import unittest
import naloge

test_case = unittest.TestCase()

podatki = []

kilometri = 42.2

expected = set()

actual = naloge.boljse(podatki,kilometri)

test_case.assertEqual(expected, actual, "Napacno delovanje funkcije pri praznem seznamu terk.")