import unittest
import naloge
import variables

test_case = unittest.TestCase()

expected = variables.slovar30_1

actual = naloge.pripravi_slovar(variables.shop30, 3, 2)

test_case.assertCountEqual(expected, actual, "Napacno vracanje funkcije.")