import unittest
import naloge
import variables

test_case = unittest.TestCase()

expected = list(variables.statistika10.keys())

actual = list(naloge.statistika(variables.slovar_izdelek10).keys())

test_case.assertCountEqual(expected, actual, "Napacni kljuci v slovarju.")
