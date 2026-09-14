import unittest
import naloge
import variables

test_case = unittest.TestCase()

expected = variables.naj30

actual = naloge.najvec_vrednosti(variables.slovar30)

test_case.assertEqual(expected, actual, "Napacno vracanje funkcije.")