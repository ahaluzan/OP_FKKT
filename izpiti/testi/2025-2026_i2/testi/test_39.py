import unittest
import naloge
import variables

test_case = unittest.TestCase()

expected = {'Gloves', 'Sneakers', 'T-shirt'}

actual = naloge.po_spolih(variables.shop10, "m")

test_case.assertEqual(expected, actual, "Napacno vracanje funkcije v nacinu 'm'.")