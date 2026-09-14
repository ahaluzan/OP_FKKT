import unittest
import naloge

test_case = unittest.TestCase()

niz = "symbols!@#$"
seznam = [11, 0, 2]

expected = "Neveljavni podatki!"

result = naloge.generator_gesel(niz, seznam)

test_case.assertEqual(expected, result, "Napacno vracanje funkcije pri previsokih indeksih.")