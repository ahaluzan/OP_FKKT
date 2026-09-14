import unittest
import naloge

test_case = unittest.TestCase()

podatki = []

expected = set()

actual = naloge.veckrat(podatki)

test_case.assertEqual(expected, actual, "Napacno vracanje funkcije pri praznem seznamu.")