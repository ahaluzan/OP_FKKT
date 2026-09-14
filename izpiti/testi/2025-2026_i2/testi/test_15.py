import unittest
import naloge
import variables

test_case = unittest.TestCase()

expected = variables.slovar10.keys()

actual = naloge.pripravi_slovar(variables.shop10, 0, 1).keys()

test_case.assertCountEqual(expected, actual, "Napacni kljuci.")