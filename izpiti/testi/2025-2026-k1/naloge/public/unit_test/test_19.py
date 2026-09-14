import unittest
import naloge

test_case = unittest.TestCase()

tempo = 7.15
kategorija = "C"

expected = '05:01:41'
actual = naloge.napoved(tempo, kategorija)

test_case.assertEqual(expected, actual, "Napacna pretvorba za kategorijo C.")