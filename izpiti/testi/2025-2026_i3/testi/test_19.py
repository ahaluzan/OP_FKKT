import unittest
import naloge
import variables

test_case = unittest.TestCase()

expected = variables.slovar_izdelek20

actual = naloge.v_slovar(variables.kava20)

test_case.assertEqual(expected, actual, "Napacno vracanje funkcije pri kljuc=False.")
