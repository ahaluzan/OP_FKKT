import unittest
import naloge
import variables

test_case = unittest.TestCase()

expected = variables.slovar20

actual = naloge.pripravi_slovar(variables.shop20, 1, 2)

test_case.assertCountEqual(expected, actual, "Napacno vracanje funkcije.")