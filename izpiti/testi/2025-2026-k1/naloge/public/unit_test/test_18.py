import unittest
import naloge

test_case = unittest.TestCase()

tempo = 5.52
kategorija = "C"

expected = '03:52:54'
actual = naloge.napoved(tempo, kategorija)

test_case.assertEqual(expected, actual, "Napacna pretvorba za kategorijo C.")