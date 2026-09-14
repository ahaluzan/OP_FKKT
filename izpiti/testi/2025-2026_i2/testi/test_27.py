import unittest
import naloge
import variables

test_case = unittest.TestCase()

expected = ('F', ['Outerwear', 'Clothing', 'Clothing'])

actual = naloge.najvec_vrednosti(variables.slovar5)

test_case.assertEqual(expected, actual, "Napacno vracanje funkcije.")