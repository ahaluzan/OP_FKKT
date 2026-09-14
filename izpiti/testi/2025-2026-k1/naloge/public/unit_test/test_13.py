import unittest
import naloge

test_case = unittest.TestCase()

tempo = 6.62
kategorija = "A"

expected = '01:06:12'
actual = naloge.napoved(tempo, kategorija)

test_case.assertEqual(expected[:2], actual[:2], "Napacna pretvorba ur.")