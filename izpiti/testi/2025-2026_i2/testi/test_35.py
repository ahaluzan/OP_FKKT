import unittest
import naloge
import variables

test_case = unittest.TestCase()

expected = {'Pants', 'Shirt'}

actual = naloge.po_spolih(variables.shop20)

test_case.assertEqual(expected, actual, "Napacno vracanje funkcije v nacinu 'skupno'.")