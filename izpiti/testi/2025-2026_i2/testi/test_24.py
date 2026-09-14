import unittest
import naloge
import variables

test_case = unittest.TestCase()

expected = variables.naj10

actual = naloge.najvec_vrednosti(variables.naj_slovar10)

test_case.assertEqual(expected, actual, "Napacno vracanje funkcije.")