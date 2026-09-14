import unittest
import naloge
import variables

test_case = unittest.TestCase()

expected = {'Shoes', 'Sweater'}

actual = naloge.po_spolih(variables.shop30)

test_case.assertEqual(expected, actual, "Napacno vracanje funkcije v nacinu 'skupno'.")