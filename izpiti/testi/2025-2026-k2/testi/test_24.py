import unittest
import naloge

test_case = unittest.TestCase()

podatki = [(1994, 'Uta Pippig', 'Germany', 8505, 42.2)]

expected = set()

actual = naloge.veckrat(podatki)

test_case.assertEqual(expected, actual, "Napacno vracanje funkcije.")