import unittest
import naloge
import variables

test_case = unittest.TestCase()

expected = variables.naj20

actual = naloge.najvec_vrednosti(variables.slovar20)

test_case.assertEqual(expected, actual, "Napacno vracanje funkcije.")