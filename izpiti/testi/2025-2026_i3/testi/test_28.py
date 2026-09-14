import unittest
import naloge
import variables

test_case = unittest.TestCase()

expected = variables.statistika5

actual = naloge.statistika(variables.slovar_izdelek5)

test_case.assertEqual(expected, actual, "Napacno vracanje funkcije.")
