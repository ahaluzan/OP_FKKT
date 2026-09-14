import unittest
import naloge
import variables

test_case = unittest.TestCase()

expected = list(variables.statistika5.keys())

actual = list(naloge.statistika(variables.slovar_izdelek5).keys())

test_case.assertCountEqual(expected, actual, "Napacni kljuci v slovarju.")
