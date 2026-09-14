import unittest
import naloge
import variables

test_case = unittest.TestCase()

expected = variables.statistika10

actual = naloge.statistika(variables.slovar_izdelek10)

test_case.assertEqual(expected, actual, "Napacno vracanje funkcije.")
