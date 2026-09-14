import unittest
import naloge

test_case = unittest.TestCase()

tempo = 7.15
kategorija = "D"

expected = 'Neveljavna kategorija!'
actual = naloge.napoved(tempo, kategorija)

test_case.assertEqual(expected, actual, "Napacno vracanje za neveljavno kategorijo. Preveri tudi tipkarske napake!")