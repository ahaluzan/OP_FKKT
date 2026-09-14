import unittest
import naloge

test_case = unittest.TestCase()

tempo = 5.52
kategorija = "B"

expected = '01:56:27'
actual = naloge.napoved(tempo, kategorija)

test_case.assertEqual(expected, actual, "Napacna pretvorba za kategorijo B.")