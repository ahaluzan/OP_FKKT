import unittest
import naloge

test_case = unittest.TestCase()

tempo = 6.62
kategorija = "B"

expected = '02:19:39'
actual = naloge.napoved(tempo, kategorija)

test_case.assertEqual(expected, actual, "Napacna pretvorba za kategorijo B.")