import unittest
import naloge
import variables

test_case = unittest.TestCase()

expected = variables.slovar_spol10

actual = naloge.v_slovar(variables.kava10, kljuc=True)

test_case.assertEqual(expected, actual, "Napacno vracanje funkcije pri kljuc=True.")
