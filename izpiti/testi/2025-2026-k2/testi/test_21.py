"veckrat"
import unittest
import naloge

test_case = unittest.TestCase()

podatki = []

expected = set()

actual = naloge.veckrat(podatki)

test_case.assertEqual(type(expected), type(actual), "Funkcija vraca napacen podatkovni tip.")