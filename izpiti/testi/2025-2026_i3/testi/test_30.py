import unittest
import naloge
import variables

test_case = unittest.TestCase()

expected = variables.statistika20

actual = naloge.statistika(variables.slovar_izdelek20)

test_case.assertEqual(expected, actual, "Napacno vracanje funkcije.")
