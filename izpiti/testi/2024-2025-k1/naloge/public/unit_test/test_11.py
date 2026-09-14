import unittest
import naloge

test_case = unittest.TestCase()

niz = "numbers123"
seznam = [8, 1, 7]

expected = "2u1"

result = naloge.generator_gesel(niz, seznam)

test_case.assertEqual(expected, result, "Funkcija vraca napacno geslo.")