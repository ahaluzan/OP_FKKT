import unittest
import naloge

test_case = unittest.TestCase()

niz = ""
seznam = []

expected = "Neveljavni podatki!"

result = naloge.generator_gesel(niz, seznam)

test_case.assertEqual(expected, result, "Napacno vracanje funkcije pri praznem nizu in praznem seznamu.")