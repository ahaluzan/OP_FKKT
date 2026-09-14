import unittest
import naloge
import variables

test_case = unittest.TestCase()

expected = list(variables.slovar_izdelek5.keys())

actual = list(naloge.v_slovar(variables.kava5).keys())

test_case.assertCountEqual(expected, actual, "Napacni kljuci v slovarju.")
