import unittest
import naloge

test_case = unittest.TestCase()

tempo = 5.5
kategorija = "A"

expected = '00:55:00'
actual = naloge.napoved(tempo, kategorija)

test_case.assertEqual(len(expected.split(":")), len(actual.split(":")), "Napacen format rezultata.")