import unittest
import naloge
import variables

test_case = unittest.TestCase()

expected = {'Jacket', 'Socks', 'Sunglasses'}

actual = naloge.po_spolih(variables.shop10, nacin="f")

test_case.assertEqual(expected, actual, "Napacno vracanje funkcije v nacinu 'f'.")