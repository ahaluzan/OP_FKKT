'''generator_gesel'''
import unittest
import naloge

test_case = unittest.TestCase()

niz = "oneofthecases"
seznam = [0,7,2]

expected = "oee"

result = naloge.generator_gesel(niz, seznam)

test_case.assertEqual(type(expected), type(result), "Funkcija vraca napacen podatkovni tip.")