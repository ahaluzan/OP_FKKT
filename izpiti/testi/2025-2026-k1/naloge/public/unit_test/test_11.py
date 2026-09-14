"napoved"
import unittest
import naloge

test_case = unittest.TestCase()

tempo = 5.5
kategorija = "A"

expected = '00:55:00'
actual = naloge.napoved(tempo, kategorija)

test_case.assertEqual(type(expected), type(actual), "Funkcija vraca napacen podatkovni tip.")