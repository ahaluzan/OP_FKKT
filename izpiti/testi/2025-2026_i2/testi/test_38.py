import unittest
import naloge
import variables

test_case = unittest.TestCase()

expected = {'Blouse', 'Gloves', 'Handbag', 'Skirt', 'Socks'}

actual = naloge.po_spolih(variables.shop20, nacin="f")

test_case.assertEqual(expected, actual, "Napacno vracanje funkcije v nacinu 'f'.")