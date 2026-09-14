import unittest
import naloge
import variables

test_case = unittest.TestCase()

expected = variables.slovar10.values()

actual = naloge.pripravi_slovar(variables.shop10, 0, 1).values()

test_case.assertCountEqual(expected, actual, "Napacne vrednosti.")