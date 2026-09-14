import unittest
import naloge
import variables

test_case = unittest.TestCase()

expected = {'Sweater'}

actual = naloge.po_spolih(variables.shop10)

test_case.assertEqual(expected, actual, "Napacno vracanje funkcije v nacinu 'skupno'.")