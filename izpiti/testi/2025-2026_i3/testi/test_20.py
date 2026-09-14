import unittest
import naloge
import variables

test_case = unittest.TestCase()

expected = variables.slovar_spol20

actual = naloge.v_slovar(variables.kava20, kljuc=True)

test_case.assertEqual(expected, actual, "Napacno vracanje funkcije pri kljuc=True.")
